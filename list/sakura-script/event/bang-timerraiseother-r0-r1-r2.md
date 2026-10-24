# `\![timerraiseother,時間,繰り返すか否か,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** イベントコマンド

待ち時間(ミリ秒)を指定して起動している他のゴーストへイベントを通知する。<br />
「繰り返すか否か」は0で指定時間ごとに繰り返しイベントが発生し、1以上で一回のみイベントが発生。<br />
第6引数以降はreference。<br />
別名のイベントはそれぞれに実行可能だが、同名のイベントに対して繰り返し実行した場合は上書きされる。<br />
同じイベント名で時間が0のさくらスクリプトを実行するとキャンセルできる。<br />
ゴースト名を\_\_SYSTEM_ALL_GHOST\_\_とすると起動している全てのゴーストに通知。<br />
ゴースト名はバイト値1区切りで複数指定可。

**対応:** SSP

## 記述例

```sakurascript
\![timerraiseother,30000,0,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5に30秒(30000ミリ秒)おきに繰り返しOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。\![timerraiseother,0,1,Emily/Phase4.5,OnRoastedPotate]ここで繰り返し通知をキャンセル。
```
