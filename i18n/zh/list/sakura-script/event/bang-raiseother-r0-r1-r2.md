# `\![raiseother,ゴースト名,イベント名,r0,r1,r2...]`

**カテゴリ:** 事件命令

向其他正在运行的ghost发送事件通知。<br />
第4个及之后的参数是reference。<br />
将ghost名称设为「\_\_SYSTEM_ALL_GHOST\_\_」时，会向所有正在运行的ghost发送通知。<br />
仅可直接指定ghost名称；可以使用字节值1作为分隔符指定多个名称。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![raiseother,Emily/Phase4.5,OnRoastedPotate,sweet potato]Emily/Phase4.5が同時起動していれば、Emily/Phase4.5にOnRoastedPotateを通知。Reference0には「sweet potato」が入っている。
```
