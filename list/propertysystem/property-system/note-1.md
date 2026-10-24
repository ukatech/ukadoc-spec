# 補足

## ※SHIORI Statusヘッダ

複数がカンマ(,)区切りで返ったり、空が返る場合もある

- **talking**: 現在スクリプトを実行中（喋り中）。
- **passive**: passiveモード中（`\![enter,passivemode]`）。
- **induction**: inductionモード中（`\![enter,inductionmode]`）。
- **timecritical**: `\t`タグでロック中。
- **nouserbreak**: nouserbreakモード中（`\![enter,nouserbreak]`）。
- **online**: オンライン中（ヘッドラインデータ取得中や時刻あわせ中、自分自身のネットワーク更新中など）。
- **choosing**: `\q`、`\__q`タグによる選択肢表示中。
- **minimizing**: 最小化中（タスクトレイアイコン化中）。
- **opening(種類)**: 入力ウィンドウ展開中。<br />
  種類の部分にはcommunicate,input,teach,textarea,dialogのうち、開いている物がスラッシュ区切りで入る。<br />
  例：opening(input/dialog)<br />
  ※SSP 2.3.97よりスラッシュ。それ以前はカンマ区切り<br />
  ※textareaはSSP 2.9.10から
- **balloon(情報)**: バルーン表示中。<br />
  情報の部分には(キャラID)=(バルーンID)の形式で表示中のバルーンが列挙される。バルーンIDは左右の区別はない(常に偶数)。<br />
  例：balloon(0=2/1=0)<br />
  ※SSP 2.3.97よりスラッシュ。それ以前はカンマ区切り

※Statusヘッダは、SHIORI毎に以下のようにも取得出来ます。

- 華和梨……System.Request.Statusエントリ
- YAYA……status変数内
- 里々……情報取得変数（Status）
