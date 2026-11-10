# icon.rect,始点X,始点Y,終点X,終点Y

**カテゴリ:** surface braces

Explicitly specifies the cropping rectangle for a face thumbnail (a reduced image cropped from the character's face, used in backlog/history windows, etc.).<br />
If specified, this takes precedence over automatic detection using the face/face or head/head hit regions (see [collision](collision-star.md)).

Unlike automatic face/head detection, the specified rectangle is used as-is; it is not enlarged to add margins.<br />
However, the output is square, so it is adjusted to a square based on the longer side of the specified rectangle and centered on the rectangle.

**既定値:** Unspecified (automatically detected from collision face/顔 or head/頭)

**対応:** SSP 2.8.52
