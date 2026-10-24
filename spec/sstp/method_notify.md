# メソッド：NOTIFY

ゴーストにイベントを通知するためのメソッドである。<br />
SENDとNOTIFYは同一の処理として扱われ、機能上の差異はない。共通するヘッダの詳細やIfGhostの振り分けルールなどの仕様は[メソッド：SEND](method_send.md)を参照のこと。<br />
Eventヘッダ＝SHIORI/3.0 IDに対応し、Reference\*はそのまま引き渡される。

## イベント通知のみサンプル(NOTIFY/1.0)

```
NOTIFY SSTP/1.0
Charset: UTF-8
Sender: Media Player
Event: OnMusicPlay
Reference0: 自由の翼
Reference1: Linked Horizon
```

ゴースト側で指定したイベントIDに反応しない場合に、「保険用の」スクリプトを指定して再生させることができる。<br />
その際に、IfGhostヘッダを指定すると、直後にあるScriptヘッダは指定したゴースト専用のスクリプトとして扱われる。

## 保険反応つきサンプル(NOTIFY/1.1)

```
NOTIFY SSTP/1.1
Charset: UTF-8
Sender: Media Player
Event: OnMusicPlay
Reference0: 紅蓮の弓矢
Reference1: Linked Horizon
IfGhost: Emily,Teddy
Script: \0\s[6]その日、エミリは思い出した…\n\s[7]まだ今日は芋食べてない！\1\s[11]わざわざ今思い出したの？
IfGhost: ラーシェ,ティセ
Script: \0\s[3]巨人っていっても、身長は列車数両分しかないよね。\1\s[14]それが縦に立ち上がるとさすがに大きいと思うけどね。
```

## request固有ヘッダ

Event、Reference\*、Script、IfGhost、Ghostなどの共通ヘッダの詳細は[メソッド：SEND](method_send.md)を参照。

- **Option**: SSTPで実行されるSakuraScriptや指定されたイベントがどのように扱われるかのオプションを指定する。<br />
  カンマ区切りで複数指定可能。指定する文字列のうち、NOTIFY特有分は以下の通り。<br />
  notify : イベントを強制的にNOTIFYで送る。また、保険用スクリプトは[ValueNotifyヘッダで返された場合](../shiori3/request.md)と同じように強制的に扱われる。 \[SSP 2.6.76\]

## response固有ヘッダ

- **Script**: イベント通知の結果再生されたスクリプト。現在SSPのみ対応。
