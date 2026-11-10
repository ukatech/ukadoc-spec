# animation\*.pattern\*,繪製方法,サーフェス編號,權重,X座標,Y座標（,選項...）

**カテゴリ:** surface brace

動畫各影格的定義。一般而言，各影格會重設先前的影格，再與 base surface 合成後繪製（嚴格來說，取決於繪製方法）。<br />
animation 後方的 \* 部分是 animationID（與 animation\*.interval 的 \* 相同）。<br />
pattern 後方的 \* 部分（pattern ID），是一系列 animation\*.pattern 定義中從 0 開始的連續編號。Materia 的上限為 127。編號較小的項目會先繪製，並依序疊加。<br />
繪製方法請參照下列[繪製方法](h-drowmethod/index.md)。<br />
權重是繪製該影格*之前*的等待時間，單位為毫秒。僅限 SSP，也可以用減號分隔「最小權重-最大權重」；此時會在最小值至最大值之間隨機選取。<br />
X 座標、Y 座標用來指定該影格相對於 base（截至該影格為止的繪製結果）的位移量。<br />
サーフェス編號設為 -1 可停止該動畫，設為 -2 則可停止目前正在執行的所有其他動畫。兩種情況下都會忽略繪製方法、X 座標和 Y 座標。<br />
サーフェス編號也可指定 name 定義中指定的 ID 以外的別名。（SSP 2.8.25～）<br />
[舊定義](caption_seriko-redefine.md)：\*pattern\*,サーフェスID,權重,繪製方法,X座標,Y座標

選項如下。若要指定多個選項，可像「animation0.pattern0,overlay,101,700,0,0,--alpha,128,--option2,...」一樣接續記述。

- **--alpha,值(0-255)**: \[SSP 2.8.37～\]指定繪製時的不透明度。0 為完全透明，255 為完全不透明。<br />
  例：animation0.pattern0,overlay,101,700,0,0,--alpha,128

**既定値:** 無動作

**対応:** Materia / SSP / CROW
