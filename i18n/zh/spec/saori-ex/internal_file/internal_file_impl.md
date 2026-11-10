# 面向实现 MediaInfo 的 baseware 的说明

MediaInfo 的范围经过限制，使其他操作系统上的 baseware 也能轻松使用现有组件（ffprobe / libavformat、TagLib、操作系统标准媒体 API 等）实现。

- **必须遵守（MUST）**：上述键的名称、单位和形式；无法获取的值设为空字符串；值的格式处理（换行符替换为`0x01`、移除 NUL）；相对路径的基准（ghost/master）；响应形式（`Result` + `Value0..`）；规格中未定义的键设为空，不返回自定义键；接受路径分隔符`/`。
- **建议遵守（SHOULD）**：也接受路径分隔符`\`（ghost 作者会使用`\`书写，但在其他操作系统上`\`可能是普通文件名字符）。用` ;  `连接多个值的标签。
- **可因实现而异**：支持的格式（ICO、HEIC 等额外格式，能获取时支持即可，无法获取也不算故障）、原始标签字符编码的推测方式、VBR 时长的精度、`Result`的判定方法、不同格式能获取哪些项目。规格不规定各格式的标签映射方式（例如 ID3v2 的`TIT2`映射为`title`）。
- **符合性确认方式**：返回值时，值必须正确。没有返回值（为空）即为合格。`duration`允许有误差（参考值为±100 毫秒或 1%）。

使用 ffprobe / libavformat 实现时的参考：

- `duration`使用`format.duration`。`width` / `height`使用视频的图像流值。
- Ogg 和 Opus 标签位于`streams[].tags`，而不是`format.tags`。
- MP3 和 M4A 中嵌入的封面图像会作为带有`attached_pic`的视频流报告。如果将其计为视频，音频文件就会被判定为`video`。
- `track`（`3/12`形式）和`date`（`2024-05-06`形式）需要转换为规格中的`track`（仅曲目编号）和`year`（前 4 位数字）的形式。

## 实现 ImageInfo / IsMediaLoadable / IsImageLoadable 时

- **ImageInfo**遵守与 MediaInfo 相同的规则（键、单位、无法获取的值设为空字符串、路径处理）。只有获取到图像本身的像素数时，才将`Result`设为`image`；对于音频和视频文件，所有`Value`都设为空。
- **IsMediaLoadable / IsImageLoadable**的 4 个等级（`none` / `read` / `embed` / `write`）用于报告 baseware 自身的能力。`embed`表示“可以在 ghost 或 balloon 中嵌入并处理”（可以将其作为素材读入，例如 surface、balloon 图像、`\![sound]`音频等）；`write`表示“可以以该格式写出”。`read`是用于“可以读取，但不保证能嵌入并处理”的格式的等级；在 SSP 中，这指没有内置加载器、交由操作系统编解码器处理的格式。如果实现使用自有加载器读取素材，大多数可读取的格式都会属于`embed`，因此没有属于`read`的格式时，可以不返回`read`。后一级别包含前一级别。
- 不规定判定依据（文件头或扩展名）。文件不存在或路径指向文件夹时，返回 400（`file not found`）；其他情况不作为错误处理，无法读取时返回`none`。
