# `\![timerraiseplugin,時間,繰り返すか否か,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Sends the specified event to a plugin after the specified wait time (in milliseconds).<br />
For "whether to repeat," specify 0 to trigger the event repeatedly at the specified interval, or 1 or greater to trigger it only once.<br />
Events with different names can each be run independently, but repeated runs of an event with the same name overwrite the previous one.<br />
To cancel, run Sakura Script with the same event name and a time of 0.

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseplugin,60000,0,実体化,OnMenuExec]プラグイン「実体化」を60秒(60000ミリ秒)おきに繰り返し実行。\![timerraiseplugin,0,0,実体化,OnMenuExec]ここで繰り返し実行をキャンセル。
```
