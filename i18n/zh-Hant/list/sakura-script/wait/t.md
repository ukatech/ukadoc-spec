# `\t`

**カテゴリ:** Wait command

Time-critical section.<br />
From here until the script is broken (for example, by selecting a choice or interrupting with a double-click on the balloon) or `\e`, event notifications such as mouse events are not sent.<br />
Note that writing `\t` again does not cancel this state.<br />
To cancel it mid-script, use `\![raise,イベント名]` to end the current script and trigger another event.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
この文章表示中はマウス反応を受け付ける。\tこれ以降スクリプト再生終了まで受け付けない。
```
