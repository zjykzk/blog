+++
author = "zenk"
slug = ""
tags = ["rocketmq"]
draft = false
categories=["cs"]
title="RocketMQ push模式的实现细节"
description="RocketMQ push模式功能和实现细节。"
date="2019-01-16T16:54:09+08:00"

+++


Rocketmq使用常轮询的方式实现了push功能。主要包括几个组件：

1. DefaultMQPushConsumerImpl：拉消息的类型。
2. ProcessQueue：保存拉出来的消息。
3. PullMessageService：执行拉消息服务。
4. ConsumeMessageService：消费消息服务。
5. ReblanceService：负载均衡服务。

**类关系**

![](/imgs/rocketmq/push-consumer-class.jpeg)

（真想吐槽！）

**执行过程**

![](/imgs/rocketmq/push-consumer-active.jpeg)

## DefaultMQPushConsumerImpl

`DefaultMQPushConsumerImpl`实现了消费者的接口。同时是个启动者，通过它直接或间接启动了拉消息服务，消费消息服务。

其中提供了一个重要的接口`pullMessage`。该接口的流程如下：

![](/imgs/rocketmq/push-consumer-pull.png)

在拉消息过程中，做了流控，防止拉的太快，消费的太慢。主要从三个方面检测：

1. 从某个消费队列拉取的等待消费的消息数量。如果超过阀值，延迟50ms后再次拉取消息。阀值默认是1000。如果设置了topic级别的阀值（默认没有限制），在队列负载均衡以后会重新计算，具体为topic级别的阀值除以当前负责的消费队列数量。主要配置变量：`DefaultMQPushConsumerImpl.pullThresholdForQueue`和`DefaultMQPushConsumerImpl.pullThresholdForTopic`。
2. 从某个消费队列拉取的等待消费的消息大小（只考虑body）。同样，超过阀值就会延迟50ms后再次拉取消息。阀值默认是100M。如果topic设置了级别（默认没有限制），队列负载均衡以后会重新计算队列的限制，具体为topic级别的阀值除以当前负责的消费队列数量。主要配置变量：`DefaultMQPushConsumerImpl.pullThresholdSizeForQueue`和`DefaultMQPushConsumerImpl.pullThresholdSizeForTopic`。
3. 在并发消费模式下，从某个消费队列拉取的等待消费的消息中，在消费队列中的最大位置和最小位置之间差别。如果超过阀值，也会延迟50ms后再拉取消息。默认是2000，这里可能会存在误判。因为，有条件拉取消息的时候，是有可能出现同一个消费队列中拉到的两个消息在队列中的位置距离很远。

**几个考虑：**

* `NO_NEW_MSG/NO_MATCHED_MSG`情况下，`correctTagsOffset`的逻辑为什么需要考虑有没有消息？如果还有消息说明本地还没有消息没被消费，此时更新的offset是服务端返回的，存在比没有被消费的消息偏移量大的情况。

* `OFFSET_ILLEAGL`的情况下为什么要过10s以后才去更新offsetstore，保存offset，在reblance中移除process queue？出现这个问题是因为`NO_MATCHED_LOGIC_QUEUE/NO_MESSAGE_IN_QUEUE/OFFSET_OVERFLOW_BADLY/OFFSET_TOO_SMALL`这四种情况，而这些情况可能发生在服务端在恢复数据的时候，因此考虑是暂停消费这个队列。如果drop之后不延迟，就会有可能又去拉取消息了。

## ProcessQueue

保存push的消费者拉到的消息。同时，有序消费模式还记录了情况下正在消费的消息。

## PullMessageService

`PullMessageService`只负责拉取消息，它会调用`DefaultMQPushConsumerImpl.pullMessage`。

当`ReblanceService`执行负载均衡的时候如果发现被分配了新的消息队列就会最终调用`PullMessage.executePullRequestImmediately`执行拉取消息。代码执行路径：

```
ReblanceService.run
->MQClientInstance.doReblance
->MQConsumerInnter.doReblance[DefaultMQPushConsumerImpl.doReblance]
->ReblanceImpl.doReblance
->ReblanceImpl.dispatchPullRequest[ReblancePushImpl.dispatchPullRequest]
->DefaultMQPushConsumerImpl.executePullRequestImmediately
->PullMessage.executePullRequestImmediately
```

另外，在`DefaultMQPushConsumerImpl.pullMessage`执行时，也会根据条件调用`PullMessageService.executePullRequestImmediately`、`PullMessageService.executeTaskLater`或者`PullMessageService.executePullRequestLater`触发拉取消息。

## ConsumeMessageService

消费服务分并发消费和顺序消费，主要区别在于提交消费任务逻辑，消费逻辑和处理消费结果的逻辑，以及对message queue的处理逻辑。另外，顺序消费是指在同一个消费队列里面的消息顺序消费。

**提交消费任务**

并发消费：把消息分成多个批次并发处理，一批多少个消息是自定义的，默认是1。如果提交异常，则延迟5s后提交。

顺序消费：依赖于process queue是否正在被消费，这样避免同时消费多个不同的消息，不然就没法保证有序了。

**消费逻辑**

下图中左边是*并发消费*，右边是*顺序消费*。

![](/imgs/rocketmq/push-consumer-consume.jpeg)

消费消息的时候，在可能停顿的执行点上面都加上了process queue是否已经drop的检查。

因为提交任务的方式不一样导致了不同模式下面消费逻辑的差别。并发消费只考虑当前的消息即可，而顺序消费却要在这里从process queue中取消息。

顺序消费的时候需要确保：

1. 每个消费队列某一时候只有一个消费请求被执行。
2. 每个消费队列某一时刻只有一个地方在执行用户的消费逻辑。

以上两个条件中只要一个条件不满足，就没法保证消息顺序消费。但是，在代码层面第一个逻辑已经确保了第二个逻辑。另外，第一个逻辑需要的锁，是因为消费慢，同时队列被分配别的消费者，在消费结束之前又分配回来了，就有可能导致1条件不满足，所以需要加锁。

**处理消费结果**

下图中左边是并发消费，右边是顺序消费。

![](/imgs/rocketmq/push-consumer-result.jpeg)

处理消费结果的逻辑主要是处理消费失败的消息。

并发消费：如果是在广播模式下，直接丢弃了。如果是在集群模式下面会尝试把消息发回broker，如果发送失败的话，就会把这些发送失败的消息延迟提交消费。

顺序模式：如果是`ROLLBACK`，把消息放回，再次消费。如果是`SUSPEND_CURRENT_QUEUE_A_MOMENT`则会判断是否需要停止一段时间再消费。通过检查消费次数，当超过预定的值（默认是没有限制）就会把消息发回broker。如果消息都已经发回broker，就提交消息接下去消费，否则就停一会，把当前的消息延迟提交消费。

**处理message queue**

并发消费：定时清理长时间没法消费的消息，默认是15分钟。

顺序消费：在集群模式下面，定时向broker锁住message queue，锁的粒度是group+clientID。