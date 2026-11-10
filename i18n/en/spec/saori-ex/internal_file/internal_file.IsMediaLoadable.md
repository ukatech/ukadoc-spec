# IsMediaLoadable

**カテゴリ:** internal_file

Checks whether SSP can handle an audio or video file. Determines this from the extension without loading the file.<br />
The check uses the same component as the check for whether an audio or video file can be opened in the built-in media player when dragged and dropped onto SSP (the set of extensions that OS DirectShow / Media Foundation may be able to play). Since the file contents are not checked, a file may not actually be playable even if the result is `read`.<br />
**Images always return `none`, regardless of format.** Images readable by SSP's built-in loader (including those identified as images by the header at the start of the file, not just by their extension) and images with extensions readable by OS WIC (such as HEIC) return `none` here, even if their extensions appear in the OS DirectShow extension table. In other words, images for which [IsImageLoadable](internal_file.IsImageLoadable.md) returns `embed` / `write`, and images that return `read` based on their extension, return `none` from this function. Use `IsImageLoadable` to check whether an image can be read.

- **Argument1**: File path. Relative paths are based on the ghost folder (ghost/master). Both `/` and `\` can be used as separators. Passing a relative path in a call without a ghost returns 400 (`ghost required`). If the file does not exist (including if the path is a folder), returns 400 (`file not found`). URLs are not accepted.

The response's `Result` indicates the handling level and is one of the following.

- **none**: Cannot be read. The file is not audio or video (images always return this), or is in an unsupported format.
- **read**: Read-only. The format is likely to be playable.
- **embed**: Can be processed as part of a ghost. **This is not currently returned.**
- **write**: Can also be written. **This is not currently returned.**

The same four levels as [IsImageLoadable](internal_file.IsImageLoadable.md) are used. Each subsequent level includes the previous levels. Since `embed` and `write` may be returned in the future, it is safer to check whether the result is not `none` rather than whether it equals `read`.

## 記述例

```
Argument0: IsMediaLoadable
Argument1: sound/bgm01.mp3

→ 200
　Result: read
```

**対応:** SSP 2.9.27
