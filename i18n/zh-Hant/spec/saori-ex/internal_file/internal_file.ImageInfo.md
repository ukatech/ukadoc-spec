# ImageInfo

**カテゴリ:** internal_file

Gets the dimensions of an image file **without loading the file** (by reading only its header). The file can be read using only its path, without creating a surface or similar object.<br />
**The information may not be available depending on the environment**. SSP first reads it using the OS property handler (the same mechanism used to display file details in Explorer). If that fails, SSP reads only the file header itself (without decoding the image). Header reading can retrieve dimensions for PNG (APNG) / JPEG / GIF / BMP / TIFF / WebP / ICO・CUR (largest entry) / PSD / XCF / PSP (version 4.0 and later) / QOI / PCX / TGA / PBM・PGM・PPM・PAM・PFM / XBM / XPM / MAG / PI. For ORA / KRA / CLIP (formats whose dimensions cannot be determined without extracting the contents), the result is empty if no OS handler is available. Failure to retrieve the information is not an error.<br />
When reading from the header, the dimensions are for the first page for TIFF, the logical screen for GIF, and the largest entry for ICO・CUR. EXIF orientation (rotation) is not applied.<br />
Note that a synchronous call stops the ghost while reading. Reading may take time depending on where the file is stored (such as a network drive), so consider using [`--async`](../async.md).

Audio and video tags and durations can be read with [MediaInfo](internal_file.MediaInfo.md).

- **Argument1**: File path. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. If a relative path is passed when called without a ghost, the result is 400 (`ghost required`). If the file does not exist (including if it is a folder), the result is 400 (`file not found`). URLs are not accepted.
- **Argument2 onward**: Keys for the desired values. At least one is required (if none are provided, the result is 400 `invalid parameter`), and up to 11 are allowed (12 or more result in 400 `invalid parameter`). Keys are case-insensitive.

The keys are as follows. Values are decimal integer strings.

- **width / height**: Image dimensions in pixels (px).

The response `Result` is `image` if the file is recognized as an image, or empty otherwise. If it is not recognized as an image (including audio and video files), all `Value` fields are empty.<br />
`Value0` onward correspond in order to the keys listed from `Argument2` onward. Values that could not be retrieved and unknown keys return an **empty string** (this is not an error; implementation-specific keys are not returned). Unreadable or unsupported formats do not result in 400; instead, the response is 200 with `Result` and all `Value` fields empty.<br />
The response character encoding follows the request's `Charset`.

## 記述例

```
Argument0: ImageInfo
Argument1: image/bg01.png
Argument2: width
Argument3: height

→ 200
　Result: image
　Value0: 640
　Value1: 480
```

**対応:** SSP 2.9.27
