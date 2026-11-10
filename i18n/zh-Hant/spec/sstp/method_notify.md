# 方法：NOTIFY

這是用來向 ghost 通知事件的方法。<br />
SEND和NOTIFY會以相同的方式處理，功能上沒有差異。共通標頭的詳細資訊、IfGhost的分派規則等規格，請參閱[方法：SEND](method_send.md)。<br />
Event標頭對應SHIORI/3.0 ID，Reference\*則會原樣傳遞。

## 僅通知事件的範例（NOTIFY/1.0）

```
NOTIFY SSTP/1.0
Charset: UTF-8
Sender: Media Player
Event: OnMusicPlay
Reference0: 自由の翼
Reference1: Linked Horizon
```

若 ghost 端未對指定的事件 ID 做出反應，可以指定並播放「備用」指令碼。<br />
此時，若指定IfGhost標頭，緊接在後的Script標頭會被視為僅供指定 ghost 使用的指令碼。

## 附帶備用反應的範例（NOTIFY/1.1）

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

## request 專用標頭

共通標頭Event、Reference\*、Script、IfGhost、Ghost等的詳細資訊，請參閱[方法：SEND](method_send.md)。

- **Option**：指定SSTP執行的Sakura Script或指定事件的處理方式。<br />
  可用逗號分隔指定多個選項。指定字串中，NOTIFY 專用的部分如下。<br />
  notify：強制以NOTIFY傳送事件。此外，備用指令碼也會以與[ValueNotify標頭傳回時](../shiori3/request.md)相同的方式強制處理。\[SSP 2.6.76\]

## response 專用標頭

- **Script**：事件通知後播放的指令碼。目前僅支援SSP。
