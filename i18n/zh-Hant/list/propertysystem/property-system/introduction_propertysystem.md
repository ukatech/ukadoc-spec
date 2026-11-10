# 屬性系統

## 概要

屬性系統是一種機制，可讓 ghost 端存取並讀寫 baseware 執行期間所保留的各種參數。

- [參考：CROW 測試項目資料](http://crow.aqrs.jp/devtest.html)

## 記述例

使用屬性系統有環境變數和一般標籤兩種方式。<br />
請同時參閱 SAKURA Script 和環境變數的屬性系統項目。

- **[%property\[屬性名稱\]](../../sakura-script/environment-variable/pct-property.md)**：將屬性作為環境變數參照，並嵌入其值。<br />
  用於只需直接顯示值的情況。<br />
  以下範例會將 baseware 的名稱和版本嵌入（顯示）在該處。

  ```
  %property[baseware.name] ver,%property[baseware.version]
  ```

- **[`\![get,property,事件名稱,屬性名稱]`](../../sakura-script/property-system-operation/bang-get-property.md)**：透過 Sakura Script 標籤觸發任意名稱的 SHIORI Event，並透過其 Reference 取得屬性。<br />
  用於希望 SHIORI 端根據屬性執行動作的情況。<br />
  以下範例會觸發 ID 為「OnGetSakuraName」的 SHIORI Event，並透過其 reference0 傳送 ghost「Emily/Phase4.5」的搭檔名稱（Teddy）。

  ```
  \![get,property,OnGetSakuraName,ghostlist(Emily/Phase4.5).keroname]
  ```

- **[`\![set,property,屬性名稱,值]`](../../sakura-script/property-system-operation/bang-set-property.md)**：透過 Sakura Script 標籤改寫屬性。<br />
  並非所有屬性都允許寫入；本頁項目中標示為*\[SET 有效\]*的項目可透過此方式操作。<br />
  以下範例會將 shell「ULTIMATE FORM」從 owner draw 選單的 shell 切換選單中隱藏。

  ```
  \![set,property,currentghost.shelllist(ULTIMATE FORM).menu,hidden]
  ```
