# HEADLINE/2.0

最終変更：2013-08-07

参考：[HEADLINE/1.1](http://usada.sakura.vg/contents/headlinesenser.html)（外部サイト）

## 前書

HEADLINE/2.0は、旧来仕様（1.1）の改訂版です。現在SSPのみ実装。

主な変更は文字コード指定の追加です。

## ヘッドラインの実体

設定ファイル「descript.txt」とexecute 関数をエクスポートするdllファイルの2つが必要です。

## DLL

[DLLのページ](dll.md)を参照してください。

## request - response 1: version取得

### request例

```
GET Version HEADLINE/2.0
Charset: UTF-8
Sender: SSP
```

### requestヘッダ詳細

- **Charset**: 文字コード
- **Sender**: イベント送信元

### response例

```
HEADLINE/2.0 200 OK
Charset: UTF-8
Value: HeadlineModule 1.1
```

### responseヘッダ詳細

- **Charset**: \[省略可\]文字コード。省略した場合は呼び出し側指定のもの。
- **Value**: \[省略可\]バージョン文字列

## request - response 2: ヘッドライン取得

### request例

```
GET Headline HEADLINE/2.0
Charset: UTF-8
Sender: SSP
Option: url
Path: C:\SSP\temp\ad9326dc37cb86a9.html
```

### requestヘッダ詳細

- **Charset**: 文字コード
- **Sender**: イベント送信元
- **Option**: \[省略可\]応答で解析可能なオプション。カンマ区切りで列挙。<br />
  現在urlのみ。responseのHeadlineヘッダの項参照。
- **Path**: ヘッドライン解析対象ファイルパス（フルパス）。

### response例

```
HEADLINE/2.0 200 OK
Charset: UTF-8
Headline: ほげほげ1
Headline: ほげほげ2
Headline: ほげほげ3
Headline: ほげほげ4
Headline: ほげほげ5
```

### responseヘッダ詳細

- **Charset**: \[省略可\]文字コード。省略した場合は呼び出し側指定のもの。
- **RequestCharset**: \[省略可\]次の呼び出し時に希望する文字コード。省略した場合はCharset。
- **Headline**: ヘッドラインの内容。<br />
  呼び出し時にOption: urlというふうに、Optionヘッダにurlが入っていた場合、URL拡張に対応しています。<br />
  その場合は、バイト値1区切りで、 内容\[1\]URL という形式で応答すると、ゴーストにURLも通知され、ゴースト側が対応していれば項目をクリックするとその詳細にジャンプ、等ができるかもしれません。<br />
  尚、返却するのはさくらスクリプトの断片ではなく、タグは使えません。単なるプレーンテキストを返却します。

## descript.txt

[Headline設定のページ](../descript/headline/index.md)を参照してください。

## SHIORI Event

いずれも詳細は[SHIORI Eventのページ](../list/shiori-event/index.md)を参照してください。

- **[OnHeadlinesenseBegin](../list/shiori-event/headline-rss/OnHeadlinesenseBegin.md)**: ヘッドラインセンス開始時。
- **[OnHeadlinesense.OnFind](../list/shiori-event/headline-rss/OnHeadlinesense.OnFind.md)**: 読みあげる内容があった時。
- **[OnHeadlinesenseComplete](../list/shiori-event/headline-rss/OnHeadlinesenseComplete.md)**: ヘッドラインセンス正常終了時。
- **[OnHeadlinesenseFailure](../list/shiori-event/headline-rss/OnHeadlinesenseFailure.md)**: ヘッドラインセンス失敗時。

## 補足

GET Headlineは2回呼ばれます。1回目は古いファイルに対して、2回目は新しいファイルに対してです。ただし古-\>新の順番は実装によっては順番が逆になる可能性がありますので、順番に依存するような処理は組んではいけません。

デバッグ中など、常に表示したい場合（no updateにならない）は、descript.txtにalwaysdisplay,1と書いてみてください（デバッグ終了後に必ず消す事）。
