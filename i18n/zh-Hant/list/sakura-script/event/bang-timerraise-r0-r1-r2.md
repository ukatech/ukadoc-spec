# `\![timerraise,時間,繰り返すか否か,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

Specify the wait time (in milliseconds) in 「時間」 to execute an event.<br />
For 「繰り返すか否か」, specify 0 to trigger the event repeatedly at the specified interval, or 1 or greater to trigger it only once.<br />
The fifth and subsequent arguments are references.<br />
Events with different names can each be executed, but repeated execution of an event with the same name overwrites the previous one.<br />
To cancel, execute Sakura Script with the same event name and a time of 0.<br />
The timer persists after a network update.

If 「繰り返すか否か」 is 0, it remains active until the specified event occurs. If 「繰り返すか否か」 is 1 or greater, it remains active until the ghost exits.

**対応:** SSP

## 記述例

```sakurascript
\![timerraise,5000,1,OnTimerraiseTest,test]5秒後(5000ミリ秒)後に、OnTimerraiseTestが発生する。さくらスクリプトが実行された瞬間から時間をカウントする。\![timerraise,0,1,OnTimerraiseTest]ここで先ほどのタイマー予約をキャンセル。
```
