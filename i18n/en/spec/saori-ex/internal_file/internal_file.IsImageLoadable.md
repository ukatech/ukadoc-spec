# IsImageLoadable

**カテゴリ:** internal_file

Checks how well SSP can handle an image file. Determines this from the header and extension without loading the file. This function lets a ghost check in advance whether an image can be used as a surface or balloon image, or whether it can be saved.<br />
The check uses the same component as the check for whether an image file can be opened in the built-in picture viewer when dragged and dropped onto SSP.

- **Argument1**: File path. Relative paths are based on the ghost folder (ghost/master). Both `/` and `\` can be used as separators. Passing a relative path in a call without a ghost returns 400 (`ghost required`). If the file does not exist (including if the path is a folder), returns 400 (`file not found`). URLs are not accepted.

The response's `Result` indicates the handling level and is one of the following.

- **none**: Cannot be read. The file is not an image or is in an unsupported format.
- **read**: Read-only. The format can be read, but it is not guaranteed to be processable as a ghost or balloon asset. In SSP, this applies to formats that the built-in loader cannot read but the OS image codec (WIC) can. These can be displayed in a viewer, but only the first frame is shown, and their use as surfaces, etc. is not guaranteed.
- **embed**: Can be processed as part of a ghost or balloon. The format can be used for surface or balloon images. In SSP, this applies to formats that the built-in loader can read.
- **write**: Can also be written. In addition to being embeddable, SSP can save images in this format (PNG / BMP / JPEG / WebP). Animated PNG and encrypted PNG are excluded.

Each subsequent level includes the previous levels (`write` also means `embed`). As with the actual loader, the check prioritizes the leading header, and checks the extension if the header is inconclusive. EXE / DLL files (used for extracting icons) are not counted as images.<br />
The level may vary depending on the SSP version and OS environment. More levels may be added in the future.

## 記述例

```
Argument0: IsImageLoadable
Argument1: image/bg01.png

→ 200
　Result: write
```

**対応:** SSP 2.9.27
