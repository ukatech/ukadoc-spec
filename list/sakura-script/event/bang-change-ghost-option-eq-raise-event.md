# `\![change,ghost,ゴースト名(,--option=raise-event)]`

**カテゴリ:** イベントコマンド

そのゴーストへの切り替えを行う。<br />
ゴースト名をrandomにするとランダムチェンジ(\\+と同様)。<br />
sequentialにするとシーケンシャルチェンジ(`\_`+と同様)。<br />
実行後、該当ゴーストがいなかった場合は無視される。

ゴースト名をlastinstalledにすると最後にインストールしたゴーストに切り替え。ただしSSPを一度終了した場合は無効。<br />
ゴースト名をrandomにするとランダムに切り替え。

SSP 2.4.74以降で、ゴースト名の後に--option=raise-eventとすると、メニューから切り替え操作をした場合と同じく[OnGhostChanging](../../shiori-event/boot-close-change/OnGhostChanging.md)が通知される。<br />
この場合、バルーンブレーク（通常ダブルクリック）による中止操作も可能な点に注意。<br />
指定しない場合は通知されない。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
Emily/Phase4.5に交代。\![change,ghost,Emily/Phase4.5]
```
