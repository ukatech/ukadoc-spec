# surface\*brace and surface.append\*brace

Definitions made with surface.append are added only to definitions that already exist (through a surface brace or the presence of suface\*.png).

Therefore, for example,

```
surface1,3
{
collision0,188,25,252,63,Head
collision1,180,191,220,222,Bust
}
```

if you then write the following intending it as an additional definition,

```
surface1-3
{
animation0.interval,sometimes
animation0.pattern0,overlay,101,100,168,67
animation0.pattern1,overlay,100,100,168,67
animation0.pattern2,overlay,101,100,168,67
animation0.pattern3,overlay,-1,100,168,67
}
```

an unintended “surface2” is *created*, and a definition is made.

For this reason, adding a definition with a range without using append can cause errors such as an “unexpected duplicate definition error.” However,

```
surface.append1-3
{
// 略
}
```

when written as above, the definitions added with append are applied only to the already-defined “surface1” and “surface3,” and the nonexistent “surface2” is not *created* internally either.

Note that, because of this relationship, the *surface brace* must *be written before the surface.append brace* in the definition file (such as surfaces.txt).
