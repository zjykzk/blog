"""Deterministic 1080p tactical animation. All players are schematic tokens."""
import argparse
import functools
import json
import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
CFG=json.loads((ROOT/'video.json').read_text())
W,H=CFG['width'],CFG['height']
FPS=CFG['fps']
BG='#0B151B'; WHITE='#F3F4ED'; MUTED='#8FA7A9'; MINT='#B7F76D'; BLUE='#73C7F5'; ORANGE='#FFAD77'
FONT='/System/Library/Fonts/STHeiti Medium.ttc'
FONT_LIGHT='/System/Library/Fonts/STHeiti Light.ttc'
FX,FY,FW,FH=660,186,1196,694
CAPTIONS=json.loads((ROOT/'captions.json').read_text()) if (ROOT/'captions.json').exists() else []


@functools.lru_cache(maxsize=64)
def font(size,light=False):
    return ImageFont.truetype(FONT_LIGHT if light else FONT,size)


def text(draw, xy, value, size=32, fill=WHITE, anchor='lt', light=False):
    draw.text(xy,value,font=font(size,light),fill=fill,anchor=anchor)


def lines(draw,xy,value,size,width,fill=WHITE,spacing=12):
    chunks=[]; chunk=''
    for char in value:
        if draw.textlength(chunk+char,font=font(size))>width:
            chunks.append(chunk);chunk=char
        else:chunk+=char
    if chunk: chunks.append(chunk)
    for i,line in enumerate(chunks):text(draw,(xy[0],xy[1]+i*(size+spacing)),line,size,fill)
    return len(chunks)


def point(p):return (FX+int(p[0]*FW),FY+int(p[1]*FH))


def smooth(x):
    x=min(1,max(0,x));return x*x*(3-2*x)


def lerp(a,b,p):return tuple(x+(y-x)*p for x,y in zip(a,b))


def sample(keys,t):
    if t<=keys[0][0]:return keys[0][1:]
    for before,after in zip(keys,keys[1:]):
        if t<=after[0]:return lerp(before[1:],after[1:],smooth((t-before[0])/(after[0]-before[0])))
    return keys[-1][1:]


def arrow(draw,a,b,fill=MINT,width=5,dashed=False,head=16):
    ax,ay=a;bx,by=b;length=math.hypot(bx-ax,by-ay)
    if length<1:return
    ux,uy=(bx-ax)/length,(by-ay)/length
    if dashed:
        for start in range(0,int(length)-head,23):
            end=min(start+12,length-head)
            if end>start:draw.line((ax+ux*start,ay+uy*start,ax+ux*end,ay+uy*end),fill=fill,width=width)
    else:draw.line((a,b),fill=fill,width=width)
    draw.polygon([(bx,by),(bx-ux*head-uy*head*.55,by-uy*head+ux*head*.55),
                  (bx-ux*head+uy*head*.55,by-uy*head-ux*head*.55)],fill=fill)


def chip(draw,p,label,fill=WHITE,bg='#18332F',size=25):
    tw=draw.textlength(label,font=font(size))
    x,y=p
    draw.rounded_rectangle((x-tw/2-18,y-10,x+tw/2+18,y+size+10),radius=10,fill=bg)
    text(draw,(x,y),label,size,fill,'mt')


@functools.lru_cache(maxsize=12)
def base(index):
    sc=CFG['scenes'][index]
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    d.rounded_rectangle((72,58,82,97),radius=4,fill=MINT)
    text(d,(101,64),'足球过人的本质',31)
    text(d,(1856,68),'U12  /  1v1 认知训练',25,MUTED,'rt')
    d.line((72,132,1856,132),fill='#26383F',width=2)
    text(d,(72,223),sc['chapter'],27,MINT)
    for j,heading in enumerate(sc['title']):
        size=60
        while d.textlength(heading,font=font(size))>532:size-=1
        text(d,(72,313+j*88),heading,size)
    d.line((72,534,149,534),fill=MINT,width=4)
    lines(d,(72,571),sc['key'],31,504,WHITE,14)
    lines(d,(72,713),sc['hint'],25,490,MUTED,13)
    text(d,(72,856),f'{index+1:02} / {len(CFG["scenes"]):02}',22,MUTED)
    # Half-pitch, subdued stripes; keep player movement uncluttered.
    d.rounded_rectangle((FX,FY,FX+FW,FY+FH),radius=28,fill='#12382D')
    for x in range(1,8,2):
        d.rectangle((FX+x*FW/8,FY+3,FX+(x+1)*FW/8,FY+FH-3),fill='#143D30')
    c='#3C6751'
    d.rectangle((FX+35,FY+30,FX+FW-35,FY+FH-30),outline=c,width=3)
    d.rectangle((FX+FW*.30,FY+30,FX+FW*.70,FY+145),outline=c,width=3)
    d.rectangle((FX+FW*.425,FY+30,FX+FW*.575,FY+80),outline=c,width=2)
    d.arc((FX+FW*.425,FY+80,FX+FW*.575,FY+224),0,180,fill=c,width=3)
    d.arc((FX+FW/2-155,FY+FH-170,FX+FW/2+155,FY+FH+140),180,360,fill=c,width=3)
    text(d,(FX+FW-28,FY+FH-62),'进攻方向 ↑',22,'#83A894','rt')
    for x,color,label in [(FX+10,BLUE,'进攻者'),(FX+217,ORANGE,'防守者'),(FX+432,WHITE,'球')]:
        d.ellipse((x,916,x+16,932),fill=color)
        text(d,(x+29,910),label,24,MUTED)
    text(d,(FX+FW,911),'覆盖与承重均为示意',21,MUTED,'rt')
    d.rectangle((0,963,W,H),fill='#081014')
    return im


def coverage(im,position,shift=0):
    overlay=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(overlay)
    x,y=point(position);x+=shift*44
    box=(x-135,y-82,x+135,y+121)
    d.ellipse(box,fill=(255,173,119,23))
    for degree in range(0,360,16):d.arc(box,degree,degree+8,fill=(255,173,119,135),width=3)
    im.paste(overlay,(0,0),overlay)


def corridor(im,start,end):
    overlay=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(overlay)
    a,b=point(start),point(end)
    d.line((a,b),fill=(183,247,109,22),width=85)
    d.ellipse((b[0]-49,b[1]-49,b[0]+49,b[1]+49),fill=(183,247,109,30))
    im.paste(overlay,(0,0),overlay)
    arrow(ImageDraw.Draw(im),a,b,MINT,4,True,18)


def player(draw,pos,defender=False,heading=-math.pi/2,lean=0):
    x,y=point(pos);r=33 if defender else 25;color=ORANGE if defender else BLUE
    draw.ellipse((x-r+3,y-r+8,x+r+3,y+r+8),fill='#0B251E')
    draw.ellipse((x-r,y-r,x+r,y+r),fill=color,outline=WHITE if not defender else '#FFC8A2',width=3)
    text(draw,(x,y+1),'4' if defender else '7',25 if defender else 22,'#112523','mm')
    dx,dy=math.cos(heading),math.sin(heading)
    nx,ny=-dy,dx
    draw.polygon([(x+dx*(r+14),y+dy*(r+14)),(x+dx*(r+2)+nx*7,y+dy*(r+2)+ny*7),
                  (x+dx*(r+2)-nx*7,y+dy*(r+2)-ny*7)],fill=color)
    if lean:
        draw.ellipse((x+lean*38-8,y+47,x+lean*38+8,y+63),fill=MINT)
        arrow(draw,(x,y+56),(x+lean*70,y+56),MINT,3,False,10)


def ball(draw,pos):
    x,y=pos;r=11
    draw.ellipse((x-r+2,y-r+4,x+r+2,y+r+4),fill='#0C231E')
    draw.ellipse((x-r,y-r,x+r,y+r),fill=WHITE,outline='#D4E2D5',width=2)
    draw.regular_polygon((x,y,5),n_sides=5,rotation=20,fill='#25433E')


def success_keys(duration=8):
    a=[(0,.45,.81),(duration*.25,.44,.68),(duration*.40,.415,.65),
       (duration*.53,.435,.64),(duration*.76,.65,.34),(duration,.77,.15)]
    d=[(0,.46,.40),(duration*.35,.45,.44),(duration*.49,.35,.46),
       (duration*.63,.35,.46),(duration*.82,.46,.37),(duration,.56,.27)]
    return a,d


def motion(scene,t):
    sid=scene['id'];dur=scene['end']-scene['start'];lean=0;status='';color=MINT
    route=False;phase=0;trialfade=1
    if sid=='opening':
        phase=0 if t<3.8 else 1
        local=t if phase==0 else min(3.4,t-3.8)
        a=[(0,.45 if phase==0 else .41,.80),(2.1,.45 if phase==0 else .41,.605)]
        d=[(0,.45,.42),(1.8,.45 if phase==0 else .42,.46)]
        status='正面硬冲 ×' if phase==0 else '拼身体 ×';color=ORANGE
        at=local
    elif sid=='distance':
        cues=[c for c in CAPTIONS if c['scene']==sid]
        near_end=(cues[1]['start']-scene['start']) if len(cues)>1 else 4
        far_end=(cues[2]['start']-scene['start']) if len(cues)>2 else 7
        phase=0 if t<near_end else 1 if t<far_end else 2
        y=[.565,.85,.655][phase]
        a=[(0,.45,y)];d=[(0,.45,.40)]
        status=['太近 ×','太远 ×','合适距离'][phase]
        color=ORANGE if phase<2 else MINT;at=t
    else:
        action_dur=dur-1.6
        a,d=success_keys(action_dur);at=max(0,t-.6)
        if sid=='momentum':
            a=[(0,.45,.70),(3,.41,.66),(4.5,.42,.64),(7.5,.65,.36),(8.7,.74,.22)]
            d=[(0,.46,.42),(3,.35,.46),(5,.35,.46),(8.7,.50,.33)]
            lean=-smooth(min(at,3)/3) if at<5 else -.3
            status='向左移动 → 向右需要再调整';route=at>3
        elif sid=='feint':
            a=[(0,.45,.73),(2.4,.41,.68),(4.4,.42,.68),(8,.66,.36),(10,.76,.21)]
            d=[(0,.46,.43),(2,.45,.45),(4.4,.35,.48),(6.4,.35,.48),(10,.53,.31)]
            lean=-smooth(at/4.4) if at<6.4 else -.25
            status='身体向左 · 诱导' if at<3 else '向左承重 · 等反应' if at<4.6 else '右侧出现空当 · 突破'
            route=at>=4.4
        elif sid=='diagonal':
            if t<3.8:
                a=[(0,.45,.80),(2,.45,.605)];d=[(0,.45,.42),(1.8,.45,.46)]
                at=t;status='正面撞力量 ×';color=ORANGE;phase=0
            else:
                a,d=success_keys(7.3);at=t-3.8;status='从侧面斜向突破';route=at>3;phase=1
        elif sid=='tempo':
            a=[(0,.45,.87),(1.8,.45,.67),(4.4,.43,.65),(5.4,.43,.65),(8,.66,.34),(10.4,.76,.19)]
            d=[(0,.46,.41),(2.6,.45,.44),(4.9,.36,.47),(6,.36,.47),(10.4,.55,.28)]
            status='快 · 接近' if at<2 else '慢 · 观察' if at<5.4 else '快 · 启动';route=at>5.4
        elif sid=='firststep':
            a=[(0,.49,.67),(1.3,.50,.63),(4.7,.72,.32),(7.8,.79,.14)]
            d=[(0,.37,.46),(2.2,.37,.46),(4.4,.49,.40),(7.8,.59,.28)]
            status='进入侧面 → 防守者转身换步';route=True
        elif sid=='questions':
            a,d=success_keys(10)
            cues=[c for c in CAPTIONS if c['scene']==sid]
            active=[j for j,c in enumerate(cues) if t+scene['start']>=c['start']]
            phase=active[-1] if active else 0
            status=['① 重心在哪？','② 让他往哪边动？','③ 哪一侧有空间？','④ 什么时候加速？'][min(phase,3)]
            route=phase>=2;lean=-.8 if phase in (1,2) else 0
        elif sid=='recap':
            phase=min(4,int(t/2));status=['保持距离','减速观察','诱导重心','斜向突破','第一步加速'][phase]
            route=t>5
        elif sid=='ending':
            a,d=success_keys(6)
            status='小个不要比力量，让大个改变方向';route=at>2.5
        else:
            status='先调动对手，再进入空间';route=at>action_dur*.43
    ap=sample(a,at);dp=sample(d,at)
    # Interpolate headings as well as positions so the ball never snaps around a stopped token.
    angles=[]
    for k,node in enumerate(a):
        candidates=[q for q in a[k+1:] if math.hypot(q[1]-node[1],q[2]-node[2])>.001]
        if candidates:
            q=candidates[0];angle=math.atan2((q[2]-node[2])*FH,(q[1]-node[1])*FW)
        else:angle=angles[-1][1] if angles else -math.pi/2
        if angles:
            while angle-angles[-1][1]>math.pi:angle-=math.tau
            while angle-angles[-1][1]<-math.pi:angle+=math.tau
        angles.append((node[0],angle))
    head=sample(angles,at)[0]
    # Keep the ball outside the player glyph. Extra separation models a controlled release,
    # followed by the player's run, never a ball passing through the defender.
    forward=49+5*math.sin(at*6)**2 if len(a)>1 else 49
    if sid=='firststep':forward+=15*math.sin(min(1,max(0,(at-1.3)/3.4))*math.pi)
    ax,ay=point(ap)
    bp=(ax+math.cos(head)*forward,ay+math.sin(head)*forward)
    return {'a':ap,'d':dp,'ball':bp,'heading':head,'lean':lean,'status':status,'color':color,'route':route,'phase':phase,'time':at}


def scene_frame(index,t):
    sc=CFG['scenes'][index];local=t-sc['start']
    im=base(index).copy();m=motion(sc,local)
    if sc['id']=='ending' and local<3.5:
        dd=ImageDraw.Draw(im)
        dd.rectangle((65,297,639,515),fill=BG)
        text(dd,(72,313),'别和大个比力量',56)
        text(dd,(72,401),'让他改变方向',60,MINT)
    coverage(im,m['d'],m['lean'])
    if m['route']:corridor(im,(.52,.64),(.76,.22))
    d=ImageDraw.Draw(im)
    if sc['id'] in ('opening','distance','diagonal'):
        total=3 if sc['id']=='distance' else 2
        text(d,(FX+54,FY+43),f'对比 {m["phase"]+1} / {total}',24,MUTED)
    if sc['id']=='distance':
        ax,ay=point(m['a']);dx,dy=point(m['d'])
        d.line((ax+145,ay,dx+145,dy),fill=m['color'],width=3)
        d.line((ax+133,ay,ax+157,ay),fill=m['color'],width=3)
        d.line((dx+133,dy,dx+157,dy),fill=m['color'],width=3)
        text(d,(ax+168,(ay+dy)/2),'判断距离',25,m['color'],'lm')
        if m['phase']==0:
            arrow(d,point(m['d']),m['ball'],ORANGE,7,False,15)
        if m['phase']==1:chip(d,point((.72,.46)),'防守者无需移动',MUTED,size=24)
    if sc['id']=='opening' or (sc['id']=='diagonal' and m['phase']==0):
        arrow(d,point((.45,.84)),point((.45,.57)),ORANGE,4,True)
        if m['time']>2:
            bx,by=m['ball'];d.line((bx-18,by-16,bx+18,by+16),fill=ORANGE,width=4)
            d.line((bx-18,by+16,bx+18,by-16),fill=ORANGE,width=4)
    if sc['id']=='momentum':
        arrow(d,point((.49,.32)),point((.29,.32)),ORANGE,5)
        chip(d,point((.40,.23)),'移动方向',ORANGE,size=23)
    if sc['id']=='feint' and m['time']<4.6:
        arrow(d,point((.44,.67)),point((.32,.64)),BLUE,5)
        chip(d,point((.69,.55)),'观察支撑与承重',MINT,size=24)
    if sc['id']=='diagonal' and m['phase']==1 and m['time']>2:
        x,y=point((.47,.66));arrow(d,(x,y),(x,y-164),'#608678',2,True,8)
        d.arc((x-75,y-75,x+75,y+75),270,315,fill=MINT,width=3)
        text(d,(x+53,y-127),'约45°',25,MINT)
    if sc['id']=='tempo':
        label='快' if m['time']<2 or m['time']>5.4 else '慢'
        chip(d,point((.78,.71)),label,BLUE,size=36)
    ax,ay=point(m['a']);dx,dy=point(m['d'])
    player(d,m['d'],True,heading=math.atan2(ay-dy,ax-dx),lean=m['lean'])
    player(d,m['a'],heading=m['heading'])
    ball(d,m['ball'])
    chip(d,(FX+FW/2,FY+FH-45),m['status'],m['color'],size=26)
    if sc['id']=='space':
        dx,dy=point(m['d']);chip(d,(dx,dy-134),'当下覆盖范围',ORANGE,size=24)
        if m['route']:chip(d,point((.80,.43)),'空当',MINT,size=30)
    if sc['id']=='recap':
        labels=['距离','节奏','重心','方向','加速']
        for j,label in enumerate(labels):
            x=FX+102+j*235
            d.rounded_rectangle((x-67,FY+35,x+67,FY+86),radius=12,fill=MINT if j==m['phase'] else '#15362C')
            text(d,(x,FY+46),label,26,BG if j==m['phase'] else MUTED,'mt')
    if sc['id']=='ending' and local>=6.3:
        opacity=smooth((local-6.3)/.45)
        card=Image.new('RGB',(W,H),BG);cd=ImageDraw.Draw(card)
        text(cd,(W/2,190),'足球过人的本质',33,MUTED,'mt')
        text(cd,(W/2,345),'我要让防守者',94,WHITE,'mt')
        text(cd,(W/2,476),'做什么？',115,MINT,'mt')
        text(cd,(W/2,709),'观察 → 诱导 → 空间 → 突破',40,WHITE,'mt')
        text(cd,(W/2,821),'先读反应，再抓住时间差',27,MUTED,'mt')
        im=Image.blend(im,card,opacity);d=ImageDraw.Draw(im)
    subtitle=next((c['text'] for c in CAPTIONS if c['start']<=t<=c['end']),None)
    if subtitle:
        size=37
        while d.textlength(subtitle,font=font(size))>1740:size-=1
        text(d,(W/2,996),subtitle,size,WHITE,'mt')
    d.rectangle((0,H-5,int(W*t/CFG['duration']),H),fill=MINT)
    return im


def frame(t):
    index=next((i for i,s in enumerate(CFG['scenes']) if s['start']<=t<s['end']),len(CFG['scenes'])-1)
    return scene_frame(index,t)


def render():
    out=ROOT/'football-dribbling-120s-1080p.mp4'
    cmd=['ffmpeg','-hide_banner','-loglevel','warning','-y','-f','rawvideo','-pix_fmt','rgb24',
         '-s',f'{W}x{H}','-r',str(FPS),'-i','-', '-i',str(ROOT/'_build/mix.wav'),
         '-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-threads','4',
         '-c:a','aac','-b:a','192k','-ar','48000','-t',str(CFG['duration']),
         '-movflags','+faststart','-metadata','title='+CFG['title'],str(out)]
    process=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for i in range(FPS*CFG['duration']):
            process.stdin.write(frame(i/FPS).tobytes())
            if i%(FPS*10)==0:print(f'Rendered {i//FPS:03} / {CFG["duration"]} seconds',flush=True)
        process.stdin.close()
        if process.wait():raise RuntimeError('ffmpeg encode failed')
    finally:
        if process.poll() is None:process.terminate()
    print(out,flush=True)


def previews():
    (ROOT/'stills').mkdir(exist_ok=True)
    times=[2.6,15,22,30,34.5,39.5,48,60,72.5,82,93,103,117]
    for i,t in enumerate(times):frame(t).save(ROOT/'stills'/f'{i+1:02}-{t:05.1f}s.jpg',quality=91)
    frame(117).save(ROOT/'poster.jpg',quality=94)
    width=640;height=360
    sheet=Image.new('RGB',(width*3,height*5),'#0B151B')
    for i,t in enumerate(times):
        small=frame(t).resize((width,height),Image.Resampling.LANCZOS)
        sheet.paste(small,((i%3)*width,(i//3)*height))
    sheet.save(ROOT/'contact-sheet.jpg',quality=92)
    print('Previews ready',flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--preview',action='store_true')
    args=parser.parse_args()
    previews()
    if not args.preview:render()
