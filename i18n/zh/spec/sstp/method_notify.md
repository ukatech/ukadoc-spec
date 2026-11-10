# 方法：NOTIFY

用于向 ghost 通知事件。<br />
SEND和NOTIFY按相同的处理方式处理，在功能上没有差异。有关共通标头的详细信息以及IfGhost的分发规则等规范，请参阅[方法：SEND](method_send.md)。<br />
Event标头对应SHIORI/3.0的ID，Reference\*会原样传递。

## 仅通知事件的示例（NOTIFY/1.0）

```
NOTIFY SSTP/1.0
Charset: UTF-8
Sender: Media Player
Event: OnMusicPlay
Reference0: 自由の翼
Reference1: Linked Horizon
```

如果 ghost 不响应指定的事件ID，可以指定一段“备用”脚本并播放。<br />
此时，如果指定了IfGhost标头，则紧随其后的Script标头会被视为仅供指定 ghost 使用的脚本。

## 带备用响应的示例（NOTIFY/1.1）

```
NOTIFY SSTP/1.1
Charset: UTF-8
Sender: Media Player
Event: OnMusicPlay
Reference0: 紅蓮の弓矢
Reference1: Linked Horizon
IfGhost: Emily,Teddy
Script: \0\s[6]その日、エミリは思い出した…\n\s[7]まだ今日は芋食べてない！\1\s[11]わざわざ今思い出したの？
IfGhost: ラーシェ,ティセ
Script: \0\s[3]巨人っていっても、身長は列車数両分しかないよね。\1\s[14]それが縦に立ち上がるとさすがに大きいと思うけどね。
```

## request专用标头

有关Event、Reference\*、Script、IfGhost、Ghost等共通标头的详细信息，请参阅[方法：SEND](method_send.md)。

- **Option**: 指定SSTP执行的Sakura Script或指定事件的处理方式。<br />
  可以用逗号分隔指定多个选项。指定字符串中，NOTIFY特有的选项如下。<br />
  notify : 强制通过NOTIFY发送事件。此外，备用脚本也会像[ValueNotify标头返回时](../shiori3/request.md)一样被强制处理。 \[SSP 2.6.76\]

## response专用标头

- **Script**: 事件通知后播放的脚本。目前仅SSP支持。
