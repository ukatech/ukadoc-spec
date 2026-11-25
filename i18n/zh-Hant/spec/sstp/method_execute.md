# 方法：EXECUTE

使用 EXECUTE 方法，可以取得 ghost 的各種資訊，或執行不透過 Sakura Script 的各種命令。<br />
執行此方法時，ghost 不會說話，但內部狀態可能會改變。

## EXECUTE 範例

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## request 專屬標頭

- **Command 或 Command\[param1,param2...\]**: 要執行的命令。執行內容和傳回的資訊詳見下文。<br />
  在方括號中指定要傳給命令的參數。
- **Reference\* \[SSP\]**: 也可以不使用方括號，而以 Reference0 起的標頭指定參數。

關於 Command 標頭可指定的字串，以及 response 的「附加資料」中傳回的結果，請參閱下文。

## Command 標頭可指定的命令及傳回的附加資料

- **GetName**: 執行中 ghost 的（`\0`名稱）、（`\1`名稱），以逗號分隔
- **GetNames \[SSP\]**: 目前已安裝的 `\0` 名稱清單。以換行分隔，以空行結尾。
- **GetFMO \[SSP 2.5.57\] \[遠端限制\]**: 取得與 [FMO](../fmo-mutex/index.md) 內容相同的資訊。<br />
  但僅限於透過 SSTP 通訊的應用程式內部管理的部分，與同時執行的應用程式共用的原始 FMO 不同。<br />
  主要供沒有視窗、無法傳送 Direct SSTP 的主控台應用程式等使用，僅透過 Socket SSTP 利用 ReceiverGhostHWnd 標頭實現相當於 Direct SSTP 的功能。<br />
  以換行分隔，以空行結尾。<br />
  遠端要求時，各路徑資訊會被省略，標頭和 hwnd 會被替換為虛擬值。
- **GetGhostName \[SSP\]**: 執行中 ghost 本身的名稱（descript.txt 的 name）
- **GetShellName \[SSP\]**: 執行中 ghost 目前使用的 shell 名稱
- **GetBalloonName \[SSP\]**: 執行中 ghost 目前使用的 balloon 名稱
- **GetVersion**: baseware（執行中的軟體）的版本
- **GetGhostNameList \[SSP 2.6.53\]**: SSP 識別的所有 ghost 名稱（descript.txt 的 name）清單，以換行分隔
- **GetShellNameList \[SSP 2.6.53\]**: 執行中 ghost 識別的所有 shell 名稱（descript.txt 的 name）清單，以換行分隔
- **GetBalloonNameList \[SSP 2.6.53\]**: SSP 識別的所有 balloon 名稱（descript.txt 的 name）清單，以換行分隔
- **GetHeadlineNameList \[SSP 2.6.53\]**: SSP 識別的所有 headline 名稱（descript.txt 的 name）清單，以換行分隔
- **GetPluginNameList \[SSP 2.6.53\]**: SSP 識別的所有 plugin 名稱（descript.txt 的 name）清單，以換行分隔
- **GetGhostUUIDList \[SSP 2.9.35\]**: SSP 識別的所有 ghost 的 [UUID](../../list/propertysystem/property-system/general-property/uuid.md) 清單，以換行分隔。順序與 GetGhostNameList 相同。<br />
  **GetBalloonUUIDList \[SSP 2.9.35\]**: 所有 balloon 的 UUID。順序與 GetBalloonNameList 相同。<br />
  **GetShellUUIDList \[SSP 2.9.35\]**: 執行中 ghost 識別的所有 shell 的 UUID。順序與 GetShellNameList 相同。<br />
  UUID 依照 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 的程序，從 descript.txt 的值計算（與屬性系統的 `uuid` 相同）。
- **GetGhostMetaInfoList \[SSP 2.9.35\]**: SSP 識別的所有 ghost 的 metainfo 資料夾 URL 清單，以換行分隔。順序與 GetGhostNameList 相同。<br />
  **GetBalloonMetaInfoList \[SSP 2.9.35\]**: 所有 balloon 的 metainfo 資料夾 URL。順序與 GetBalloonNameList 相同。<br />
  **GetShellMetaInfoList \[SSP 2.9.35\]**: 執行中 ghost 識別的所有 shell 的 metainfo 資料夾 URL。順序與 GetShellNameList 相同。<br />
  使用 descript.txt 的 [metainfo](../../descript/ghost/descript-txt/metainfo.md) 值。若不存在，則使用從 [githubrepo](../../descript/ghost/descript-txt/githubrepo.md) 推導的 URL（預設分支視為 `master`）。兩者都不存在時為空行。
- **GetShortVersion \[SSP 2.6.53\]**: baseware（執行中的軟體）的版本（僅以句點分隔的版本號）<br />
  與 [version.json](https://ssp.shillest.net/archive/version.json) 的 ssp.full.version 等直接比較，即可檢查是否為最新版
- **GetStatus \[SSP 2.8.94\]**: 執行中 ghost 目前的執行狀態。內容與 SHIORI/3.0 request 的 Status 標頭及屬性系統的 [currentghost.status](../../list/propertysystem/property-system/currentghost.status.md) 相同。<br />
  符合多個狀態時以逗號分隔。各值的意義請參閱 [※SHIORI Status 標頭](../../list/propertysystem/property-system/currentghost.status.md)。<br />
  不符合任何狀態時沒有附加資料（狀態碼 200）<br />
  \[SSP 2.9.39\] EXECUTE 的 GetStatus 也包含 `scriptbusy`（有等待播放的腳本或正在播放）。`talking` 在佇列中腳本的間隔期間，以及接受腳本後至開始播放前會消失，但 `scriptbusy` 會保留。SEND 的回應在腳本加入佇列後傳回，因此緊接著讀取時一定能看到。SHIORI/3.0 request 的 Status 標頭和 `currentghost.status` 不包含此狀態（以免改變 ghost 端的判定）。
- **SetTimeShift \[SSP 2.9.39\] \[不可遠端使用\]**: 不透過 ghost 腳本，同步設定「虛擬變更目前時間」（時光機）的時間差。供測試依賴日期或時間的 ghost 使用。<br />
  參數 0：指定時間差。格式與 [`\![timemachine,set,値]`](../../list/sakura-script/misc/bang-timemachine-set-value.md) 的值相同（`+秒` / `-秒` / `0` / ISO8601 格式的日期時間）。不是加到目前的時間差，而是將時間差設為此值。<br />
  僅在以 `--allow-timemachine-control` 啟動 SSP 時接受。未加上時不執行任何動作，以 420 失敗，並在錯誤日誌中記錄警告。無法從遠端執行（420）。省略值或無法解析時以 400 失敗（時間差不變）。<br />
  成功時，在附加資料中傳回設定後的時間差（秒，帶符號整數）（狀態碼 200）。收到回應時時間差已生效，屬性 `system.os.timeshift` 也會傳回該值。時間差僅在本次執行期間有效，不會儲存至設定。
- **Quiet \[不可遠端使用\]**: 保持安靜，直到執行 Restore 或經過 16 秒。無附加資料（狀態碼為 200 系列時成功）
- **Restore**: 解除 Quiet。無附加資料（狀態碼為 200 系列時成功）
- **CompressArchive \[SSP 2.7.23\] \[不可遠端使用\]**: 將指定資料夾內的檔案壓縮成 ZIP 檔案。壓縮目的地的副檔名若為 `.7z`，則使用 7z 格式，否則使用 ZIP 格式（即使指定 `.lzh` 或 `.cab`，內容仍為 ZIP）。不包含隱藏檔案和隱藏資料夾。<br />
  參數 0：壓縮檔名（以完整路徑指定，不可指定相對路徑）<br />
  參數 1：要壓縮的資料夾完整路徑<br />
  參數 2 以後：選項（可省略）<br />
  選項如下。<br />
  --event=事件識別碼……指定事件識別碼後，會在回應後繼續壓縮，完成時觸發事件。識別碼以 On 開頭時觸發該識別碼的事件，否則觸發 OnCompressArchiveComplete 或 OnCompressArchiveFailure。省略時，處理完成前不會傳回回應。<br />
  --password=密碼……使用指定的密碼啟用 AES 加密 ZIP。<br />
  關於動作完成後的事件規格，請參閱 [OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md)・[OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 從 SAORI over DirectSSTP 也可透過 [internal_file 的 CompressArchive](../saori-ex/internal_file/internal_file.CompressArchive.md) 呼叫（也可指定相對路徑或以 `/` 分隔）。<br />
  \[SSP 2.9.33\] 參數 1 不是資料夾（例如檔案路徑）時，不會壓縮並以 400 失敗（若指定了 `--event=`，會以 `invalid parameter` 觸發失敗事件（OnCompressArchiveFailure 或在識別碼後加上 `Failure` 的事件））。在此之前，傳入檔案路徑會導致壓縮失敗（`file not found`）。<br />
  基於安全考量，壓縮目的地僅限 SSP 管理的資料夾（ghost 資料夾、balloon 資料夾等在「資料夾」設定中指定的位置）及其下層。<br />
  此限制也可能視需要加強，因此以限制在存放 ghost 自身資料的資料夾及其下層較為穩妥。<br />
  無附加資料（狀態碼為 200 系列時成功）
- **ExtractArchive \[SSP 2.7.23\] \[不可遠端使用\]**: 解壓縮指定的壓縮檔。除了 ZIP，也可解壓縮 7z、tar 等格式（支援的格式請參閱 [internal_file 的 ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式)）。<br />
  參數 0：壓縮檔名（以完整路徑指定，不可指定相對路徑）<br />
  參數 1：解壓縮目的地資料夾的完整路徑<br />
  參數 2 以後：選項（可省略）<br />
  選項如下。<br />
  --event=事件識別碼……指定事件識別碼後，會在回應後繼續解壓縮，完成時觸發事件。識別碼以 On 開頭時觸發該識別碼的事件，否則觸發 OnExtractArchiveComplete 或 OnExtractArchiveFailure。省略時，處理完成前不會傳回回應。<br />
  --password=密碼……使用指定的密碼解壓縮。\[SSP 2.9.26\] 不會顯示密碼輸入對話框。需要密碼但未指定或密碼錯誤時，不顯示對話框而直接失敗（回應為 500；若指定了事件，則觸發識別碼＋Failure 或 [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)）。\[SSP 2.9.25\] 以前會忽略此選項並顯示對話框。<br />
  \[SSP 2.9.26\] 即使將包含 `..` 的絕對路徑指定為解壓縮目的地，若解析結果位於 SSP 管理的資料夾之外，也會被拒絕（以前可解壓縮至管理範圍之外）。<br />
  關於動作完成後的事件規格，請參閱 [OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md)・[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 從 SAORI over DirectSSTP 也可透過 [internal_file 的 ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md) 呼叫（也可指定相對路徑或以 `/` 分隔）。<br />
  基於安全考量，解壓縮目的地僅限 SSP 管理的資料夾（ghost 資料夾、balloon 資料夾等在「資料夾」設定中指定的位置）及其下層。<br />
  此限制也可能視需要加強，因此以限制在存放 ghost 自身資料的資料夾及其下層較為穩妥。<br />
  無附加資料（狀態碼為 200 系列時成功）
- **DumpSurface \[SSP 2.5.98\] \[不可遠端使用\]**: 將合成後的 surface 圖片輸出至指定目錄。參數與 [`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md) 相同。<br />
  但無法指定事件 ID，須依序指定目錄、scope ID、surface 清單、prefix、從零位置裁切、動畫 ID \[SSP 2.9.05\]。<br />
  \[SSP 2.9.08\] 與 Sakura Script 版相同，也可使用 --dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation= 格式，不限順序指定，也可與上述依順序指定的方式混用（不以 -- 開頭的參數會依出現順序按上述順序分配）。除了目錄以外皆可省略，省略 scope ID 時為 0。--event= 會被忽略。<br />
  由於 DumpSurface\[...\] 格式的參數中不能寫入逗號，包含逗號的 surface 清單須以 Reference0 以後的標頭指定。<br />
  請注意，處理完成前不會傳回回應。<br />
  無附加資料（狀態碼為 200 系列時成功）
- **MoveAsync \[SSP\] \[不可遠端使用\]**: 不透過 Sakura Script，執行與 [`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md) 相同的動作。參數指定方式與 Sakura Script 版相同。<br />
  由於無法在 SSTP 逾時前傳回 response，且會造成死結，因此無法執行沒有 async 的 move。<br />
  無附加資料（狀態碼為 200 系列時成功）
- **SetTrayIcon \[SSP\] \[不可遠端使用\]**: 不透過 Sakura Script，執行與 [`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md) 相同的動作。參數指定方式與 Sakura Script 版相同。<br />
  無附加資料（狀態碼為 200 系列時成功）
- **SetTrayBalloon \[SSP\] \[不可遠端使用\]**: 不透過 Sakura Script，執行與 [`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md) 相同的動作。參數指定方式與 Sakura Script 版相同。<br />
  無附加資料（狀態碼為 200 系列時成功）
- **SetProperty \[SSP\] \[不可遠端使用\]**: 將值寫入[屬性系統](../../list/propertysystem/index.md)。<br />
  參數 0：屬性名稱<br />
  參數 1：要設定的值<br />
  無附加資料（狀態碼為 200 系列時成功）
- **GetProperty \[SSP\]**: 從[屬性系統](../../list/propertysystem/index.md)讀取值。<br />
  參數 0：屬性名稱<br />
  附加資料為取得的屬性值。
- **SetCookie**: 寫入依 Sender 指定的用戶端名稱分別儲存的通用資料儲存區。<br />
  預期用法與瀏覽器的「Cookie」相同。<br />
  參數 0：Cookie 名稱<br />
  參數 1：要設定的值<br />
  無附加資料（狀態碼為 200 系列時成功）
- **GetCookie**: 從依 Sender 指定的用戶端名稱分別儲存的通用資料儲存區讀取資料。<br />
  參數 0：Cookie 名稱<br />
  附加資料為取得的 Cookie 值。
