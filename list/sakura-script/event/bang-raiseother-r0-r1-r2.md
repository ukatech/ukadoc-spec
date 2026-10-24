# `\![raiseother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** イベントコマンド

起動している他のゴーストへイベントを通知する。<br />
第4引数以降はreference。<br />
ゴースト名を「\_\_SYSTEM_ALL_GHOST\_\_」とすると起動している全てのゴーストに通知。<br />
ゴースト名は直接指定のみ、バイト値1区切りで複数指定可。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![raiseother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。
```
