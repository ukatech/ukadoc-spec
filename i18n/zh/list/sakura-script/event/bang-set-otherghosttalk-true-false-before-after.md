# `\![set,otherghosttalk,true|false|before|after]`

**カテゴリ:** 事件命令

设置是否通知 [OnOtherGhostTalk](../../shiori-event/other/OnOtherGhostTalk.md)。初始值为 false。<br />
设置为 false 以外的值后，同时运行的其他 ghost 说话时，就会收到 OnOtherGhostTalk 通知。<br />
指定 before 时，会在说话前通知；指定 after 时，会在说话后通知。true 与 after 相同。

有效期至 ghost 结束。

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,otherghosttalk,true]これ以降、同時に起動しているゴーストが何か喋り終わるたびに、OnOtherGhostTalkが通知されるようになる。
```
