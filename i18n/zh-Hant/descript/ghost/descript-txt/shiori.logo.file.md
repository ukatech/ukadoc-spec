# shiori.logo.file,檔案名稱

**カテゴリ:** descript.txt

指定用於 AI 圖表背景的圖片檔案名稱。<br />
顯示多個圖表時，會載入在副檔名前加上數字的檔案。<br />
例：指定aigraph.png時，會載入aigraph0.png、aigraph1.png…<br />
圖片尺寸為288x288px，會填滿圖表繪製區域。<br />
深色模式時會使用檔名後加上\_dark的檔案。以上例而言，即為aigraph0_dark.png。若檔案不存在，則固定顯示淺色模式。

**既定値:** ai.png（ai0.png、ai1.png…/ai0_dark.png、ai1_dark.png…），若不存在則使用 baseware 標準背景

**対応:** Materia 廢止規格 / SSP 多檔指定自2.4.26起支援，深色模式自2.8.56起支援
