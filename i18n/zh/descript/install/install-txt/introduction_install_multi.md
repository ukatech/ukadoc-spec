# 同时安装

## 概要

SSP 可以在 ghost 或 shell 的归档中附带 balloon 等内容，并将它们一起安装。<br />
附带内容通过以「\*.」开头的条目指定，\*部分填写附带内容的种类。

\*中可填写以下5种类型。

- **balloon**: balloon
- **headline**: headline sensor
- **plugin**: plugin
- **calendar.skin**: 日历外观文件
- **calendar.plugin**: 日历的日程传感器

请注意，与 [type](type.md) 中的写法不同，日历相关项使用*点号分隔*（calendar.skin，而非 calendar skin）。

无论归档自身的 [type](type.md) 如何，都可以使用此功能；但实际使用时，通常用于 type 为*ghost*或*shell*的归档。

## 同时附带多个内容时的编号方式

同时附带多个相同种类的内容时，将 \*部分写成 balloon0、balloon1、……，在种类后添加从0开始的编号。（SSP 2.7.00及以后）

按*无编号→0→1→2…*的顺序查找，*遇到缺失的编号时即停止查找*。<br />
因此*不能跳过编号*。例如，只写 balloon0 和 balloon2 时，由于缺少 balloon1，查找会在此处停止，因此不会读取 balloon2。

无编号项和编号为0的项会被视为不同内容。如果同时写入 balloon 和 balloon0，就会安装两个 balloon。

[\*.directory](star-.directory.md)、[\*.source.directory](star-.source.directory.md)、[\*.refresh](star-.refresh.md)、[\*.refreshundeletemask](star-.refreshundeletemask.md)均可按各自编号单独指定。

另外，*只有第一个内容会被设置为与 ghost 或 shell 关联的 balloon*。<br />
第二个及之后的内容只会被安装，不会成为该 ghost 的默认 balloon。

## 記述例

在 ghost 中附带2个 balloon 和1个 plugin 的情况

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
balloon0.directory,example_balloon
balloon0.source.directory,balloon_normal
balloon1.directory,example_balloon_ex
balloon1.source.directory,balloon_special
plugin0.directory,example_plugin
```
