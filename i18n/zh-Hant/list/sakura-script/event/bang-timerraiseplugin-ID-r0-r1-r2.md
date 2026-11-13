# `\![timerraiseplugin,時間,繰り返すか否か,プラグインのIDまたは名前,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件指令

指定等待時間（毫秒），向 plugin 傳送指定的事件。<br />
「是否重複」指定為 0 時，每隔指定時間重複觸發事件；指定為 1 以上時，只觸發一次事件。<br />
不同名稱的事件可分別執行，但對同名事件重複執行時會覆寫先前的設定。<br />
執行事件名稱相同且時間為 0 的 Sakura Script 即可取消。<br />
\[SSP 2.9.35\] 也可以指定 plugin 的 [UUID](../../propertysystem/property-system/general-property/uuid.md)（與 [raiseplugin](bang-raiseplugin-ID-r0-r1-r2.md) 相同）。目的對象是在每次傳送事件時查找，而非設定計時器時查找。

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseplugin,60000,0,実体化,OnMenuExec]プラグイン「実体化」を60秒(60000ミリ秒)おきに繰り返し実行。\![timerraiseplugin,0,0,実体化,OnMenuExec]ここで繰り返し実行をキャンセル。
```
