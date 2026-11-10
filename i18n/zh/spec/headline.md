# HEADLINE/2.0

最終変更：2013-08-07

参考：[HEADLINE/1.1](http://usada.sakura.vg/contents/headlinesenser.html)（外部サイト）

## 前言

HEADLINE/2.0是旧版规范（1.1）的修订版。目前仅 SSP 实现。

主要变更是新增字符编码指定。

## headline sensor 的组成

需要设置文件「descript.txt」和导出 execute 函数的 dll 文件。

## DLL

请参阅[DLL 页面](dll.md)。

## request - response 1：获取 version

### request 示例

```
GET Version HEADLINE/2.0
Charset: UTF-8
Sender: SSP
```

### request 头详细说明

- **Charset**: 字符编码
- **Sender**: 事件发送方

### response 示例

```
HEADLINE/2.0 200 OK
Charset: UTF-8
Value: HeadlineModule 1.1
```

### response 头详细说明

- **Charset**: \[可省略\]字符编码。省略时使用调用方指定的编码。
- **Value**: \[可省略\]版本字符串

## request - response 2：获取 headline

### request 示例

```
GET Headline HEADLINE/2.0
Charset: UTF-8
Sender: SSP
Option: url
Path: C:\SSP\temp\ad9326dc37cb86a9.html
```

### request 头详细说明

- **Charset**: 字符编码
- **Sender**: 事件发送方
- **Option**: \[可省略\]可在响应中解析的选项。以逗号分隔列出。<br />
  目前仅支持 url。请参阅 response 的 Headline 头一节。
- **Path**: headline 解析目标文件的路径（完整路径）。

### response 示例

```
HEADLINE/2.0 200 OK
Charset: UTF-8
Headline: ほげほげ1
Headline: ほげほげ2
Headline: ほげほげ3
Headline: ほげほげ4
Headline: ほげほげ5
```

### response 头详细说明

- **Charset**: \[可省略\]字符编码。省略时使用调用方指定的编码。
- **RequestCharset**: \[可省略\]下次调用时所需的字符编码。省略时使用 Charset。
- **Headline**: headline 的内容。<br />
  调用时若在 Option 头中传入 url，例如 Option: url，则支持 URL 扩展。<br />
  此时以字节值 1 为分隔符，按「内容\[1\]URL」的格式响应，便会同时将 URL 通知 ghost；如果 ghost 支持，点击条目后可能可以跳转到相应详情等。<br />
  此外，返回的不是 Sakura Script 片段，不能使用标签。返回的是纯文本。

## descript.txt

请参阅[Headline 设置页面](../descript/headline/index.md)。

## SHIORI Event

详情请参阅[SHIORI Event 页面](../list/shiori-event/index.md)。

- **[OnHeadlinesenseBegin](../list/shiori-event/headline-rss/OnHeadlinesenseBegin.md)**: headline sensor 开始时。
- **[OnHeadlinesense.OnFind](../list/shiori-event/headline-rss/OnHeadlinesense.OnFind.md)**: 有要朗读的内容时。
- **[OnHeadlinesenseComplete](../list/shiori-event/headline-rss/OnHeadlinesenseComplete.md)**: headline sensor 正常结束时。
- **[OnHeadlinesenseFailure](../list/shiori-event/headline-rss/OnHeadlinesenseFailure.md)**: headline sensor 失败时。

## 补充说明

GET Headline 会被调用两次。第一次针对旧文件，第二次针对新文件。不过，旧文件到新文件的顺序可能会因实现而颠倒，因此不得编写依赖顺序的处理。

调试期间等需要始终显示（不变为 no update）时，请尝试在 descript.txt 中写入 alwaysdisplay,1（调试结束后务必删除）。
