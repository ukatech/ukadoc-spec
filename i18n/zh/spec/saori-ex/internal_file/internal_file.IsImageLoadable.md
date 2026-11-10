# IsImageLoadable

**カテゴリ:** internal_file

检查 SSP 能够处理到什么程度的图像文件。不会加载文件，而是根据文件头和扩展名进行判断。供 ghost 事先确认图像能否用作 surface 或 balloon 图像、能否保存。<br />
判断时使用的组件，与将图像文件拖放到 SSP 上时，判断能否用内置图片查看器打开该文件的组件相同。

- **Argument1**: 文件路径。相对路径以 ghost 的文件夹（ghost/master）为基准。分隔符可以写作`/`或`\`。在没有 ghost 的情况下调用并传入相对路径时，返回 400（`ghost required`）。文件不存在（包括路径指向文件夹）时，返回 400（`file not found`）。不接受 URL。

响应中的`Result`表示处理级别，为以下值之一。

- **none**: 无法读取。不是图像，或格式不受支持。
- **read**: 仅可读取。不能保证能将其作为 ghost 或 balloon 素材进行处理，但可以读取。SSP 中，内置加载器无法读取、但 OS 图像编解码器（WIC）能够读取的格式属于此级别。可以在查看器等程序中显示，但仅显示第一帧，且不保证能用作 surface 等。
- **embed**: 可以集成到 ghost 或 balloon 中进行处理。可用作 surface 或 balloon 图像的格式。在 SSP 中，内置加载器能够读取的格式属于此级别。
- **write**: 也可以写入。除了满足 embed 的条件外，SSP 还能够以该格式保存图像（PNG / BMP / JPEG / WebP）。不包括动画 PNG 和加密 PNG。

后面的级别包含前面的级别（例如，`write`也属于`embed`）。判断时与实际加载器相同，优先检查文件头；如果无法从文件头判断，则检查扩展名。EXE / DLL（用于提取图标）不视为图像。<br />
所属级别可能因 SSP 版本或 OS 环境而异。将来可能会增加级别。

## 記述例

```
Argument0: IsImageLoadable
Argument1: image/bg01.png

→ 200
　Result: write
```

**対応:** SSP 2.9.27
