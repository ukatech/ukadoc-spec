# icon.rect,start X,start Y,end X,end Y

**カテゴリ:** surface brace

Explicitly specifies the clipping rectangle for the face thumbnail (a reduced image cropped from the character's face, used in windows such as the backlog/speech history window).<br />
When specified, this takes precedence over automatic detection using the face or head hit region (see [collision](collision-star.md)).

Unlike automatic face/head detection, the specified rectangle is used as-is, without being enlarged to add margins.<br />
However, the output is square, so it is adjusted to a square based on the longer side of the specified rectangle and centered on the rectangle.

**既定値:** Unspecified (automatically detected from collision face/head)

**対応:** SSP 2.8.52
