# surface brace examples

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

There is a notation called surace.append for specifying additional definitions in SSP only (appending definitions to those that have already been defined).<br />
For details, see [below](caption_surface.append.md).

```
surface.append1-9,20-29
{
// 略（ふつうのsurfaceブレスと同様）
}
```

In the \* part of surface(.append)\*, specify the number that serves as the surface ID. Multiple values and ranges can be specified ([see below](caption_surfacebraceid.md)).

For the numeric parts of all other lines, see the descriptions of the respective definitions.
