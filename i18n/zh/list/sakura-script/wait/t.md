# `\t`

**カテゴリ:** Wait commands

Time-critical section.<br />
Until the script is interrupted (e.g. by selecting an option or double-clicking a balloon) or `\e`, events such as mouse events are not reported.<br />
Note that entering `\t` again does not end the section.<br />
To end it partway through, use `\![raise,イベント名]` to terminate the current script and trigger another event.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
この文章表示中はマウス反応を受け付ける。\tこれ以降スクリプト再生終了まで受け付けない。
```
