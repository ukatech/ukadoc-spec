# 方法：EXECUTE

透過 EXECUTE 方法，可以取得 ghost 的各種資訊，或執行不透過 Sakura Script 的各種命令。<br />
執行此方法時，ghost 不會說話，但內部狀態可能會被改寫。

## EXECUTE 範例

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## request 專用標頭

- **Command 或 Command\[param1,param2...\]**: 要執行的命令。執行內容與傳回的資訊如下所述。<br />
  方括號之後可指定要傳遞給命令的參數。
- **Reference\* \[SSP\]**: 也可以使用 Reference0～標頭指定參數，取代方括號指定方式。

可指定於 Command 標頭的字串，以及 response 的「附加資料」所傳回的結果，請參閱下文。

## 可指定於 Command 標頭的命令與傳回的附加資料

- **GetName**: 目前執行中的 ghost 的 (`\0`名稱),(`\1`名稱)，以逗號分隔
- **GetNames \[SSP\]**: 目前已安裝的`\0`名稱清單，以換行分隔。以空行結尾。
- **GetFMO \[SSP 2.5.57\] \[遠端使用受限\]**: 取得與 [FMO](../fmo-mutex/index.md) 內容相同的資訊。<br />
  但僅限於透過 SSTP 通訊的應用程式內部所管理的部分，與原本由同時執行中的應用程式群組共用的 FMO 不同。<br />
  主要用於沒有視窗、無法傳送 Direct SSTP 的主控台應用程式等，讓它們只透過 Socket SSTP 使用 ReceiverGhostHWnd 標頭，實現相當於 Direct SSTP 的功能。<br />
  以換行分隔，並以空行結尾。<br />
  若要求來自遠端，各路徑資訊會省略，標頭與 hwnd 則會替換為虛設值。
- **GetGhostName \[SSP\]**: 目前執行中的 ghost 本體名稱（descript.txt 的 name）
- **GetShellName \[SSP\]**: 目前執行中的 ghost 所使用的 shell 名稱
- **GetBalloonName \[SSP\]**: 目前執行中的 ghost 所使用的 balloon 名稱
- **GetVersion**: baseware（執行中的軟體）版本
- **GetGhostNameList \[SSP 2.6.53\]**: SSP 所識別的所有 ghost 名稱（descript.txt 的 name）清單，以換行分隔
- **GetShellNameList \[SSP 2.6.53\]**: 目前執行中的 ghost 所識別的所有 shell 名稱（descript.txt 的 name）清單，以換行分隔
- **GetBalloonNameList \[SSP 2.6.53\]**: SSP 所識別的所有 balloon 名稱（descript.txt 的 name）清單，以換行分隔
- **GetHeadlineNameList \[SSP 2.6.53\]**: SSP 所識別的所有 headline sensor 名稱（descript.txt 的 name）清單，以換行分隔
- **GetPluginNameList \[SSP 2.6.53\]**: SSP 所識別的所有 plugin 名稱（descript.txt 的 name）清單，以換行分隔
- **GetShortVersion \[SSP 2.6.53\]**: baseware（執行中的軟體）版本（僅包含以句點分隔的版本號）<br />
  與 [version.json](https://ssp.shillest.net/archive/version.json) 的 ssp.full.version 等項目進行簡單比較，即可檢查是否為最新版
- **GetStatus \[SSP 2.8.94\]**: 目前執行中的 ghost 狀態。內容與 SHIORI/3.0 request 的 Status 標頭，以及屬性系統的 [currentghost.status](../../list/propertysystem/property-system/currentghost.status.md) 相同。<br />
  符合多種狀態時，以逗號分隔。各值的意義請參閱[※SHIORI Status 標頭](../../list/propertysystem/property-system/currentghost.status.md)。<br />
  若不符合任何狀態，則沒有附加資料（狀態碼 200）
- **Quiet \[不可遠端使用\]**: 保持安靜，直到執行 Restore 或經過 16 秒為止。沒有附加資料（狀態碼為 200 番台即表示成功）
- **Restore**: 解除 Quiet。沒有附加資料（狀態碼為 200 番台即表示成功）
- **CompressArchive \[SSP 2.7.23\] \[不可遠端使用\]**: 將指定資料夾中的檔案壓縮成 ZIP 檔案。若壓縮目的地的副檔名是`.7z`，則使用 7z 格式；其他情況則使用 ZIP 格式（即使指定`.lzh`或`.cab`，內容仍是 ZIP）。不會包含隱藏檔案與隱藏資料夾。<br />
  參數0：壓縮檔名稱（以完整路徑指定，不可指定相對路徑）<br />
  參數1：要壓縮之資料夾的完整路徑<br />
  參數2 之後：選項（可省略）<br />
  選項如下。<br />
  --event=事件識別碼……指定事件識別碼時，會在 response 後繼續壓縮，完成後觸發事件。若識別碼以 On 開頭，則觸發該識別碼的事件；否則觸發 OnCompressArchiveComplete 或 OnCompressArchiveFailure。省略時，會等到處理完成才傳回 response。<br />
  --password=密碼……使用指定的密碼啟用 AES 加密 ZIP。<br />
  執行後的事件規格，請參閱 [OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md)・[OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 從 SAORI over DirectSSTP 呼叫時，也可使用 [internal_file 的 CompressArchive](../saori-ex/internal_file/internal_file.CompressArchive.md)（也可以指定相對路徑或使用`/`分隔）。<br />
  \[SSP 2.9.33\] 參數1不是資料夾（例如檔案路徑）時，不會進行壓縮，並以 400 失敗（若有指定`--event=`，則會以 `invalid parameter` 觸發失敗事件（OnCompressArchiveFailure，或在識別碼後加上`Failure`）。在此之前，傳入檔案路徑時會因壓縮失敗而回報 `file not found`。<br />
  基於安全性考量，壓縮目的地僅限於 SSP 管理的資料夾（ghost 資料夾、balloon 資料夾等由「資料夾」設定指定的位置）及其子資料夾。<br />
  此外，此限制可能會視需要加強，因此最好將目的地限制在存放 ghost 自身資料的資料夾及其子資料夾。<br />
  沒有附加資料（狀態碼為 200 番台即表示成功）
- **ExtractArchive \[SSP 2.7.23\] \[不可遠端使用\]**: 解壓縮指定的封存檔。除了 ZIP，也可以解壓縮 7z、tar 等格式（支援的格式請參閱 [internal_file 的 ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式)）。<br />
  參數0：壓縮檔名稱（以完整路徑指定，不可指定相對路徑）<br />
  參數1：解壓縮目的地資料夾的完整路徑<br />
  參數2 之後：選項（可省略）<br />
  選項如下。<br />
  --event=事件識別碼……指定事件識別碼時，會在 response 後繼續解壓縮，完成後觸發事件。若識別碼以 On 開頭，則觸發該識別碼的事件；否則觸發 OnExtractArchiveComplete 或 OnExtractArchiveFailure。省略時，會等到處理完成才傳回 response。<br />
  --password=密碼……使用指定的密碼解壓縮。\[SSP 2.9.26\] 不會顯示密碼輸入對話方塊。需要密碼但未指定密碼，或密碼錯誤時，不會顯示對話方塊並會失敗（response 為 500；若有指定事件，則會觸發識別碼＋Failure，或 [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)）。\[SSP 2.9.25\]以前會忽略此選項，並顯示對話方塊。<br />
  \[SSP 2.9.26\] 即使將包含`..`的絕對路徑指定為解壓縮目的地，若解析後的位置在 SSP 管理資料夾之外，仍會遭到拒絕（以前可以解壓縮至管理範圍之外）。<br />
  執行後的事件規格，請參閱 [OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md)・[OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)。<br />
  \[SSP 2.9.25\] 從 SAORI over DirectSSTP 呼叫時，也可使用 [internal_file 的 ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md)（也可以指定相對路徑或使用`/`分隔）。<br />
  基於安全性考量，解壓縮目的地僅限於 SSP 管理的資料夾（ghost 資料夾、balloon 資料夾等由「資料夾」設定指定的位置）及其子資料夾。<br />
  此外，此限制可能會視需要加強，因此最好將目的地限制在存放 ghost 自身資料的資料夾及其子資料夾。<br />
  沒有附加資料（狀態碼為 200 番台即表示成功）
- **DumpSurface \[SSP 2.5.98\] \[不可遠端使用\]**: 將合成後的 surface 圖片輸出至指定目錄。參數與[`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md)相同。<br />
  但不可指定事件 ID，並依序指定目錄、scope ID、surface 清單、prefix、從零位置裁切、動畫 ID \[SSP 2.9.05\]。<br />
  \[SSP 2.9.08\] 與 Sakura Script 版本相同，也可以使用 --dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation= 的格式，以任意順序指定；也可與上述順序指定方式混用（不以 -- 開頭的參數會依出現順序，按照上述順序分配）。除了目錄之外皆可省略；省略 scope ID 時會使用 0。--event= 會被忽略。<br />
  DumpSurface\[...\] 格式無法在參數中輸入逗號，因此含有逗號的 surface 清單請使用 Reference0 之後指定。<br />
  請注意，必須等到處理完成才會傳回 response。<br />
  沒有附加資料（狀態碼為 200 番台即表示成功）
- **MoveAsync \[SSP\] \[不可遠端使用\]**: 不透過 Sakura Script，執行與 [`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md)相同的操作。參數指定方式與 Sakura Script 版本相同。<br />
  由於無法在 SSTP 逾時前傳回 response，且可能造成死結，因此無法執行不含 async 的 move。<br />
  沒有附加資料（狀態碼為 200 番台即表示成功）
- **SetTrayIcon \[SSP\] \[不可遠端使用\]**: 不透過 Sakura Script，執行與 [`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md)相同的操作。參數指定方式與 Sakura Script 版本相同。<br />
  沒有附加資料（狀態碼為 200 番台即表示成功）
- **SetTrayBalloon \[SSP\] \[不可遠端使用\]**: 不透過 Sakura Script，執行與 [`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md)相同的操作。參數指定方式與 Sakura Script 版本相同。<br />
  沒有附加資料（狀態碼為 200 番台即表示成功）
- **SetProperty \[SSP\] \[不可遠端使用\]**: 將值寫入[屬性系統](../../list/propertysystem/index.md)。<br />
  參數0：屬性名稱<br />
  參數1：要設定的值<br />
  沒有附加資料（狀態碼為 200 番台即表示成功）
- **GetProperty \[SSP\]**: 從[屬性系統](../../list/propertysystem/index.md)讀取值。<br />
  參數0：屬性名稱<br />
  附加資料為取得的屬性值。
- **SetCookie**: 寫入依 Sender 指定的用戶端名稱分別儲存的通用資料區域。<br />
  預期用途與瀏覽器的「Cookie」相同。<br />
  參數0：Cookie 名稱<br />
  參數1：要設定的值<br />
  沒有附加資料（狀態碼為 200 番台即表示成功）
- **GetCookie**: 從依 Sender 指定的用戶端名稱分別儲存的通用資料區域讀取資料。<br />
  參數0：Cookie 名稱<br />
  附加資料為取得的 Cookie 值。
