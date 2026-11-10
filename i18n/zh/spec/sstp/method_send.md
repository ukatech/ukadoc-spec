# 方法：SEND

SEND是一种方法，用于从外部应用程序向 ghost 发送Sakura Script或SHIORI事件并使其播放。<br />
SEND和NOTIFY按相同的处理方式处理，两者在功能上没有差异。以下规范同样适用于NOTIFY。<br />
既可以通过Script标头直接指定Sakura Script，也可以通过Event标头发送事件并从SHIORI响应中获取脚本。<br />
Event和Script可以同时使用；如果SHIORI对Event的响应没有返回脚本，则会回退到Script标头中的脚本。<br />
如果未指定目标 ghost，则以当前已启动的 ghost 为目标。

## 基本脚本播放示例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\w5\u\s[10]ご機嫌いかが？\e
```

## 事件发送示例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnExternalEvent
Reference0: param1
Reference1: param2
```

## 事件＋回退脚本示例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnCustomEvent
Reference0: data
Script: \h\s[0]イベント未対応時のスクリプト\e
```

通过多次书写IfGhost标头，并与对应的Script标头组合，可以为不同的 ghost 指定不同的脚本。

## 使用IfGhost分发的示例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\e
IfGhost: まゆら
Script: \h\s[0]まゆらさん、こんにちは。\e
IfGhost: 花ちゃん,妹
Script: \h\s[0]花ちゃんと妹さん、こんにちは。\e
```

## 带中断抑制的示例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]割り込まないで追加。\e
Option: nobreak
```

## request专用标头

- **Sender**: 虽然是共通标头，但在SEND/NOTIFY中可以使用特殊值`Sender: First`。指定后，目标为首次启动时的 ghost（sakura）。<br />
  如果Sender和User-Agent均未指定，则返回400 Bad Request。
- **Script**: 要播放的Sakura Script。<br />
  与Event标头同时使用时，如果SHIORI对Event的响应没有返回脚本，则该脚本将作为回退脚本使用。
- **Entry**: 条目数据。会传递给SHIORI。
- **Event**: SHIORI事件名。在SHIORI/3.0中作为ID标头处理。
- **Reference\***: 事件的Reference标头。只进行字符编码转换等最低限度的处理，然后原样传递给SHIORI。
- **IfGhost**: 按`\0`侧名,`\1`侧名的格式指定 ghost 名称后，紧随其后的Script标头会被视为仅供特定 ghost 使用。<br />
  如果存在不紧跟在IfGhost之后的Script标头，则该Script用于未匹配IfGhost时的默认处理。<br />
  如果省略，则对任何 ghost 都播放相同的Script标头。<br />
  有关详细的分发规则，请参阅后文的[使用IfGhost分发脚本](method_send.md#ifghostによるスクリプト振り分け)。
- **Ghost**: 通过 ghost 名称（descript.txt的name）指定目标 ghost。
- **Option**: 指定SSTP执行的Sakura Script的处理方式。<br />
  可以用逗号分隔指定多个选项。除共通选项（nodescript、notranslate等）外，可在SEND/NOTIFY中使用的选项标志如下。<br />
  nobreak : 将脚本加入队列，不中断当前正在播放的脚本。<br />
  notify : 以notify模式（无需响应）发送SHIORI事件。此外，脚本也会像[ValueNotify标头返回时](../shiori3/request.md)一样被强制处理。 \[SSP 2.6.76\]

## response专用标头

- **Script**: 实际播放的脚本。换行符会被移除。
- **SHIORI自定义标头**: SHIORI响应中包含的标头会被透传。

## 使用IfGhost分发脚本

通过多次书写IfGhost标头，并与对应的Script标头组合，可以为不同的 ghost 指定不同的脚本。<br />
IfGhost与Script按出现顺序对应。写在第一个IfGhost之前的Script为默认脚本。

- **名称匹配**: 如果IfGhost的格式为“`\0`侧名,`\1`侧名”，则两个名称都必须匹配。<br />
  如果IfGhost的格式仅为“`\0`侧名”，则只要`\0`侧名匹配即可选中。<br />
  如果均不匹配，则使用默认脚本。但是，如果 ghost 端启用了“拒绝未指定SSTP”设置，则也不会使用默认脚本。
- **按默认ghost处理**: 以下名称会按默认ghost（sakura）处理，其脚本也会作为默认脚本使用。<br />
  「さくら」「エミリ」「えみりぃ」
