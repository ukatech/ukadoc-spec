# animation\*.pattern\*, drawing method, surface number, weight, X coordinate, Y coordinate (, options...)

**カテゴリ:** surface brace

Defines each animation frame. Normally, each frame is drawn by compositing it onto the base surface, resetting the preceding frame (strictly speaking, this depends on the drawing method).<br />
The \* following animation is the animationID (the same as the \* in animation\*.interval).<br />
The \* following pattern (pattern ID) is a sequential number starting at 0 within a series of animation\*.pattern definitions. In materia, the maximum is 127. Frames are drawn layered in ascending order of their numbers.<br />
For drawing methods, see [Drawing methods](h-drowmethod/index.md) below.<br />
The weight is the wait time *until* the frame is drawn. The unit is milliseconds. SSP alone also allows the format “minimum weight-maximum weight,” with the values separated by a hyphen; in that case, a value is selected at random from the range.<br />
The X and Y coordinates specify how far to offset the frame when displaying it relative to the base (the drawing result up to that frame).<br />
For the surface number, -1 stops the animation, and -2 stops all other animations currently running. In either case, the drawing method and X and Y coordinates are ignored.<br />
An alias other than the ID specified in the name definition can also be used as the surface number. (SSP 2.8.25～)<br />
[Legacy definition](caption_seriko-redefine.md): \*pattern\*, surface ID, weight, drawing method, X coordinate, Y coordinate

The options are as follows. To specify multiple options, continue listing them as in “animation0.pattern0,overlay,101,700,0,0,--alpha,128,--option2,...”.

- **--alpha,value(0-255)**: \[SSP 2.8.37～\]Specifies the opacity when drawing. 0 is fully transparent; 255 is fully opaque.<br />
  Example: animation0.pattern0,overlay,101,700,0,0,--alpha,128

**既定値:** No behavior

**対応:** Materia / SSP / CROW
