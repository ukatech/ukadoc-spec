# PLUGIN/2.0

最終変更：2013-08-10

参考：[PLUGIN/1.0](http://usada.sakura.vg/contents/plugin.html)（外部サイト）

## 前書

PLUGIN/2.0は、旧来仕様（1.0）の改訂版です。SSPで実装。

整備中の規格であり、大幅な変更の可能性があります。

## バージョンの設計思想と影響評価

### 設計思想

手軽に本体やゴーストとやりとりできるよう改修し、SAORI群としてゴーストごとに分散してしまったもののうち「便利機能」にあたる部分を統合し、利用者側の利便性を改善する。

プラグイン開発者から実行環境へ負担を移すほうが良いでしょう……多分。

### 処理系

処理系にいろいろ負担を移すことを前提としていますので、覚悟してください（苦笑

### プラグイン作者

新たにコール用にrequestエクスポートを定義するので、PLUGIN/1.0との衝突は考慮する必要はありません。

スクリプトやイベント等のゴーストへの通知が非常に楽になる。

### ゴースト作者

特定のプラグインにたとえ対応していなくてもデフォルトスクリプト仕様（後述）があるので致命的な事にならない。

どうしてもデフォルトスクリプトで雰囲気を壊されたくない場合は対応しましょう……

### バージョンの影響評価

ゴーストごとにちりぢりになった機能群をまとめて扱えるので便利かつ楽。

## 実体

設定ファイル「descript.txt」とdllファイルの2つが必要です。

## DLL

[DLLのページ](dll.md)を参照してください。

*※YAYA/KAWARI as PLUGIN利用者・モジュール作者は読み飛ばして大丈夫です。*

## request規定

典型的なリクエスト例は以下の通り。※改行コード＝CR+LF

```
GET PLUGIN/2.0
ID: OnGhostChange
Charset: UTF-8
Reference0: 54
```

```
NOTIFY PLUGIN/2.0
ID: OnMenuExec
Charset: UTF-8
Sender: 晶子
Reference0: 17982
```

空行で終了。他のDLL仕様といっしょで、ゼロ終端とは限らないので注意してください。

PLUGIN/2.0のフォーマットは基本的にSHIORI/3.0仕様に準じています。<br />
イベント識別子のIDヘッダと、任意の数(8以降あり)の追加情報であるReferenceヘッダから構成されます。<br />
Referenceの内容はIDによって変わります。

Reference等の内容に改行等を含めたい場合、また含めなければならないと規定したい場合は、%8f%73のように、回避したい文字のみURLエンコードして渡すよう規定することを \*強く推奨\* します（仕様ではありませんが）

Senderの内容は、後述するゴースト側からの呼び出し仕様によって呼び出された場合、ゴースト名となります。<br />
本体側からコールされた場合はSenderヘッダ自体が消滅するか空文字列が代入されます。<br />
SHIORIのように「本体の名前（SSPとかCROWとか）」が入るわけではないので注意してください。

通知されるリクエストの種類（ID）については、[PLUGIN Eventのページ](../list/plugin-event/index.md)を参照してください。

## response規定

レスポンスの例は以下の通り。※改行コード＝CR+LF

```
PLUGIN/2.0 200 OK
Charset: Shift_JIS
Target: 54
Event: OnResourceLow
EventOption: notify
Reference0: 19
Reference1: 31
Reference2: 65
Script: すくりぷと～
ScriptOption: nobreak,notranslate
```

※複数起動対応の処理系のみ※ 現在起動中のゴーストでTargetに該当するゴーストがいたらそれで処理されます。<br />
"\_\_SYSTEM_ALL_GHOST\_\_"が指定されている場合は、「起動中の全ゴースト」に通知されます。

該当しない場合、何も指定しない場合は処理系に応じて適当なゴースト「1体」で処理されます。<br />
また、後述のゴースト側からの呼び出し仕様で呼ばれた場合は、Targetヘッダで明示的に指定がされない限り、呼んだゴーストに返ります。

※対応していない処理系ではそもそも1体しかありませんのでそのゴーストが毎度呼び出されます。

### Event/Reference

EventヘッダとReferenceヘッダはゴースト側に送るイベントです。<br />
これにゴーストが反応しない場合、デフォルトスクリプトであるScriptヘッダが再生されます。

### ScriptOption

ScriptOptionは、Scriptヘッダ内容にのみ適用されるオプション指定です。

- **notranslate**: ゴーストのトランスレートを介さない
- **nobreak**: 現在喋っているトークを中断せず最後まで喋った後で指定したスクリプトを実行する

### EventOption

EventOptionは、Eventヘッダ内容にのみ適用されるオプション指定です。

- **notify**: 指定したイベントをゴーストにnotifyで通知する

Event,EventOption,Reference,Target,Script,ScriptOptionはすべて省略可能です。<br />
例えばイベントだけ送りたい、デフォルトスクリプトは不要な場合はScript/ScriptOptionヘッダを省略してください。<br />
※スクリプトだけ送りたい場合はその逆です。

## プラグインID

[Plugin設定のIDの項](../descript/plugin/descript-txt/id.md)を参照してください。

## descript.txt

[Plugin設定のページ](../descript/plugin/index.md)を参照してください。

## ゴースト側拡張

### スクリプト拡張

```
\![raiseplugin,プラグイン名またはID,イベント,Reference0...]
\![notifyplugin,プラグイン名またはID,イベント,Reference0...]
```

指定したプラグインに指定したイベントを送信します。 プラグイン側でTarget指定がない限り(system_any)、プラグインからのレスポンスはraisepluginしたゴーストに優先的に割り振られますので、SAORIもどき的な使い方も可能です。

送信コマンドは、[`\![raiseplugin]`](../list/sakura-script/event/bang-raiseplugin-ID-r0-r1-r2.md)の場合はGET、[`\![notifyplugin]`](../list/sakura-script/event/bang-notifyplugin-ID-r0-r1-r2.md)の場合はNOTIFYとなります。

### SHIORIイベント拡張

[installedpluginの項目](../list/shiori-event/notify/installedplugin.md)を参照してください。
