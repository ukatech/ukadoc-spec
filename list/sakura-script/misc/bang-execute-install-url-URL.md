# `\![execute,install,url,URL,種別]`

**カテゴリ:** 未分類コマンド

指定したURLのファイルをダウンロードし、種別に応じたインストール／登録処理を行う。<br />
ファイルのダウンロードを一時ファイル用フォルダ内に自動的に行い、適宜インストール処理を行う。<br />
このタグで実行されたダウンロード処理については、OnURLQueryは発生しない。

種別は省略可能。省略した場合はContent-Typeとファイルの中身から自動判別される。

- nar……narファイルとしてインストールする
- feed……[ヘッドラインセンサ](../../../descript/install/install-txt/type.md)(RSSFeed)として登録する
- homeurl……そのURLをhomeurlとみなしてネットワーク更新を実行する
- ical……iCal(.ics)を購読する[スケジュールセンサ](../../../descript/install/install-txt/type.md)として登録する。カレンダー用フォルダ内にdescript.txtが自動生成され、以後カレンダーの表示や[OnScheduleTodayNotify](../../shiori-event/calendar/OnScheduleTodayNotify.md)の対象になる
- ssf……SSFファイルとして取得し、トークを再生する

**対応:** SSP

## 記述例

```sakurascript
\![execute,install,url,http://ssp.shillest.net/ghost/emily4.nar,nar]Emily/Phase4.5のnarをダウンロードしてきてインストールする。
```
