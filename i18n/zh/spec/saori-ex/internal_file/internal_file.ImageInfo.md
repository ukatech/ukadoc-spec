# ImageInfo

**カテゴリ:** internal_file

Gets the dimensions of an image file **without loading the file** (by reading only its header). The dimensions can be read from the path alone, without creating a surface or similar.<br />
**Dimensions may not be available depending on the environment**. SSP first reads them using the OS property handler (the same mechanism used to display file details in Explorer); if that fails, SSP reads only the file header itself (without decoding the image). The formats whose dimensions can be obtained from the header are PNG (APNG) / JPEG / GIF / BMP / TIFF / WebP / ICO and CUR (largest entry) / PSD / XCF / PSP (version 4.0 and later) / QOI / PCX / TGA / PBM / PGM / PPM / PAM / PFM / XBM / XPM / MAG / PI. For ORA / KRA / CLIP (formats whose dimensions cannot be determined without decoding the contents), the result is empty if no OS handler is available. Failure to obtain dimensions is not an error.<br />
When reading from the header, the dimensions are for the first page for TIFF, the logical screen for GIF, and the largest entry for ICO and CUR. EXIF orientation (rotation) is not applied.<br />
Note that calling this synchronously stops the ghost while the file is being read. Reading can take time depending on where the file is located (such as on a network drive), so consider using [`--async`](../async.md).

Use [MediaInfo](internal_file.MediaInfo.md) to read audio/video tags and duration.

- **Argument1**: File path. Relative paths are based on the ghost's folder (ghost/master). Both `/` and `\` can be used as separators. Passing a relative path when calling without a ghost returns 400 (`ghost required`). If the file does not exist (including when the path refers to a folder), returns 400 (`file not found`). URLs are not accepted.
- **Argument2 and later**: Keys for the values to retrieve. At least one is required (if none are provided, returns 400 `invalid parameter`), with a maximum of 11 (12 or more returns 400 `invalid parameter`). Keys are case-insensitive.

The keys are as follows. Values are strings containing decimal integers.

- **width / height**: Image dimensions in pixels (px).

The response `Result` is `image` if the file is recognized as an image, or empty otherwise. If the file is not recognized as an image (including audio and video files), all `Value` fields are empty.<br />
`Value0` onward correspond in order to the keys listed from `Argument2` onward. Values that could not be obtained and unknown keys return an **empty string** (this is not an error; implementation-specific keys are not returned). Even for unreadable or unsupported formats, the response is 200 with all `Result` and `Value` fields empty, not 400.<br />
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
