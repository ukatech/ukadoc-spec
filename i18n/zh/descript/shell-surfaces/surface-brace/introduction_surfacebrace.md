# surface 块示例

```
surface1
{
element0,overlay,body0.png,0,0
element1,overlay,face0.png,0,0

collision0,188,25,252,63,Head
collision1,190,92,236,118,Face
collision2,180,191,220,222,Bust
collision3,154,311,248,362,Skirt

animation0.interval,sometimes
animation0.pattern0,overlay,101,100,168,67
animation0.pattern1,overlay,100,100,168,67
animation0.pattern2,overlay,101,100,168,67
animation0.pattern3,overlay,-1,100,168,67
}
```

仅 SSP 支持用于追加指定（在已定义内容上追加定义）的写法surace.append。<br />
详情请参见[下文](caption_surface.append.md)。

```
surface.append1-9,20-29
{
// 略（ふつうのsurfaceブレスと同様）
}
```

在surface(.append)\*的\*部分指定作为 surface ID 的数字。可以指定多个 ID，也可以指定范围（[下文](caption_surfacebraceid.md)）。

其他各行中的数字部分请参见相应定义的说明。
