# `\![timernotify,時間,繰り返すか否か,イベント名,r0,r1,r2...]`

**カテゴリ:** イベントコマンド

timerraiseと同じで、違いはこの通知イベントで何か値を返してもSSPに反映されないということのみ。

**対応:** SSP

## 記述例

```sakurascript
\![notify,OnNotifyTest,test]OnNotifyTestが通知され、Reference0に「test」が入っている。OnNotifyTestでトークを書いてもSSPに反映されない。
```
