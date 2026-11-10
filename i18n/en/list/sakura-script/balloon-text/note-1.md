# Notes

## About `\_b[ファイルパス,...]`

Paths may be absolute or relative to the SHIORI module itself.

Note: SSP only; environment variables can also be used in paths such as file names.

- **When using base64**: Example: "data:image/png;base64,iV～II"
- **When using exe/dll resources**: Example: D:\\hogehoge.exe,20
- **When using exe/dll resources (specifying a resource ID)**: Example: D:\\hogehoge.exe,-10

## Options for `\_b[ファイルパス,...]`

Options that can be specified for both `\_b[ファイルパス,x,y,オプション,オプション...]` and `\_b[ファイルパス,inline,オプション,オプション...]`.

- **--option=opaque**: Display the image without making the top-left color transparent.
- **--option=use_self_alpha**: Display PNG images with an alpha channel as transparent.
- **--clipping=左 上 右 下**: Crop and display a rectangular portion of the image.<br />
  Specify the crop area as numeric values for left, top, right, and bottom.
- **--scaling=横 縦**: Scale the image to the specified size.<br />
  If a number is followed by %, it is treated as a percentage of the original image (after cropping with --clipping); if no unit is specified or it is followed by px, it is treated as a number of pixels.<br />
  If a number is negative, the image is flipped horizontally or vertically and displayed at the size of its absolute value.<br />
  If 0 is specified for either the width or height, the image is scaled to fit the non-zero dimension while preserving the original aspect ratio. (If the original image is 300x200, 150 0 produces the same result as 150x100.)\[SSP 2.8.82～\]<br />
  The size must be in the range of 1–4096px.<br />
  \[SSP 2.8.73～\]
- **--scaling=サイズ 基準辺**: Scale and display the image while preserving its original aspect ratio, so that the specified size is applied to the reference edge. The size must be given in pixels; % cannot be used.<br />
  Specify long (longer edge) or short (shorter edge) as the reference edge.<br />
  Adding max to the end of the reference edge scales down only (images smaller than the specified size are not enlarged); adding min scales up only (images larger than the specified size are not reduced).<br />
  If long or short is omitted and only max or min is specified, long is used.<br />
  If the size is negative, the image is flipped both horizontally and vertically and displayed at the size of its absolute value.<br />
  The size must be in the range of 1–4096px.<br />
  Example: --scaling=300 long makes an original image of 400x300 into 300x225.<br />
  Example: --scaling=300 longmax scales the image down to 300px only if its longer edge exceeds 300px.<br />
  \[SSP 2.8.82～\]
- **--option=fixed**: Keep the image stationary when scrolling.<br />
  Effective only when x,y are specified. It has no effect with inline, since the image is placed within the line.
- **--option=background**: Composite the image with the balloon's transparency taking precedence over the image's transparency.\[Standard behavior when unspecified\]<br />
  When x,y are specified, the image is displayed behind the text. This option lets you use the image as a background for text.
- **--option=foreground**: Composite the image with the image's transparency taking precedence over the balloon's transparency.\[SSP 2.6.54～\]<br />
  When x,y are specified, the image is displayed in front of the text.
- **--source=値**: Specify which item to use for rendering from an image or file with multiple rendering candidates.<br />
  For multipage TIFFs, specify the zero-based page number; for icons in DLL/EXE files, specify the zero-based resource number;<br />
  for PSD files and others, specify the layer name.<br />
  To specify a layer inside a layer group, write the group name separated by :: (nested groups are supported).<br />
  \[SSP 2.8.41～\]
