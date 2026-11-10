# IsMediaLoadable

**カテゴリ:** internal_file

检查 SSP 能否处理音频或视频文件。不会加载文件，而是根据扩展名进行判断。<br />
判断时使用的组件，与将音频或视频文件拖放到 SSP 上时，判断能否用内置媒体播放器打开该文件的组件相同（即 OS 的 DirectShow / Media Foundation 可能播放的扩展名集合）。由于不会检查文件内容，即使结果为`read`，也不一定能实际播放。<br />
**所有格式的图像都会返回`none`**。即使 OS 的 DirectShow 扩展名表中列有某种图像扩展名，在此函数中也会返回`none`。这包括 SSP 内置加载器能够读取的图像（不仅是根据扩展名识别的图像，也包括根据文件开头的文件头识别为图像的情况），以及 OS 的 WIC（例如 HEIC）能够读取的扩展名对应的图像。也就是说，[IsImageLoadable](internal_file.IsImageLoadable.md)返回`embed` / `write`的图像，以及根据扩展名返回`read`的图像，在此函数中都会返回`none`。要检查图像能否读取，请使用`IsImageLoadable`。

- **Argument1**: 文件路径。相对路径以 ghost 的文件夹（ghost/master）为基准。分隔符可以写作`/`或`\`。在没有 ghost 的情况下调用并传入相对路径时，返回 400（`ghost required`）。文件不存在（包括路径指向文件夹）时，返回 400（`file not found`）。不接受 URL。

响应中的`Result`表示处理级别，为以下值之一。

- **none**: 无法读取。不是音频或视频（图像必定属于此级别），或格式不受支持。
- **read**: 仅可读取。预期能够播放的格式。
- **embed**: 可以集成到 ghost 中进行处理。**目前不会返回此值。**
- **write**: 也可以写入。**目前不会返回此值。**

使用与[IsImageLoadable](internal_file.IsImageLoadable.md)相同的四级术语。后面的级别包含前面的级别。将来可能会开始返回`embed`和`write`，因此最好根据是否为`none`来判断，而不要判断是否等于`read`。

## 記述例

```
Argument0: IsMediaLoadable
Argument1: sound/bgm01.mp3

→ 200
　Result: read
```

**対応:** SSP 2.9.27
