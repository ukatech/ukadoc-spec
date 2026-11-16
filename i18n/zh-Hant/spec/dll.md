# DLL 共通規格

## DLL 共通規格

本規格定義 SHIORI、SAORI 及其他伺か (Ukagaka) 系統所使用的 DLL 模組之共通介面。

## 記憶體管理

所有引數與回傳值的傳遞均使用 Windows 的 Global Memory。具體處理步驟如下：

- baseware 使用 GlobalAlloc() 指定 GMEM_FIXED 旗標配置記憶體，並寫入資料
- 模組將收到的 HGLOBAL 轉型為 (char\*)，直接存取資料
- 模組參照 len 參數取得資料長度，並讀取所需資料
- 模組使用 GlobalFree() 釋放記憶體
- 回傳處理結果時，模組重新使用 GlobalAlloc() 指定 GMEM_FIXED 配置記憶體
- 模組將結果寫入配置的記憶體，並將新的資料長度設定至 len
- baseware 使用回傳的記憶體控制代碼後，以 GlobalFree() 釋放記憶體

注意事項：

- 使用 GMEM_FIXED 旗標時，不需要 GlobalLock()/GlobalUnlock()
- 將 HGLOBAL 轉型為 (char\*) 即可直接存取記憶體
- 傳入的記憶體不保證以 NULL 結尾，因此必須參照 len 參數限制存取範圍
- 為確保不受 baseware 實作方式影響且能穩健運作，建議回傳值用的記憶體比 len 多配置 1 位元組，並以零結尾

## request 函式

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

所有請求都透過唯一的 request 函式進行。request 函式是伺か (Ukagaka) 模組的主要介面，處理來自 baseware 的所有要求。

請求資料的格式參考 HTTP 和 SSTP 的標頭格式設計，遵循以下規則：

- 所有行均以 CR+LF（0x0D, 0x0A）分隔
- 第 1 行記載指令名稱與協定版本
- 第 2 行之後接任意數量的標頭，格式為「標頭名稱: 值」
- 連續放置兩組 CR+LF（加入空行）表示標頭區段結束
- 字元編碼依照標頭指定的方式（通常為 UTF-8 或預設的 OEM codepage）

## 生命週期函式

載入及卸載 DLL 時會呼叫以下函式。

### loadu 函式

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

用於初始化模組的函式。<br />
第 1 個引數的全域記憶體中，以 *UTF-8 編碼*儲存模組的目錄路徑。

自 SSP 2.6.92 (2025/1/16) 起實作。在此之前僅實作 load。

處理內容範例：

- 以傳入的路徑作為目前目錄，讀取所需的資料檔案
- 初始化模組運作所需的資源
- 視需要初始化記錄檔或資料庫

注意事項：

- 即使不需要字串資料，也必須釋放傳入的全域記憶體
- 初始化成功時回傳 TRUE，失敗時回傳 FALSE
- baseware 會優先使用此函式

#### load 函式

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

loadu 函式的舊版。<br />
除了第 1 個引數的模組目錄路徑以預設的 OEM codepage（日文環境中為 CP932）編碼外，規格與 loadu 函式相同。

注意事項：

- 當未實作 loadu 函式時，作為備援使用
- 為確保相容性，建議同時實作 load 和 loadu，並在已透過 loadu 初始化後又呼叫 load 時忽略該呼叫
- 為支援 Unicode，需要將收到的路徑適當轉換為寬字元字串

#### unload 函式

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

用於執行模組結束處理的函式。模組卸載時由 baseware 呼叫。

應實作的處理：

- 釋放以 CreateFile 等開啟的檔案控制代碼
- 釋放以 CreateMutex 等建立的同步物件
- 等待以 CreateThread 等建立的執行緒結束，並執行後續處理
- 此外，釋放模組配置的所有系統資源

目前不使用回傳值，但考量未來擴充性，建議回傳 TRUE。

## 多實例用函式（選用）

`load` / `request` / `unload` 對每個 DLL 只能持有一個實例。為了讓 baseware 能在同一個程序中從同一個 DLL 建立多個實例，可以**選擇性地**實作以下以 id 區分實例的函式。即使不實作，仍可作為模組運作，且在不呼叫這些函式的 baseware 中也能如以往一樣運作。

```
extern "C" __declspec(dllexport) long __cdecl multi_loadu(HGLOBAL h, long len);
extern "C" __declspec(dllexport) long __cdecl multi_load(HGLOBAL h, long len);
extern "C" __declspec(dllexport) BOOL __cdecl multi_unload(long id);
extern "C" __declspec(dllexport) HGLOBAL __cdecl multi_request(long id, HGLOBAL h, long *len);
```

- **multi_loadu / multi_load**: 使用與 `loadu` / `load` 相同的引數建立新實例。模組目錄路徑的字元編碼也分別與 `loadu`（UTF-8）及 `load`（預設的 OEM codepage）相同。回傳值是指向該實例的 id（1 以上的整數）。記憶體也與 `loadu` / `load` 一樣由模組釋放
- **multi_unload**: 結束 id 指定的實例。成功時回傳 TRUE，id 不存在時回傳 FALSE
- **multi_request**: 將與 `request` 格式相同的請求傳給 id 指定的實例。id 不存在時回傳 NULL

注意事項：

- id 0 分配給由舊有 `load` / `request` / `unload` 處理的實例。`multi_load*` 不得回傳 0
- 舊有函式與多實例用函式可以同時實作於同一個 DLL 中。兩者的實例視為不同實例
- 未規定 `multi_load*` 失敗時的回傳值（YAYA 一律回傳 id）
- SSP 不使用這些函式（此規格供 SSP 以外的 baseware 使用）

## YAYA 專屬函式

以下函式由 YAYA（`yaya.dll`）自行實作，用於與除錯用檢查工具連動，不包含在 SHIORI 規格中。其他模組無須實作，baseware 也無須呼叫。

!!! note "註"
    規格可能因 YAYA 的需求而變更。帶有 `multi_` 的函式與前節的多實例用函式相同，會作用於 id 指定的實例。

### CI_check_failed 函式

```
extern "C" __declspec(dllexport) BOOL __cdecl CI_check_failed(void);
extern "C" __declspec(dllexport) BOOL __cdecl multi_CI_check_failed(long id);
```

字典載入失敗而處於停止運作的狀態，或進入緊急模式時回傳 TRUE。id 不存在（`multi_` 版）或呼叫 `load` 之前回傳 FALSE。

### Set_loghandler 函式

```
extern "C" __declspec(dllexport) void __cdecl Set_loghandler(void (*loghandler)(const wchar_t *str, int mode, int id));
extern "C" __declspec(dllexport) void __cdecl multi_Set_loghandler(long id, void (*loghandler)(const wchar_t *str, int mode, int id));
```

註冊接收 YAYA 記錄的回呼函式。註冊後即啟用記錄輸出。`multi_` 版只能註冊至透過 `multi_load*` 建立後的實例，id 不存在時不執行任何動作。

回呼函式的引數如下。

- **str**: 記錄字串（UTF-16）。`mode` 為控制用的值時為空字串
- **mode**: 記錄的種類或控制值
- **id**: 記錄的訊息編號（不是實例的 id）

`mode` 的值如下。

- **0**: 資訊
- **1**: 致命錯誤
- **2**: 錯誤
- **3**: 警告
- **4**: 註記
- **6**: 記錄結束
- **16 / 17 / 32**: 通知後續記錄中多位元組字元的字元編碼。16 為 Shift_JIS、17 為 UTF-8、32 為 OS 的預設值。於記錄開始時呼叫 1 次

回呼函式會在呼叫 `load` / `request` / `unload` 的執行緒中執行。

### logsend 函式

```
extern "C" __declspec(dllexport) BOOL __cdecl logsend(long hwnd);
```

僅 Windows 的 DLL 版提供此函式。傳入透過 `WM_COPYDATA` 接收記錄的視窗控制代碼（HWND）。一律回傳 TRUE。若已透過 `Set_loghandler` 註冊回呼函式，則優先使用該回呼函式。

`WM_COPYDATA` 的 `dwData` 包含與 `Set_loghandler` 的 `mode` 相同的值，`lpData` 包含記錄字串（UTF-16、NUL 結尾）。
