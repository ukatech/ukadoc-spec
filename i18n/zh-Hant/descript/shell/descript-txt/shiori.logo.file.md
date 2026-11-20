# shiori.logo.file,檔案名稱

**カテゴリ:** descript.txt

用作 AI 圖表背景的影像檔案名稱。<br />
顯示多個圖表時，會讀取副檔名前加上數字的檔案。<br />
例如：指定 aigraph.png 時，讀取 aigraph0.png、aigraph1.png…<br />
影像大小為 288x288px 時會填滿圖表繪製區域。<br />
深色模式時，會使用檔名後方再加上 \_dark 的檔案。以上述例子來說即為 aigraph0_dark.png。若不存在，則固定顯示淺色模式。

也可寫在 ghost 側的 descript.txt。若 shell 側有指定，則優先使用 shell 側的值；否則使用 ghost 側的值。

**既定値:** ai.png（ai0.png、ai1.png…/ai0_dark.png、ai1_dark.png…），若不存在則使用 baseware 標準背景

**対応:** Materia 廢止規格 / SSP 多個指定自 2.4.26 起支援，深色模式自 2.8.56 起支援
