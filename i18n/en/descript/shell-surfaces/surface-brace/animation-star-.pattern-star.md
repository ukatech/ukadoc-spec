# animation\*.pattern\*, drawing method, surface number, weight, X coordinate, Y coordinate (, options...)

**カテゴリ:** surface brace

Defines each frame of an animation. Normally, each frame is drawn by compositing it onto the base surface, resetting any previous frames first (strictly speaking, this depends on the drawing method).<br />
The \* following animation is the animationID (the same as the \* in animation\*.interval).<br />
The \* following pattern (the pattern ID) is a sequential number starting at 0 within a series of animation\*.pattern definitions. In materia, the maximum is 127. Frames are drawn stacked in order from the lowest number.<br />
For drawing methods, see [Drawing Methods](h-drowmethod/index.md) below.<br />
The weight is the delay *before* drawing that frame. The unit is milliseconds. SSP also supports a format with the minimum and maximum weights separated by a hyphen (“minimum-maximum”); in this case, a value is selected at random from that range.<br />
The X and Y coordinates specify how far to shift the frame relative to the base (the drawing result up to that frame).<br />
Setting the surface number to -1 stops that animation; setting it to -2 stops all other animations currently running. In either case, the drawing method and X and Y coordinates are ignored.<br />
An alias other than the ID specified in the name definition can also be used as the surface number. (SSP 2.8.25～)<br />
[Old definition](caption_seriko-redefine.md): \*pattern\*, surface ID, weight, drawing method, X coordinate, Y coordinate

The available options are as follows. To specify multiple options, append them as shown here: “animation0.pattern0,overlay,101,700,0,0,--alpha,128,--option2,...”.

- **--alpha,value (0-255)**: \[SSP 2.8.37～\]Specifies the opacity when drawing. 0 is fully transparent; 255 is fully opaque.<br />
  Example: animation0.pattern0,overlay,101,700,0,0,--alpha,128

**既定値:** No behavior

**対応:** Materia / SSP / CROW
