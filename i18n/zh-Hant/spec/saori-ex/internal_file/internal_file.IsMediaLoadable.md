# IsMediaLoadable

**カテゴリ:** internal_file

Checks whether SSP can handle an audio or video file. It determines this from the extension without loading the file.<br />
The check uses the same component as the check for whether an audio or video file can be opened in the built-in media player when dragged and dropped onto SSP (the set of extensions that OS DirectShow / Media Foundation may be able to play). Since the file contents are not examined, a `read` result does not guarantee that the file can actually be played.<br />
**Images are `none` in every format**. Images that can be read by SSP's built-in loader (including cases where they are identified as images from the file's leading header rather than just the extension), and images with extensions readable by OS WIC (such as HEIC), return `none` here even if their extensions are listed in OS DirectShow's extension table. In other words, images for which [IsImageLoadable](internal_file.IsImageLoadable.md) returns `embed` / `write`, and images that return `read` based on their extension, return `none` with this function. Use `IsImageLoadable` to check whether an image can be read.

- **Argument1**: File path. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. Passing a relative path when calling without a ghost returns 400 (`ghost required`). If the file does not exist (including folders), it returns 400 (`file not found`). URLs are not accepted.

The response `Result` is the handling level, one of the following.

- **none**: Cannot be read. The file is not audio or video (images always fall into this category), or is in an unsupported format.
- **read**: Read-only. A format that is likely to be playable.
- **embed**: Can be incorporated into a ghost and processed. **Not currently returned.**
- **write**: Can also be written. **Not currently returned.**

The same four-level terms as [IsImageLoadable](internal_file.IsImageLoadable.md) are used. Each higher level includes the previous level. Since `embed` and `write` may be returned in the future, it is safer to check whether the result is not `none` rather than whether it equals `read`.

## 記述例

```
Argument0: IsMediaLoadable
Argument1: sound/bgm01.mp3

→ 200
　Result: read
```

**対応:** SSP 2.9.27
