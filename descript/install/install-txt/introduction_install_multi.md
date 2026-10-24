# 同時インストール

## 概要

SSPでは、ゴーストやシェルのアーカイブにバルーンなどを同梱して、まとめてインストールさせる事ができる。<br />
同梱する内容は「\*.」で始まるエントリで指定し、\*の部分には同梱する内容の種別が入る。

\*に書けるのは下記の5種類。

- **balloon**: バルーン
- **headline**: ヘッドラインセンサ
- **plugin**: プラグイン
- **calendar.skin**: カレンダーの外見ファイル
- **calendar.plugin**: カレンダーのスケジュールセンサ

[type](type.md)での表記と異なり、カレンダー系は*ドット区切り*である事に注意（calendar skinではなくcalendar.skin）。

アーカイブ自身の[type](type.md)を問わず機能するが、実用上はtypeが*ghost*か*shell*のアーカイブで用いる。

## 複数同梱する場合の番号の付け方

同じ種別のものを複数同梱する場合は、\*の部分を balloon0、balloon1、… のように、種別の後ろへ0始まりの番号を付けて並べる。（SSP 2.7.00以降）

探索は*無印→0→1→2…*の順に行われ、*見つからない番号が出た時点で打ち切られる*。<br />
そのため*欠番を作ってはいけない*。例えばballoon0とballoon2だけを書いた場合、balloon1が無い時点で打ち切られるため、balloon2は読まれない。

無印と0は別のものとして扱われる。balloonとballoon0を両方書けば、バルーンが2個インストールされる。

[\*.directory](star-.directory.md)、[\*.source.directory](star-.source.directory.md)、[\*.refresh](star-.refresh.md)、[\*.refreshundeletemask](star-.refreshundeletemask.md)は、いずれも番号ごとに独立して指定できる。

なお、ゴーストやシェルに*紐づくバルーンとして設定されるのは最初の1個だけ*である。<br />
2個目以降はインストールされるだけで、そのゴーストの標準バルーンにはならない。

## 記述例

ゴーストにバルーン2個とプラグイン1個を同梱する場合

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
balloon0.directory,example_balloon
balloon0.source.directory,balloon_normal
balloon1.directory,example_balloon_ex
balloon1.source.directory,balloon_special
plugin0.directory,example_plugin
```
