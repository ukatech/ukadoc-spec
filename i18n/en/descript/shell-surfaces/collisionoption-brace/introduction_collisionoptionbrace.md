# collisionoption brace example

```
sakura.collisionoption
{
nodrag0,Knob
nodrag1,Bust
nocontextmenu0,Bust
}
```

For the partner character, use kero.collisionoption or char\*.collisionoption.

This brace specifies collision names for which the baseware's default response to mouse operations is disabled.<br />
Because it looks up collisions by name, it applies to names assigned by collision, collisionex, or animation\*.collision. Settings apply per name, not per surface. To vary them by surface, use different names.

Do not overuse this feature, as it restricts user operations.<br />
For each specified collision, use mouseup\*, mousedown\*, mouserightdown\*, or similar settings in the cursor brace to specify a cursor that tells users the operation is unavailable.

**対応:** SSP 2.9.38
