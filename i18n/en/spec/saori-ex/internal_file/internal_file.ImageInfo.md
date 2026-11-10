# ImageInfo

**カテゴリ:** internal_file

Gets the dimensions of an image file **without loading the file** (by reading only its header). The image can be read from its path alone, without creating a surface or anything similar.<br />
**The information may not be available in some environments**. SSP first reads it using the OS property handler (the same mechanism used for file details in Explorer); if that fails, SSP reads only the file header itself (without decoding the image). The formats whose dimensions can be read from the header are PNG (APNG) / JPEG / GIF / BMP / TIFF / WebP / ICO and CUR (largest entry) / PSD / XCF / PSP (version 4.0 and later) / QOI / PCX / TGA / PBM / PGM / PPM / PAM / PFM / XBM / XPM / MAG / PI. For ORA / KRA / CLIP (formats whose dimensions can only be determined by decompressing the contents), the result is empty if no OS handler is available. Failure to retrieve the information is not an error.<br />
When reading from the header, the dimensions are for the first page of TIFF files, the logical screen of GIF files, and the largest entry of ICO and CUR files. EXIF orientation (rotation) is not applied.<br />
Note that calling this synchronously stops the ghost while the file is being read. Reading can take time depending on where the file is stored (for example, on a network drive), so consider using [`--async`](../async.md) as well.

Use [MediaInfo](internal_file.MediaInfo.md) to read audio and video tags and durations.

- **Argument1**: File path. Relative paths are based on the ghost folder (ghost/master). Both `/` and `\` can be used as separators. If a relative path is passed in a call without a ghost, the result is 400 (`ghost required`). If the file does not exist (including if the path is a folder), the result is 400 (`file not found`). URLs are not accepted.
- **Argument2 onward**: Keys for the values to retrieve. At least one is required (if none are specified, the result is 400 `invalid parameter`), and up to 11 can be specified (12 or more results in 400 `invalid parameter`). Keys are case-insensitive.

The keys are as follows. Values are decimal integer strings.

- **width / height**: Image dimensions in pixels (px).

The response `Result` is `image` if the file is identified as an image, or empty otherwise. If it cannot be identified as an image (including audio and video files), all `Value` fields are empty.<br />
`Value0` onward correspond in order to the keys listed from `Argument2` onward. Values that could not be retrieved and unknown keys return an **empty string** (this is not an error; implementation-specific keys are not returned). Unsupported or unreadable formats do not result in 400; instead, 200 is returned with both `Result` and all `Value` fields empty.<br />
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
