# `\![set,balloontimeout,時間]`

**カテゴリ:** Balloon, text command

Specifies the timeout for displaying the balloon. The unit is milliseconds.<br />
The timeout is counted from when the script finishes displaying. A value of 0 or less disables the timeout.<br />
This setting is effective only during the current script.

Omitting the time: Reverts to the default value<br />
Time specified as 0 or -1: No timeout

**対応:** SSP

## 記述例

```sakurascript
\![set,balloontimeout,3000]このトークは、喋り終わってから3秒でバルーンが閉じる。
```
