# `\![set,otherghosttalk,true|false|before|after]`

**カテゴリ:** 事件命令

設定是否通知[OnOtherGhostTalk](../../shiori-event/other/OnOtherGhostTalk.md)。初始值為false。<br />
設定為false以外的值時，同時啟動的其他ghost說話後，便會通知OnOtherGhostTalk。<br />
指定before時，會在說話前通知；指定after時，則在說話後通知。true與after相同。

在ghost結束前有效。

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,otherghosttalk,true]これ以降、同時に起動しているゴーストが何か喋り終わるたびに、OnOtherGhostTalkが通知されるようになる。
```
