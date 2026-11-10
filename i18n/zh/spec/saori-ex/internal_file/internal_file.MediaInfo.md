# MediaInfo

**カテゴリ:** internal_file

获取音频和视频文件的标签、时长和尺寸，**无需加载文件**（无需准备播放，只读取标头和标签）。即使不通过 `\![sound]` 创建元素，也可以仅凭路径读取。`sound.*`列表中不会增加元素，不会触发`OnSound*`事件，也不会创建临时文件。\[SSP 2.9.27\] 图像尺寸请通过[ImageInfo](internal_file.ImageInfo.md)读取。将图像文件传给MediaInfo时的处理方式不作保证（SSP从\[SSP 2.9.25\]起仍会返回图像的`Result`、`width` / `height`）。<br />
**某些环境下可能无法获取**。\[SSP 2.9.32\] 对于MP3等文件的ID3（v1 / v2.2 / v2.3 / v2.4）、FLAC・Ogg Vorbis・Opus的注释，以及WAV・AVI的INFO标签，SSP会自行读取。对于其他格式（MP4・WMA・MKV / WebM等）以及SSP无法读取的项目，则依赖OS属性处理程序（与资源管理器中文件详细信息所用机制相同）读取。因此，如果OS没有对应格式的处理程序，或者处理程序未返回部分项目，这些值就会为空（无法与没有标签的文件区分）。未能获取不会导致错误。<br />
请注意，同步调用时，ghost会在读取期间停止。读取耗时可能因文件所在位置（例如网络驱动器）而异，因此也可以考虑使用[`--async`](../async.md)。

- **Argument1**: 文件路径。相对路径以ghost文件夹（ghost/master）为基准。分隔符可以使用`/`或`\`。在没有ghost的情况下调用并传入相对路径时，返回400（`ghost required`）。文件不存在（包括文件夹）时，返回400（`file not found`）。不接受URL。
- **Argument2以降**: 所需值的键。至少需要1个（未提供时返回400 `invalid parameter`），最多11个（12个以上时返回400 `invalid parameter`）。键不区分大小写。

键如下。所有值均为字符串（数值为十进制整数）。标签项目的名称和含义与`sound.(要素名).meta.*`相同。

- **title / artist / albumartist / album / genre / comment**: 字符串。
- **year**: 4位公历年份。原始值为完整日期时，取前4位。
- **track**: 仅曲目编号整数。不包含总数（`3/12`时为`3`）。
- **duration**: 音频或视频的时长（毫秒）。图像为空。VBR MP3等可能返回估算值。
- **width / height**: 像素数（px）。视频为影像尺寸。音频为空。仅包含嵌入式封面图等图像的视频不计为视频。

响应中的`Result`表示类型，为`audio`（音频）或`video`（视频）。无法判别时为空。\[SSP 2.9.32\] 对于OS不会返回类型的Ogg・Opus・WebM等格式，则根据文件内容判定（Matroska / WebM有影像轨道时为`video`，否则为`audio`）。类型仅供参考，因此即使`Result`为空，`Value`也可能有值。不要根据`Result`分支判断，而应根据`Value`是否为空来判断。今后可能会增加类型。<br />
`Value0`及之后的值，依次对应`Argument2`及之后列出的键。无法获取的值和未知键均返回**空字符串**（不会导致错误；不返回实现自定义的键）。对于无法读取或不支持的格式，不会返回400，而是以`Result`和`Value`全部为空的200响应。

- 值中的换行会替换为字节值`0x01`（CRLF也替换为单个`0x01`。仅LF或仅CR也各自替换为单个`0x01`）。NUL会被移除。
- 对于包含多个值的标签（例如多个艺术家），将其合并为一个字符串，以` ;  `（分号和半角空格）连接。
- 响应的字符编码遵循请求中的`Charset`。
- \[SSP 2.9.32\] 对于SSP自行读取的标签中未指定字符编码的项目（ID3v1、ID3v2的ISO-8859-1、WAV・AVI的INFO），SSP会按UTF-8 → Shift_JIS → OS默认字符编码的顺序进行推测。由于这是推测，在非日语OS上尤其可能混淆西欧语言和日语。对于SSP不自行读取格式的标签，字符编码推测由OS处理，可能出现乱码。
- 不同OS环境下可获取的格式和项目有所不同。根据在SSP上的测试，在Windows 11的标准环境中，MKV / WebM的大多数标签和影像尺寸等都无法获取（从\[SSP 2.9.32\]起，WAV标签和MP3注释由SSP自行读取，因此可以获取）。

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
