# `\t`

**カテゴリ:** Wait command

Time-critical section.<br />
No notifications of events such as mouse events are sent until the script is interrupted (for example, by selecting a choice or double-clicking a balloon) or reaches `\e`.<br />
Note that entering `\t` again does not end the section.<br />
To end it partway through, use `\![raise,イベント名]` to end the current script and trigger another event.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
この文章表示中はマウス反応を受け付ける。\tこれ以降スクリプト再生終了まで受け付けない。
```
