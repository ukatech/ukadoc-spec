# `\![call,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** イベントコマンド

ゴースト名で指定されたゴーストを呼び出す。<br />
ゴースト名をlastinstalledにすると最後にインストールしたゴーストを呼び出し。<br />
ゴースト名をrandomにするとランダムに呼び出し。<br />
\[SSP 2.9.35\] ゴースト名の代わりに、ゴーストの[UUID](../../propertysystem/property-system/general-property/uuid.md)も指定できる(名前が同じゴーストを取り違えない)。

SSP 2.4.74以降で、ゴースト名の後に--option=raise-eventとすると、メニューから切り替え操作をした場合と同じく[OnGhostCalling](../../shiori-event/boot-close-change/OnGhostCalling.md)が通知される。<br />
指定しない場合は通知されない。

**対応:** SSP / Ninix

## 記述例

```sakurascript
Emily/Phase4.5を呼び出す。\![call,ghost,Emily/Phase4.5]
```
