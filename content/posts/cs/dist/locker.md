+++
author = "zenk"
slug = ""
tags = ["dist"]
draft = true
categories=["cs"]
title="分布式锁"
description="分布式锁原理和实践"
date="2018-11-23T14:00:51+08:00"

+++

redis实现

[redission](https://github.com/redisson/redisson)

```
// lock KEYS: locker key, ARGV: lease time millis, locker name
// reenter locker
if (redis.call('exists', KEYS[1]) == 0) then
    redis.call('hset', KEYS[1], ARGV[2], 1);
    redis.call('pexpire', KEYS[1], ARGV[1]);
        return nil;
end;
if (redis.call('hexists', KEYS[1], ARGV[2]) == 1) then
    redis.call('hincrby', KEYS[1], ARGV[2], 1);
    redis.call('pexpire', KEYS[1], ARGV[1]);
        return nil;
end;
return redis.call('pttl', KEYS[1]);

// unlock KEYS: locker key, channel ARGV: unlock flag(0), lease time in millis, locker name
if (redis.call('exists', KEYS[1]) == 0) then
    redis.call('publish', KEYS[2], ARGV[1]);
        return 1;
end;
if (redis.call('hexists', KEYS[1], ARGV[3]) == 0) then
    return nil;
end;
local counter = redis.call('hincrby', KEYS[1], ARGV[3], -1);
if (counter > 0) then
    redis.call('pexpire', KEYS[1], ARGV[2]);
    return 0;        
else
    redis.call('del', KEYS[1]);
    redis.call('publish', KEYS[2], ARGV[1]);
    return 1;
end;
return nil;

// force unlock KEYS: locker key, channel ARGV: unlock flag(0)
if (redis.call('del', KEYS[1]) == 1) then
    redis.call('publish', KEYS[2], ARGV[1]);
    return 1
else
    return 0
end
```



