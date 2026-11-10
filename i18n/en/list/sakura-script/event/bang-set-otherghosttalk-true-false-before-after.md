# `\![set,otherghosttalk,true|false|before|after]`

**カテゴリ:** Event command

Sets whether to send the [OnOtherGhostTalk](../../shiori-event/other/OnOtherGhostTalk.md) notification. The default is false.<br />
When set to anything other than false, OnOtherGhostTalk is sent when another concurrently running ghost speaks.<br />
If before is specified, the notification is sent before it speaks; if after is specified, it is sent after it speaks. true is equivalent to after.

Valid until the ghost ends.

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,otherghosttalk,true]これ以降、同時に起動しているゴーストが何か喋り終わるたびに、OnOtherGhostTalkが通知されるようになる。
```
