# Method: NOTIFY

This method notifies a ghost of an event.<br />
SEND and NOTIFY are handled identically and have no functional differences. For details about common headers and specifications such as the IfGhost routing rules, see [Method: SEND](method_send.md).<br />
The Event header corresponds to the SHIORI/3.0 ID, and Reference\* is passed through as is.

## Event notification only sample (NOTIFY/1.0)

```
NOTIFY SSTP/1.0
Charset: UTF-8
Sender: Media Player
Event: OnMusicPlay
Reference0: 自由の翼
Reference1: Linked Horizon
```

If the ghost does not respond to the specified event ID, you can specify a “fallback” script to play instead.<br />
If you specify an IfGhost header in this case, the Script header immediately following it is treated as a script exclusive to the specified ghost.

## Sample with fallback response (NOTIFY/1.1)

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

## Request-specific headers

For details about common headers such as Event, Reference\*, Script, IfGhost, and Ghost, see [Method: SEND](method_send.md).

- **Option**: Specifies options for how Sakura Script executed by SSTP or the specified event is handled.<br />
  Multiple values can be specified, separated by commas. Of the strings that can be specified, the NOTIFY-specific one is as follows.<br />
  notify : Forces the event to be sent as NOTIFY. Also, the fallback script is handled forcibly in the same way as when returned in a [ValueNotify header](../shiori3/request.md). \[SSP 2.6.76\]

## Response-specific headers

- **Script**: The script played as a result of the event notification. Currently supported only by SSP.
