# `\![set,balloontimeout,時間]`

**カテゴリ:** balloon, text command

Specifies the timeout for displaying the balloon. The unit is milliseconds.<br />
The timeout countdown starts after the script has finished displaying. A value of 0 or less disables the timeout.<br />
It is in effect only during the script.

Omitting the time specification: restores the default value<br />
A time specification of 0 or -1: no timeout

**対応:** SSP

## 記述例

```sakurascript
\![set,balloontimeout,3000]このトークは、喋り終わってから3秒でバルーンが閉じる。
```
