# `\![change,shell,シェル名(,--option=raise-event)]`

**カテゴリ:** イベントコマンド

そのシェルへの切り替えを行う。<br />
該当シェルがなかった場合は無視される。<br />
変更後SHIORIイベント[OnShellChanged](../../shiori-event/boot-close-change/OnShellChanged.md)が通知される。

シェル名をlastinstalledにすると最後にインストールしたゴーストに切り替え。ただしSSPを一度終了した場合は無効。<br />
シェル名をrandomにするとランダムに切り替え。

SSP 2.4.74以降で、シェル名の後に--option=raise-eventとすると、メニューから切り替え操作をした場合と同じく[OnShellChanging](../../shiori-event/boot-close-change/OnShellChanging.md)が通知される。<br />
この場合、バルーンブレーク（通常ダブルクリック）による中止操作も可能な点に注意。<br />
指定しない場合は通知されない。

**対応:** SSP / CROW / Ninix

## 記述例

```sakurascript
masterシェルに切り替え。\![change,shell,master]
```
