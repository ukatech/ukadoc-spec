# shiori.logo.file,ファイル名

**カテゴリ:** descript.txt

AIグラフ背景に使用する画像ファイル名。<br />
複数グラフ表示の場合は拡張子の前に数字をつけたものを読み込む。<br />
例：aigraph.pngと指定した場合、aigraph0.png、aigraph1.png…<br />
画像サイズは288x288pxでグラフ描画面一杯になる。<br />
ダークモード時はさらに後ろに\_darkがついたファイル名のものが使われる。上記の例であればaigraph0_dark.png。ない時はライトモード固定表示。

**既定値:** ai.png（ai0.png、ai1.png…/ai0_dark.png、ai1_dark.png…）、なければベースウェア標準背景

**対応:** Materia廃止仕様 / SSP 複数指定は2.4.26～ ダークモードは2.8.56～
