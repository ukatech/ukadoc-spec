# icon.rect,始点X,始点Y,終点X,終点Y

**カテゴリ:** surface brace

Explicitly specifies the clipping rectangle for the face thumbnail (a reduced image clipped from the character's face, used in places such as the backlog and speech history window).<br />
When specified, this takes precedence over automatic detection using the face/顔 or head/頭 hitboxes (see [collision](collision-star.md)).

Unlike automatic face/head detection, the specified rectangle is used as-is, without enlarging it to add margins.<br />
However, because the output is square, it is adjusted to a square based on the longer side of the specified rectangle, centered on the rectangle.

**既定値:** Unspecified (automatic detection from collision face/顔 or head/頭)

**対応:** SSP 2.8.52
