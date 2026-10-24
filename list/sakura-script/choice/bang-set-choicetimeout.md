# `\![set,choicetimeout,時間]`

**カテゴリ:** 選択肢コマンド

選択肢のタイムアウトの時間を指定する。単位はミリ秒。<br />
時間のカウントはトークの表示が全て終わってから開始される。<br />
そのスクリプト中のみ有効。選択肢より後ろに書いても有効。<br />
選択肢がタイムアウトした場合、[OnChoiceTimeout](../../shiori-event/choice/OnChoiceTimeout.md)イベントが発生する。

時間指定を省略：デフォルト値に戻す<br />
時間指定が0か-1：タイムアウトしない

**対応:** Materia / SSP / CROW

## 記述例

```sakurascript
\q[早押し,FastPush]\![set,choicetimeout,500]
```
