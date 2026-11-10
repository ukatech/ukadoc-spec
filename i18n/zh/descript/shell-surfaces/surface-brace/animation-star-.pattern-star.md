# animation\*.pattern\*, drawing method, surface number, weight, X coordinate, Y coordinate (, options...)

**カテゴリ:** surface brace

Defines each frame of an animation. Normally, each frame is drawn by compositing it onto the base surface, resetting the previous frame (strictly speaking, this depends on the drawing method).<br />
The \* following animation is the animationID (the same as the \* in animation\*.interval).<br />
The \* following pattern (the pattern ID) is a sequential number starting from 0 within a set of animation\*.pattern definitions. In materia, the maximum is 127. Frames are drawn layered in ascending order of their numbers.<br />
See [drawing methods](h-drowmethod/index.md) below for drawing methods.<br />
Weight is the delay *before* drawing that frame. The unit is milliseconds. SSP alone also allows the format “minimum weight-maximum weight,” separated by a hyphen; in that case, a value is chosen at random from the range.<br />
The X and Y coordinates specify how far to offset the frame relative to the base (the drawing result up to that frame).<br />
Setting the surface number to -1 stops that animation; setting it to -2 stops all other animations currently running. In either case, the drawing method and X and Y coordinates are ignored.<br />
You can also specify aliases other than the IDs specified in the name definition as the surface number. (SSP 2.8.25～)<br />
[Legacy definition](caption_seriko-redefine.md): \*pattern\*, surface ID, weight, drawing method, X coordinate, Y coordinate

Options are as follows. To specify multiple options, continue writing them as in “animation0.pattern0,overlay,101,700,0,0,--alpha,128,--option2,...”.

- **--alpha,value(0-255)**: \[SSP 2.8.37～\] Specifies opacity when drawing. 0 is fully transparent; 255 is fully opaque.<br />
  Example: animation0.pattern0,overlay,101,700,0,0,--alpha,128

**既定値:** No effect

**対応:** Materia / SSP / CROW
