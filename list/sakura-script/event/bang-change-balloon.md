# `\![change,balloon,バルーン名]`

**カテゴリ:** イベントコマンド

そのバルーンへの切り替えを行う。<br />
該当バルーンがなかった場合は無視される。<br />
変更後SHIORIイベント[OnBalloonChange](../../shiori-event/boot-close-change/OnBalloonChange.md)が通知される。

バルーン名をlastinstalledにすると最後にインストールしたバルーンに切り替え。ただしSSPを一度終了した場合は無効。<br />
バルーン名をrandomにするとランダムに切り替え。

**対応:** SSP / Ninix

## 記述例

```sakurascript
SSPデフォルト+にバルーン変更。\![change,balloon,SSPデフォルト+]
```
