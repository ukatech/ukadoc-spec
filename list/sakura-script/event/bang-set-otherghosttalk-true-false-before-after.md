# `\![set,otherghosttalk,true|false|before|after]`

**カテゴリ:** イベントコマンド

[OnOtherGhostTalk](../../shiori-event/other/OnOtherGhostTalk.md)を通知するかどうかを設定。初期値false。<br />
false以外を設定すると、同時起動している他ゴーストが喋った時OnOtherGhostTalkが通知されるようになる。<br />
beforeを指定すると喋る前、afterを指定すると喋った後に通知。trueはafterと同じ。

ゴースト終了まで有効。

**対応:** SSP / Ninix

## 記述例

```sakurascript
							\![set,otherghosttalk,true]これ以降、同時に起動しているゴーストが何か喋り終わるたびに、OnOtherGhostTalkが通知されるようになる。
```
