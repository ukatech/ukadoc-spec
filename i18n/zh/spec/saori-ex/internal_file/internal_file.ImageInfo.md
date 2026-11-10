# ImageInfo

**カテゴリ:** internal_file

**无需加载文件**（只读取文件头）即可获取图像文件的尺寸。无需创建 surface 等对象，只需提供路径即可读取。<br />
**根据环境不同，可能无法获取信息**。SSP 首先通过操作系统的属性处理程序读取（与资源管理器文件详细信息中使用的机制相同）；如果无法获取，则由 SSP 自身仅读取文件头获取（不解码图像）。可从文件头读取的格式有：PNG（APNG）/ JPEG / GIF / BMP / TIFF / WebP / ICO・CUR（最大条目）/ PSD / XCF / PSP（4.0 及更高版本）/ QOI / PCX / TGA / PBM・PGM・PPM・PAM・PFM / XBM / XPM / MAG / PI。对于 ORA / KRA / CLIP 等必须解压内容才能识别的格式，如果没有操作系统处理程序，结果会为空。无法获取信息不会被视为错误。<br />
从文件头读取尺寸时，TIFF 使用第一页的尺寸，GIF 使用逻辑屏幕尺寸，ICO・CUR 使用最大条目的尺寸。不考虑 EXIF 方向（旋转）。<br />
请注意，同步调用时，ghost 会在读取期间停止。读取可能会因文件存放位置（例如网络驱动器）而耗时，因此也可以考虑使用 [`--async`](../async.md)。

音频和视频的标签或时长请使用 [MediaInfo](internal_file.MediaInfo.md) 读取。

- **Argument1**: 文件路径。相对路径以 ghost 文件夹（ghost/master）为基准。分隔符可以使用 `/` 或 `\`。不带 ghost 调用时传入相对路径会返回 400（`ghost required`）。文件不存在（包括路径指向文件夹）时返回 400（`file not found`）。不接受 URL。
- **Argument2 及之后**: 所需值的键。至少需要 1 个（没有键时返回 400 `invalid parameter`），最多 11 个（12 个及以上时返回 400 `invalid parameter`）。键不区分大小写。

键如下。值为十进制整数的字符串。

- **width / height**: 图像的像素数（px）。

响应中的 `Result` 为 `image`（识别为图像时）或空。无法识别为图像时（包括音频、视频文件），所有 `Value` 均为空。<br />
从 `Value0` 开始，依次对应 `Argument2` 及之后列出的键。无法获取的值和未知键会返回**空字符串**（不会报错，也不会返回实现自定义的键）。对于无法读取或不支持的格式，不会返回 400，而是以 200 返回，且 `Result` 和所有 `Value` 均为空。<br />
响应的字符编码遵循请求的 `Charset`。

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
