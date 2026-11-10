# blend-overlay

**カテゴリ:** surface brace \> Drawing method

*New layer* is composited over the image using overlay.<br />
This corresponds to the Overlay layer blend mode in image-editing software such as Photoshop.<br />
This is unrelated to the [overlay](overlay.md) method: dark areas use multiply, while light areas use screen blending.<br />
This can also be used with dressup and element.<br />
It is recommended to set [`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md) in the shell's descript.txt.

**対応:** SSP 2.8.36
