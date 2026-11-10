# MediaInfo

**カテゴリ:** internal_file

Gets the tags, duration, and dimensions of an audio or video file **without loading the file** (without preparing it for playback, reading only its header and tags). The file can be read using only its path, without creating an element with `\![sound]`. No elements are added to the `sound.*` list, no `OnSound*` events are fired, and no temporary files are created. \[SSP 2.9.27\] Read image dimensions with [ImageInfo](internal_file.ImageInfo.md). Handling of image files passed to MediaInfo is not guaranteed (as of \[SSP 2.9.25\], SSP still returns the image's `Result` and `width` / `height`).<br />
**Some values may not be available depending on the environment**. \[SSP 2.9.32\] SSP reads ID3 (v1 / v2.2 / v2.3 / v2.4) tags for MP3 and other formats, comments for FLAC, Ogg Vorbis, and Opus, and INFO tags for WAV and AVI itself. For other formats (MP4, WMA, MKV / WebM, etc.) and items SSP could not read, it relies on the OS property handler (the same mechanism that displays file details in Explorer). As a result, values are empty for formats without a handler on the OS, or for which the handler does not return some items (these cannot be distinguished from files without tags). Failure to retrieve a value does not result in an error.<br />
Note that when called synchronously, the ghost stops while the data is being read. Reading may take time depending on where the file is stored (such as on a network drive), so consider using [`--async`](../async.md).

- **Argument1**: File path. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. Passing a relative path when calling without a ghost returns 400 (`ghost required`). If the file does not exist (including folders), it returns 400 (`file not found`). URLs are not accepted.
- **Argument2 and later**: Keys for the values to retrieve. At least one is required (if none are provided, returns 400 `invalid parameter`), and up to 11 are allowed (12 or more returns 400 `invalid parameter`). Keys are case-insensitive.

The keys are as follows. All values are strings (numbers are decimal integers). Tag items have the same names and meanings as `sound.(要素名).meta.*`.

- **title / artist / albumartist / album / genre / comment**: String.
- **year**: Four-digit Gregorian year. If the original value is a full date, the first four digits are used.
- **track**: Track number only, as an integer. The total number is not included (`3/12` becomes `3`).
- **duration**: Audio or video duration (milliseconds). Empty for images. May be an estimated value for VBR MP3 and other formats.
- **width / height**: Dimensions in pixels (px). For video, these are the video dimensions. Empty for audio. Video consisting only of embedded cover art, such as album art, is not counted as video.

The response `Result` indicates the type: either `audio` or `video`. It is empty if the type cannot be determined. \[SSP 2.9.32\] Even for Ogg, Opus, WebM, and other formats for which the OS does not return a type, it is determined from the file contents (Matroska / WebM is `video` if it has a video track, and `audio` otherwise). The type is only a guide, so `Value` may be populated even when `Result` is empty. Do not branch on `Result`; check whether `Value` is empty. More types may be added in the future.<br />
`Value0` and later correspond in order to the keys listed in `Argument2` and later. Values that could not be retrieved and unknown keys return an **empty string** (this is not an error; implementation-specific keys are not returned). Unsupported or unreadable formats do not return 400; they return 200 with `Result` and all `Value` fields empty.

- Line breaks within values are replaced with the byte value `0x01` (CRLF is replaced with one `0x01`; LF-only and CR-only are each replaced with one `0x01`). NUL bytes are removed.
- Tags with multiple values (such as multiple artists) are combined into a single string joined with ` ;  ` (a semicolon and half-width spaces).
- The response character encoding follows the request's `Charset`.
- \[SSP 2.9.32\] Among tags read by SSP itself, for those without a specified character encoding (ID3v1, ISO-8859-1 in ID3v2, and INFO in WAV / AVI), SSP tries to determine the encoding in this order: UTF-8 → Shift_JIS → the OS's default character encoding. Since this is an estimate, Western European and Japanese text may be misidentified, especially on non-Japanese OSes. The OS determines the encoding for tags in formats SSP does not read itself, so text may be garbled.
- Which items can be retrieved for each format varies by OS environment. In tests with SSP, most tags and video dimensions in MKV / WebM could not be retrieved in the standard Windows 11 environment (as of \[SSP 2.9.32\], SSP reads WAV tags and MP3 comments itself, so those can be retrieved).

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
