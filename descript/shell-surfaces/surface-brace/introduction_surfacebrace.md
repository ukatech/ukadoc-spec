# surfaceブレス記述例

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

SSPのみ追加指定（すでに定義済みのものに対してさらに定義を後付けする）用記法surace.appendがある。<br />
詳細は[後述](caption_surface.append.md)。

```
surface.append1-9,20-29
{
// 略（ふつうのsurfaceブレスと同様）
}
```

surface(.append)\*の\*部分に、サーフェスIDとなる数字を指定。複数指定、範囲指定が可能（[後述](caption_surfacebraceid.md)）。

なおそれ以外の各行の数字部分については各定義の説明参照。
