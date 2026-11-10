# MediaInfo

**カテゴリ:** internal_file

Gets the tags, duration, and dimensions of an audio or video file **without loading the file** (without preparing to play it; only the header and tags are read). The values can be read using only the path, without creating an element with `\![sound]`. No elements are added to the `sound.*` list, no `OnSound*` events are fired, and no temporary files are created. \[SSP 2.9.27\] Read image dimensions with [ImageInfo](internal_file.ImageInfo.md). Handling of image files passed to MediaInfo is not guaranteed (as of \[SSP 2.9.25\], SSP still returns the image's `Result` and `width` / `height`).<br />
**Values may not be available depending on the environment**. \[SSP 2.9.32\] SSP reads MP3 and other ID3 tags (v1 / v2.2 / v2.3 / v2.4), FLAC, Ogg Vorbis, and Opus comments, and WAV / AVI INFO tags itself. For other formats (such as MP4, WMA, and MKV / WebM) and items SSP could not read, it relies on the OS property handler (the same mechanism used to show file details in Explorer). Therefore, values are empty if the OS has no handler for the format, or if the handler does not return certain items (these cases cannot be distinguished from a file without tags). Failure to retrieve a value does not result in an error.<br />
Note that a synchronous call pauses the ghost while reading. Reading may take time depending on where the file is stored (such as on a network drive), so consider using [`--async`](../async.md).

- **Argument1**: File path. Relative paths are based on the ghost folder (ghost/master). Both `/` and `\` can be used as separators. Passing a relative path in a call without a ghost returns 400 (`ghost required`). If the file does not exist (including if the path is a folder), returns 400 (`file not found`). URLs are not accepted.
- **Argument2 and later**: Keys for the values to retrieve. At least one key is required (if none are specified, returns 400 `invalid parameter`), and up to 11 keys are allowed (12 or more returns 400 `invalid parameter`). Keys are case-insensitive.

The keys are as follows. All values are strings (numeric values are decimal integers). Tag items have the same names and meanings as `sound.(element name).meta.*`.

- **title / artist / albumartist / album / genre / comment**: String.
- **year**: Four-digit Gregorian year. If the original value is a full date, the first four digits are used.
- **track**: Integer track number only. Does not include the total number (`3/12` becomes `3`).
- **duration**: Audio or video duration (milliseconds). Empty for images. May be an estimate for VBR MP3 and similar formats.
- **width / height**: Dimensions in pixels (px). For video, the video dimensions. Empty for audio. Video consisting only of embedded artwork, such as album art, is not counted as video.

The response's `Result` indicates the media type and is either `audio` or `video`. It is empty if the type cannot be determined. \[SSP 2.9.32\] The type is also determined from the file contents for Ogg, Opus, WebM, and other formats where the OS does not return a type (Matroska / WebM is `video` if it has a video track, and `audio` otherwise). The type is only a guide, so `Value` may still be populated when `Result` is empty. Do not branch on `Result`; check whether `Value` is empty. More types may be added in the future.<br />
`Value0` and later correspond in order to the keys listed in `Argument2` and later. Values that could not be retrieved and unknown keys return an **empty string** (this is not an error; implementation-specific keys are not returned). Unreadable or unsupported formats do not return 400; instead, they return 200 with both `Result` and all `Value` fields empty.

- Newlines in values are replaced with byte value `0x01` (CRLF is replaced with a single `0x01`; LF and CR alone are each also replaced with a single `0x01`). NUL characters are removed.
- Tags with multiple values (such as multiple artists) are joined into a single string with ` ;  ` (a semicolon and two half-width spaces).
- The response character encoding follows the request's `Charset`.
- \[SSP 2.9.32\] For tags that SSP reads itself and that do not specify a character encoding (ID3v1, ISO-8859-1 in ID3v2, and WAV / AVI INFO), SSP tries to determine the encoding in this order: UTF-8 → Shift_JIS → the OS default character encoding. Since this is an estimate, Western European text may be mistaken for Japanese, especially on non-Japanese OSes. Character encoding detection for tags in formats SSP does not read itself is left to the OS, and may result in garbled text.
- Which items can be retrieved for each format varies by OS environment. In testing with SSP, most tags and video dimensions in MKV / WebM could not be retrieved in the standard Windows 11 environment (as of \[SSP 2.9.32\], SSP reads WAV tags and MP3 comments itself, so these can be retrieved).

## 記述例

```
Argument0: MediaInfo
Argument1: sound/bgm01.mp3
Argument2: title
Argument3: artist
Argument4: duration
Argument5: --async=OnMediaInfo

→ 204（結果はOnMediaInfoイベントで届く）
　Reference0: OnMediaInfo
　Reference1: audio
　Reference2: internal_file
　Reference3: MediaInfo
　Reference4: タイトル
　Reference5: アーティスト
　Reference6: 215000
```

**対応:** SSP 2.9.25
