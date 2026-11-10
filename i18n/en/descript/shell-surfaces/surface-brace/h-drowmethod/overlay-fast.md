# overlay-fast

**カテゴリ:** surface brace \> Drawing Methods

Overlays the *new layer* according to the opacity of the *base layer*.<br />
In semitransparent areas of the *base layer*, the less opaque the area, the more strongly the *new layer* is composited; fully opaque areas are composited completely, and fully transparent areas are not composited at all.<br />
This is the counterpart to the [interpolate](interpolate.md) method.<br />
Can also be used in dressup and elements.<br />
The word "fast" in the name is historical; processing is not faster.

**対応:** SSP 2.8.36
