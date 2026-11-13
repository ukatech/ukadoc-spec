# 方法：SEND

SEND是用于从外部应用程序向ghost发送并播放Sakura Script或SHIORI事件的方法。<br />
SEND和NOTIFY作为相同的处理来对待，两者在功能上没有区别。以下规格同样适用于NOTIFY。<br />
既可以通过Script头直接指定Sakura Script，也可以通过Event头发送事件并从SHIORI响应中获取脚本。<br />
Event和Script可以同时使用；如果针对Event的SHIORI响应未返回脚本，则回退到Script头中的脚本。<br />
未指定目标ghost时，以当前运行中的ghost为目标。

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

通过多次填写IfGhost头并与对应的Script头组合，可以为各个ghost指定不同的脚本。

## 使用IfGhost分配脚本的示例

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

## 禁止中断的示例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]割り込まないで追加。\e
Option: nobreak
```

## request专用头

- **Sender**: 虽然是通用头，但在SEND/NOTIFY中可以使用特殊值`Sender: First`。指定后，以首次启动时的ghost（sakura）为目标。<br />
  如果Sender和User-Agent都未指定，则返回400 Bad Request。
- **Script**: 要播放的Sakura Script。<br />
  与Event头同时使用时，若针对Event的SHIORI响应未返回脚本，则将其用作回退脚本。
- **Entry**: 条目数据，传递给SHIORI。
- **Event**: SHIORI事件名。在SHIORI/3.0中作为ID头的指定值处理。
- **Reference\***: 事件的Reference头。经过字符编码转换等最低限度的处理后，原样传递给SHIORI。
- **IfGhost**: 以“`\0`侧名称,`\1`侧名称”的格式指定ghost名称时，紧随其后的Script头将作为特定ghost专用的脚本处理。<br />
  如果存在不紧跟在IfGhost之后的Script头，则将其作为不匹配IfGhost时的默认处理脚本。<br />
  \[SSP 2.9.35\] 也可以用ghost的[UUID](../../list/propertysystem/property-system/general-property/uuid.md)代替名称（不含逗号，采用UUID格式）。这样可以区分名称相同的ghost并分配脚本。<br />
  省略时，对所有ghost播放相同的Script头中的脚本。<br />
  详细的分配规则参见下文的[使用IfGhost分配脚本](method_send.md#ifghostによるスクリプト振り分け)。
- **Ghost**: 通过ghost名称（descript.txt中的name）指定目标ghost。
- **Option**: 指定SSTP执行的Sakura Script的处理方式。<br />
  可以用逗号分隔来指定多个选项。除通用选项（nodescript、notranslate等）外，SEND/NOTIFY可用的选项标志如下。<br />
  nobreak : 将脚本加入队列，不中断当前播放的脚本。<br />
  notify : 以notify模式（无需响应）发送SHIORI事件。此外，脚本会被强制按[通过ValueNotify头返回](../shiori3/request.md)时的方式处理。 \[SSP 2.6.76\]

## response专用头

- **Script**: 实际播放的脚本。换行符会被移除。
- **SHIORI自定义头**: SHIORI响应中包含的头会被透传。

## 使用IfGhost分配脚本

通过多次填写IfGhost头并与对应的Script头组合，可以为各个ghost指定不同的脚本。<br />
IfGhost和Script按出现顺序对应。在第一个IfGhost之前填写的Script将成为默认脚本。

- **名称匹配**: 如果IfGhost采用“`\0`侧名称,`\1`侧名称”格式，则两个名称都必须匹配。<br />
  如果IfGhost只有“`\0`侧名称”，则仅凭`\0`侧名称匹配即可选中。<br />
  \[SSP 2.9.35\] 如果IfGhost采用UUID格式（base64的22个字符加`==`），则通过匹配ghost的UUID而非名称来选中。如果多个具有相同UUID的ghost正在运行，则优先选择显示中的ghost。<br />
  如果均不匹配，则使用默认脚本。但如果ghost设置为“拒绝未指定目标的SSTP”，则默认脚本也不会被使用。
- **作为默认ghost处理**: 以下名称被视为默认ghost（sakura），其脚本也可作为默认脚本使用。<br />
  “さくら”“エミリ”“えみりぃ”
