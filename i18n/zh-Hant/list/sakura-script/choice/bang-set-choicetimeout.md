# `\![set,choicetimeout,時間]`

**カテゴリ:** 選項指令

設定選項的逾時時間。單位為毫秒。<br />
文字全部顯示完畢後，才開始計時。<br />
只在該腳本中有效。即使寫在選項之後也有效。<br />
選項逾時時，會觸發[OnChoiceTimeout](../../shiori-event/choice/OnChoiceTimeout.md)事件。

省略時間指定：恢復預設值<br />
時間指定為 0 或 -1：不逾時

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[早押し,FastPush]\![set,choicetimeout,500]
```
