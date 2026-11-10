# surface brace 範例

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

僅 SSP 提供用於追加指定（在已定義的項目上追加定義）的記法surace.append。<br />
詳細請參閱[後述](caption_surface.append.md)。

```
surface.append1-9,20-29
{
// 略（ふつうのsurfaceブレスと同様）
}
```

在surface(.append)\*的\*部分指定作為表面 ID 的數字。可指定多個數字或指定範圍（[後述](caption_surfacebraceid.md)）。

其他各行的數字部分，請參閱各項定義的說明。
