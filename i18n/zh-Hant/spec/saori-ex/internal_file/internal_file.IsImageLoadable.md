# IsImageLoadable

**カテゴリ:** internal_file

Checks how far SSP can handle an image file. It determines this from the header and extension without loading the file. This function lets a ghost check in advance whether a file can be used as a surface or balloon image, or saved.<br />
The check uses the same component as the check for whether an image file can be opened in the built-in picture viewer when dragged and dropped onto SSP.

- **Argument1**: File path. Relative paths are based on the ghost's folder (ghost/master). Either `/` or `\` can be used as a separator. Passing a relative path when calling without a ghost returns 400 (`ghost required`). If the file does not exist (including folders), it returns 400 (`file not found`). URLs are not accepted.

The response's `Result` indicates the level of support, and is one of the following.

- **none**: Cannot be read. The file is not an image or is in an unsupported format.
- **read**: Read only. The format can be read, but there is no guarantee that it can be incorporated and processed as a ghost or balloon asset. In SSP, this applies to formats that the built-in loader cannot read but the OS image codec (WIC) can. They can be displayed in a viewer or similar, but only the first frame is shown, and there is no guarantee they can be used as surfaces or similar.
- **embed**: Can be incorporated into a ghost or balloon and processed. The format can be used as a surface or balloon image. In SSP, this applies to formats that the built-in loader can read.
- **write**: Writing is also possible. In addition to embed, SSP can save images in this format (PNG / BMP / JPEG / WebP). Animated PNG and encrypted PNG are not included.

Each higher level includes the preceding level (`write` also means `embed`). As with the actual loader, the check prioritizes the header and checks the extension if the header is inconclusive. EXE / DLL files (used for extracting icons) are not counted as images.<br />
The level may vary depending on the SSP version and OS environment. Additional levels may be added in the future.

## 記述例

```
Argument0: IsImageLoadable
Argument1: image/bg01.png

→ 200
　Result: write
```

**対応:** SSP 2.9.27
