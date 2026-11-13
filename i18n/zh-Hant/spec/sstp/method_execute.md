# 方法：EXECUTE

使用EXECUTE方法，可以取得ghost的各種資訊，或執行不透過Sakura Script的各種指令。<br />
執行此方法時，ghost不會說話，但內部狀態可能會改變。

## EXECUTE範例

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## request專用標頭

- **Command または Command\[param1,param2...\]**: 要執行的指令。執行內容與回傳資訊將於後文說明。<br />
  從方括號起指定要傳給執行指令的參數。
- **Reference\* \[SSP\]**: 也可以使用Reference0起的標頭指定參數，代替方括號指定方式。

可在Command標頭指定的字串，以及response的「附加資料」回傳的結果，請參閱下文。

## 可在Command標頭指定的指令與回傳的附加資料

- **GetName**: 執行中的ghost的 (`\0`名稱),(`\1`名稱)，以逗號分隔
- **GetNames \[SSP\]**: 目前已安裝的`\0`名稱清單。以換行分隔，並以空行結尾。
- **GetFMO \[SSP 2.5.57\] \[遠端受限\]**: 取得與[FMO](../fmo-mutex/index.md)內容相同的資訊。<br />
  但僅限於透過SSTP通訊的應用程式內部管理的資訊，與同時執行的應用程式共用的原本FMO不同。<br />
  主要用於沒有視窗且無法傳送Direct SSTP的主控台應用程式等，僅透過Socket SSTP使用ReceiverGhostHWnd標頭，實現相當於Direct SSTP的功能。<br />
  以換行分隔，並以空行結尾。<br />
  若為遠端請求，各路徑資訊會被省略，標頭與hwnd會被替換為虛擬值。
- **GetGhostName \[SSP\]**: 執行中的ghost本體名稱（descript.txt的name）
- **GetShellName \[SSP\]**: 執行中的ghost目前使用的shell名稱
- **GetBalloonName \[SSP\]**: 執行中的ghost目前使用的balloon名稱
- **GetVersion**: baseware（執行中的軟體）的版本
- **GetGhostNameList \[SSP 2.6.53\]**: SSP所識別的所有ghost名稱（descript.txt的name）清單，以換行分隔
- **GetShellNameList \[SSP 2.6.53\]**: 執行中的ghost所識別的所有shell名稱（descript.txt的name）清單，以換行分隔
- **GetBalloonNameList \[SSP 2.6.53\]**: SSP所識別的所有balloon名稱（descript.txt的name）清單，以換行分隔
- **GetHeadlineNameList \[SSP 2.6.53\]**: SSP所識別的所有headline名稱（descript.txt的name）清單，以換行分隔
- **GetPluginNameList \[SSP 2.6.53\]**: SSP所識別的所有plugin名稱（descript.txt的name）清單，以換行分隔
- **GetGhostUUIDList \[SSP 2.9.35\]**: SSP所識別的所有ghost的[UUID](../../list/propertysystem/property-system/general-property/uuid.md)清單，以換行分隔。順序與GetGhostNameList相同。<br />
  **GetBalloonUUIDList \[SSP 2.9.35\]**: 所有balloon的UUID。順序與GetBalloonNameList相同。<br />
  **GetShellUUIDList \[SSP 2.9.35\]**: 執行中的ghost所識別的所有shell的UUID。順序與GetShellNameList相同。<br />
  UUID依照[metainfo-standard](https://github.com/ukatech/metainfo-standard)的程序，從descript.txt的值計算（與屬性系統的`uuid`相同）。
- **GetGhostMetaInfoList \[SSP 2.9.35\]**: SSP所識別的所有ghost的metainfo資料夾URL清單，以換行分隔。順序與GetGhostNameList相同。<br />
  **GetBalloonMetaInfoList \[SSP 2.9.35\]**: 所有balloon的metainfo資料夾URL。順序與GetBalloonNameList相同。<br />
  **GetShellMetaInfoList \[SSP 2.9.35\]**: 執行中的ghost所識別的所有shell的metainfo資料夾URL。順序與GetShellNameList相同。<br />
  使用descript.txt的[metainfo](../../descript/ghost/descript-txt/metainfo.md)值。若不存在，則使用從[githubrepo](../../descript/ghost/descript-txt/githubrepo.md)推導出的URL（預設分支視為`master`）。兩者皆不存在時為空行。
- **GetShortVersion \[SSP 2.6.53\]**: baseware（執行中的軟體）的版本（僅含以句點分隔的版本號碼）<br />
  與[version.json](https://ssp.shillest.net/archive/version.json)的ssp.full.version等直接比較，即可檢查是否為最新版本
- **GetStatus \[SSP 2.8.94\]**: 執行中的ghost目前的執行狀態。內容與SHIORI/3.0 request的Status標頭及屬性系統的[currentghost.status](../../list/propertysystem/property-system/currentghost.status.md)相同。<br />
  符合多個狀態時以逗號分隔。各值的意義請參閱[※SHIORI Status標頭](../../list/propertysystem/property-system/currentghost.status.md)。<br />
  不符合任何狀態時沒有附加資料（狀態碼200）
- **Quiet \[不可遠端使用\]**: 保持安靜，直到執行Restore或經過16秒。沒有附加資料（狀態碼為200系列表示成功）
- **Restore**: 解除Quiet。沒有附加資料（狀態碼為200系列表示成功）
- **CompressArchive \[SSP 2.7.23\] \[不可遠端使用\]**: 將指定資料夾內的檔案壓縮成ZIP檔案。壓縮目的地的副檔名若為`.7z`則使用7z格式，否則使用ZIP格式（即使指定`.lzh`或`.cab`，內容仍為ZIP）。不包含隱藏檔案與隱藏資料夾。<br />
  參數0：壓縮檔案名稱（以完整路徑指定，不可指定相對路徑）<br />
  參數1：要壓縮的資料夾完整路徑<br />
  參數2以後：選項（可省略）<br />
  選項如下。<br />
  --event=事件識別碼……指定事件識別碼後，回應後繼續壓縮，完成時觸發事件。識別碼以On開頭時，觸發該識別碼的事件；否則觸發OnCompressArchiveComplete或OnCompressArchiveFailure。省略時，直到處理完成才會回傳回應。<br />
  --password=密碼……使用指定密碼啟用AES加密ZIP。<br />
  執行後事件的規格請參閱[OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md)及[OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 從SAORI over DirectSSTP也可透過[internal_file的CompressArchive](../saori-ex/internal_file/internal_file.CompressArchive.md)呼叫（也可指定相對路徑或使用`/`分隔）。<br />
  \[SSP 2.9.33\] 參數1不是資料夾（例如檔案路徑）時，不會進行壓縮，並以400失敗（若指定了`--event=`，則以`invalid parameter`觸發失敗事件（OnCompressArchiveFailure或識別碼加上`Failure`））。在此之前，傳入檔案路徑會導致壓縮失敗（`file not found`）。<br />
  基於安全考量，壓縮目的地限於SSP管理的資料夾（ghost資料夾、balloon資料夾等在「資料夾」設定中指定的位置）之下。<br />
  此限制也可能視情況加強，因此限定在存放ghost自身資料的資料夾之下較為穩妥。<br />
  沒有附加資料（狀態碼為200系列表示成功）
- **ExtractArchive \[SSP 2.7.23\] \[不可遠端使用\]**: 解壓縮指定的封存檔。除ZIP外，也可解壓縮7z、tar等格式（支援的格式請參閱[internal_file的ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式)）。<br />
  參數0：壓縮檔案名稱（以完整路徑指定，不可指定相對路徑）<br />
  參數1：解壓縮目的地資料夾的完整路徑<br />
  參數2以後：選項（可省略）<br />
  選項如下。<br />
  --event=事件識別碼……指定事件識別碼後，回應後繼續解壓縮，完成時觸發事件。識別碼以On開頭時，觸發該識別碼的事件；否則觸發OnExtractArchiveComplete或OnExtractArchiveFailure。省略時，直到處理完成才會回傳回應。<br />
  --password=密碼……使用指定密碼解壓縮。\[SSP 2.9.26\] 不會顯示密碼輸入對話方塊。需要密碼但未指定或密碼錯誤時，不顯示對話方塊便失敗（回應為500，若指定了事件則觸發識別碼＋Failure或[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)）。\[SSP 2.9.25\]及之前的版本會忽略此選項並顯示對話方塊。<br />
  \[SSP 2.9.26\] 即使指定包含`..`的絕對路徑作為解壓縮目的地，若解析結果位於SSP管理的資料夾之外，仍會遭到拒絕（先前可解壓縮至管理範圍之外）。<br />
  執行後事件的規格請參閱[OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md)及[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 從SAORI over DirectSSTP也可透過[internal_file的ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md)呼叫（也可指定相對路徑或使用`/`分隔）。<br />
  基於安全考量，解壓縮目的地限於SSP管理的資料夾（ghost資料夾、balloon資料夾等在「資料夾」設定中指定的位置）之下。<br />
  此限制也可能視情況加強，因此限定在存放ghost自身資料的資料夾之下較為穩妥。<br />
  沒有附加資料（狀態碼為200系列表示成功）
- **DumpSurface \[SSP 2.5.98\] \[不可遠端使用\]**: 將合成後的surface圖片輸出至指定目錄。參數與[`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md)相同。<br />
  但無法指定事件ID，須依目錄、scope ID、surface清單、prefix、從零位置裁切、動畫ID \[SSP 2.9.05\] 的順序指定。<br />
  \[SSP 2.9.08\] 與Sakura Script版相同，也可以--dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation=的形式不依順序指定，並可與上述依順序指定的方式混用（不以--開頭的參數會依出現順序按上述順序分配）。除目錄外皆可省略，省略scope ID時為0。--event=會被忽略。<br />
  由於DumpSurface\[...\]格式的參數中無法寫入逗號，包含逗號的surface清單須以Reference0以後的標頭指定。<br />
  注意，直到處理完成才會回傳回應。<br />
  沒有附加資料（狀態碼為200系列表示成功）
- **MoveAsync \[SSP\] \[不可遠端使用\]**: 不透過Sakura Script執行與[`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md)相同的操作。參數指定方式與Sakura Script版相同。<br />
  由於無法在SSTP逾時前回傳response，且會造成死結，因此無法執行不帶async的move。<br />
  沒有附加資料（狀態碼為200系列表示成功）
- **SetTrayIcon \[SSP\] \[不可遠端使用\]**: 不透過Sakura Script執行與[`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md)相同的操作。參數指定方式與Sakura Script版相同。<br />
  沒有附加資料（狀態碼為200系列表示成功）
- **SetTrayBalloon \[SSP\] \[不可遠端使用\]**: 不透過Sakura Script執行與[`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md)相同的操作。參數指定方式與Sakura Script版相同。<br />
  沒有附加資料（狀態碼為200系列表示成功）
- **SetProperty \[SSP\] \[不可遠端使用\]**: 將值寫入[屬性系統](../../list/propertysystem/index.md)。<br />
  參數0：屬性名稱<br />
  參數1：要設定的值<br />
  沒有附加資料（狀態碼為200系列表示成功）
- **GetProperty \[SSP\]**: 從[屬性系統](../../list/propertysystem/index.md)讀取值。<br />
  參數0：屬性名稱<br />
  附加資料為取得的屬性值。
- **SetCookie**: 寫入依Sender指定的用戶端名稱分別保存的通用資料儲存區。<br />
  預期用法與瀏覽器的「Cookie」相同。<br />
  參數0：Cookie名稱<br />
  參數1：要設定的值<br />
  沒有附加資料（狀態碼為200系列表示成功）
- **GetCookie**: 從依Sender指定的用戶端名稱分別保存的通用資料儲存區讀取資料。<br />
  參數0：Cookie名稱<br />
  附加資料為取得的Cookie值。
