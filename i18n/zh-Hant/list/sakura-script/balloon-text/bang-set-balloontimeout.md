# `\![set,balloontimeout,時間]`

**カテゴリ:** balloon, text command

Specifies the timeout duration for balloon display. The unit is milliseconds.<br />
The timeout countdown starts after the script finishes displaying. A value of 0 or less disables the timeout.<br />
This setting is in effect only during the current script.

Omitting the duration: restores the default value<br />
Duration set to 0 or -1: no timeout

**対応:** SSP

## 記述例

```sakurascript
\![set,balloontimeout,3000]このトークは、喋り終わってから3秒でバルーンが閉じる。
```
