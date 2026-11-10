# element\*,繪製方法,檔名,X座標,Y座標(,選項...)

**カテゴリ:** surface brace

合成基礎surface。<br />
將多張圖像合成，並將合成結果作為基礎surface，視為一張圖像的機制。<br />
若存在對應該surface的surface\*.png圖像，且已定義element0，則原本surface\*.png的內容會被丟棄，並以element0取代<br />
element1以後會依序合成在其上方。<br />
\*的部分（elementID）是從0開始，在同一個surface內連續使用的流水號。<br />
繪製方法請參閱下方的[繪製方法](h-drowmethod/index.md)。<br />
若在surface\*.png或element定義中指定動畫GIF/APNG/WebP動畫，即使未撰寫SERIKO定義也會自動播放動畫(SSP 2.7.38～)。<br />
將以element定義的surface用作動畫部件時，也會如同一張圖像般運作(SSP 2.3.53～。在此之前未定義)。

選項如下。若要指定多個選項，可以像「element0,overlay,face.png,0,0,--clipping,10,10,50,50,--alpha,128」這樣接續撰寫。

- **--clipping,左,上,右,下**: \[SSP 2.8.15～\]只繪製左、上、右、下所指定的矩形區域。使用此選項會停用動畫載入。<br />
  例：element0,overlay,face.png,0,0,--clipping,10,10,50,50
- **--alpha,值(0-255)**: \[SSP 2.8.37～\]指定繪製時的不透明度。0為完全透明，255為完全不透明。<br />
  例：element0,overlay,face.png,0,0,--alpha,128
- **--source,值**: \[SSP 2.8.41～\]從具有多個繪製候選項目的圖像或檔案中，指定實際用於繪製的項目。<br />
  多頁TIFF時指定從0開始的頁碼；DLL/EXE內的圖示時指定從0開始的資源編號；PSD等檔案則指定圖層名稱。<br />
  指定圖層群組中的圖層時，請以::分隔並寫入群組名稱（支援群組巢狀）。<br />
  僅限PSD等圖層資訊包含繪製方法資訊的格式，才能將繪製方法指定為auto。<br />
  PSD等檔案中指定的圖層若設定了不透明度，且未指定alpha選項，則會自動使用圖層的不透明度資訊。<br />
  例：element0,auto,face.png,0,0,--source,顔::頭
- **--scaling,橫向,縱向**: \[SSP 2.8.73～\]將圖像縮放至指定尺寸後合成。與clipping併用時，會縮放裁切後的範圍。<br />
  橫向與縱向的數值若在末尾加上%，會視為相對於（clipping後）原始圖像的百分比；若省略單位或在末尾加上px，則會視為像素數。<br />
  將數值設為負數時，會以其絕對值作為尺寸，並左右或上下翻轉顯示。<br />
  \[SSP 2.8.82～\]若將橫向或縱向其中一項設為0，則會依照非0項的尺寸，在保持原圖長寬比的情況下縮放。<br />
  可指定的尺寸限制在1～4096px之間。<br />
  例：element0,overlay,face.png,0,0,--scaling,50%,50%<br />
  例：element0,overlay,face.png,0,0,--scaling,150,0（若原圖為300x200，則會變成150x100）
- **--scaling,尺寸,基準邊**: \[SSP 2.8.82～\]在保持原圖長寬比的情況下縮放並合成，使基準邊符合指定尺寸。尺寸只能使用像素數，不能使用%。<br />
  基準邊可指定long（長邊）或short（短邊）。<br />
  在基準邊末尾加上max時只會縮小（小於指定尺寸的圖像不會放大）；加上min時只會放大（大於指定尺寸的圖像不會縮小）。<br />
  若省略long・short，只寫max或min，則會視為指定long。<br />
  將尺寸設為負數時，會以其絕對值作為尺寸，並同時左右及上下翻轉顯示。<br />
  可指定的尺寸限制在1～4096px之間。<br />
  例：element0,overlay,face.png,0,0,--scaling,300,long（若原圖為400x300，則會變成300x225）<br />
  例：element0,overlay,face.png,0,0,--scaling,300,longmax（僅在長邊超過300px時縮小至300px）<br />
  例：element0,overlay,face.png,0,0,--scaling,300,shortmin（僅在短邊小於300px時放大至300px）

**既定値:** 無作用

**対応:** Materia / SSP / CROW
