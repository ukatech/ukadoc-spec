# collisionoption brace example

```
sakura.collisionoption
{
nodrag0,Knob
nodrag1,Bust
nocontextmenu0,Bust
}
```

The settings for the other characters are kero.collisionoption and char\*.collisionoption.

This brace specifies options that suppress the baseware's default response to mouse operations on named collision regions.<br />
Because regions are matched by name, the options apply to names assigned by collision, collisionex, or animation\*.collision. Options apply per name, not per surface. Use different names to vary the behavior by surface.

Do not overuse these options, as they restrict user operations.<br />
For each specified collision region, use mouseup\*, mousedown\*, mouserightdown\*, or similar entries in the cursor brace to specify a cursor that tells the user the operation is unavailable.

**対応:** SSP 2.9.38
