# `\![set,otherghosttalk,true|false|before|after]`

**カテゴリ:** Event command

Set whether to send notifications for [OnOtherGhostTalk](../../shiori-event/other/OnOtherGhostTalk.md). The default is false.<br />
When set to anything other than false, OnOtherGhostTalk is sent when another concurrently running ghost speaks.<br />
When before is specified, the notification is sent before it speaks; when after is specified, it is sent after it speaks. true is equivalent to after.

This setting remains in effect until the ghost exits.

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,otherghosttalk,true]これ以降、同時に起動しているゴーストが何か喋り終わるたびに、OnOtherGhostTalkが通知されるようになる。
```
