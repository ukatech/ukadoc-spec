# 相容模組

SSP內建了以下常用SAORI DLL的相容功能。ghost載入這些DLL時，SSP不會讀取DLL，而會替換成內建功能（依檔名判定）。<br />
\[SSP 2.9.13\] 也可以透過Direct SSTP呼叫這些模組，名稱為去掉DLL名稱中`.dll`的部分（例如`Module: string`）。引數和回傳值與原始SAORI相同。

`houchi` `clipcopy` `textcopy` `saori_ip` `saori_cpuid` `mciaudio` `cpuusage` `httpc` `string` `hanayu` `osuwari`（`osuwari`適用於 \[SSP 2.9.33\]）

- Direct SSTP沒有`load` / `unload`，因此會為每個ghost準備各自狀態的模組（`mciaudio` / `httpc` / `string` / `hanayu`），並在該ghost第一次呼叫時建立，於ghost結束時（包括重新載入SHIORI）捨棄。這些模組不會與以DLL方式載入的模組共用狀態。
- 沒有ghost時呼叫，依賴ghost的處理（`httpc`的取得、儲存和`bg`、`hanayu`的`show`、`mciaudio`的`load` / `play` / `loop` / `stop`）會回傳400（`ghost required`）。
- `houchi`會在載入時執行，因此從Direct SSTP呼叫也不會有任何作用。
- Direct SSTP的要求會在SSP主執行緒中處理，因此請使用`bg`執行`httpc`的取得（若未加上，取得期間SSP畫面會停止回應）。

## osuwari \[SSP 2.9.33\]

相容於ukiya氏的`Osuwari.dll`。讓ghost視窗追蹤前景視窗、指定的視窗或畫面矩形（與[`\![set,alignmenttodesktop,osuwari,…]`](../../list/sakura-script/surface/bang-set-alignmenttodesktop.note.md)的處理相同，選項的意義也記載於該處）。引數與原始版本相同，採用位置引數。

- `START`: 依序從`Argument1`開始指定控制目標的HWND / 追蹤目標（`ACTIVE` `FIX` `@標題` `#控制代碼`） / 原點（`TL` `TR` `BL` `BR`） / x偏移 / y偏移 / 更新間隔（毫秒。0代表100） / (可省略)選項（以空格分隔的`XMOVE` `YMOVE` `NOCLIP` `BACK`。`BACK`會將視窗放在目標視窗正後方。原始版本沒有此選項） / (可省略)無法就座時的指定（以空格分隔的`DESKTOP` `WORKAREA`，以及`CENTER` `LEFT` `RIGHT` `TOP` `BOTTOM`） / (可省略)裁切邊界（`左_上_右_下`）。
  - 省略第7個及之後的引數時，會沿用前一次`START`的值。行為與原始版本相同。`\![set,alignmenttodesktop,osuwari,…]`則會在每次省略選項時使用預設值（不會沿用）。
  - 控制目標的HWND只能指定由`OnHWND`事件（`hwnd`）通知的**該ghost角色的視窗**。不會移動其他視窗（找不到時回傳500）。
- `STOP`: 停止由SAORI設定的就座，並將對齊方式還原為ghost與shell的預設值（`descript.txt`）。若`descript.txt`的預設值是osuwari，則會重新就座至osuwari。透過`\![set,alignmenttodesktop,osuwari,…]`設定的項目不會停止。卸載SAORI（包括重新載入SHIORI）時也會停止。
- 成功時回傳204；引數不足或無法解析時回傳400；找不到控制目標HWND時回傳500（`source window is not exist`）。
- 與原始版本的差異如下。
  - 視窗矩形會依外觀邊框測量。
  - 基準畫面是目標視窗所在的螢幕（裁切判定會以所有螢幕合併後的區域為準）。
  - 沒有原始版本指定`DESKTOP`時`side`永遠為`TOP`的問題。
  - 不會就座於最小化或隱藏的視窗。
  - 不需要在shell的`descript.txt`中寫入`seriko.alignmenttodesktop,free`。
- 改名後的DLL（例如`osuwari0.dll`）不屬於相容範圍，會載入真正的DLL。
