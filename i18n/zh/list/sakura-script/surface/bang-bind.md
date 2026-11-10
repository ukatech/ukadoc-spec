# `\![bind,カテゴリ名,パーツ名,数値]`

**カテゴリ:** 表面命令

穿上或脱下dressup部件。<br />
数值部分为1时穿上，为0时脱下。<br />
部件名留空时，按类别执行操作。<br />
数值栏留空或省略时，会像操作菜单一样切换ON/OFF。<br />
脚本执行后，会通知SHIORI事件OnDressupChanged，随后通知SHIORI事件OnNotifyDressupInfo。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![bind,head,ribbon,1]本体側の着せ替えとして設定された、headカテゴリのribbonを装着。\1\![bind,arm,,0]相方側の着せ替えとして設定された、armカテゴリのパーツを全て解除。
```
