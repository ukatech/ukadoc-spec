# DLL 通用規格

## DLL 通用規格

本規格定義 SHIORI、SAORI 及其他 伺か 系統所使用 DLL 模組的通用介面。

## 記憶體管理

所有引數／傳回值的傳遞都使用 Windows 的 Global Memory。具體處理步驟如下：

- baseware 使用 GlobalAlloc() 指定 GMEM_FIXED 旗標配置記憶體，並寫入資料
- 模組將收到的 HGLOBAL 轉型為 (char\*)，直接存取資料
- 模組參照 len 參數取得資料長度，並讀取所需資料
- 模組使用 GlobalFree() 釋放記憶體
- 傳回處理結果時，模組會以 GlobalAlloc() 重新配置指定 GMEM_FIXED 旗標的記憶體
- 模組將結果寫入配置的記憶體，並在 len 設定新的資料長度
- baseware 使用傳回的記憶體控制代碼後，以 GlobalFree() 釋放記憶體

注意事項：

- 使用 GMEM_FIXED 旗標時，不需要呼叫 GlobalLock()/GlobalUnlock()
- 將 HGLOBAL 轉型為 (char\*) 即可直接存取記憶體
- 無法保證傳入的記憶體以 NULL 結尾，因此務必參照 len 參數限制存取範圍
- 為確保程式運作穩健，不受 baseware 的實作方式影響，建議為傳回值配置比 len 多 1 個位元組的記憶體，並以零終止

## request 函數

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

所有要求都透過唯一的 request 函數提出。request 函數是 伺か 模組的主要介面，負責處理 baseware 傳來的所有要求。

要求資料的格式參考 HTTP 和 SSTP 標頭格式設計，並遵循以下規則：

- 所有行都以 CR+LF（0x0D, 0x0A）分隔
- 第 1 行記載命令名稱和通訊協定版本
- 第 2 行起可接續任意數量的標頭，格式為「標頭名稱: 值」
- 連續放置兩個 CR+LF（新增空行）表示標頭區段結束
- 字元編碼依照標頭指定的方式（通常為 UTF-8 或預設的 OEM codepage）

## 生命週期函數

DLL 載入和卸載時會呼叫以下函數。

### loadu 函數

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

初始化模組的函數。<br />
第 1 個引數的全域記憶體中會儲存模組目錄路徑，編碼為*UTF-8*。

此函數自 SSP 2.6.92 (2025/1/16) 起實作。在此之前僅實作 load。

處理內容範例：

- 將傳入的路徑設為目前目錄，並讀取所需的資料檔案
- 初始化模組運作所需的資源
- 視需要初始化記錄檔或資料庫

注意事項：

- 即使不需要字串資料，也務必釋放傳入的全域記憶體
- 初始化成功時傳回 TRUE，失敗時傳回 FALSE
- baseware 會優先使用此函數

#### load 函數

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

loadu 函數的舊版。<br />
除了第 1 個引數的模組目錄路徑使用預設 OEM codepage（日本語環境為 CP932）編碼之外，其規格與 loadu 函數相同。

注意事項：

- 若未實作 loadu 函數，則會使用此函數作為後援
- 為確保相容性，建議同時實作 load 和 loadu；若 loadu 已完成初始化後又呼叫 load，則忽略該呼叫
- 若要支援 Unicode，必須將收到的路徑適當轉換為寬字元字串

#### unload 函數

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

執行模組結束處理的函數。模組卸載時會由 baseware 呼叫。

應實作的處理：

- 釋放以 CreateFile 等函數開啟的檔案控制代碼
- 釋放以 CreateMutex 等函數建立的同步物件
- 等待以 CreateThread 等函數建立的執行緒結束，並進行後續處理
- 釋放模組配置的所有其他系統資源

目前不會使用傳回值，但為考量未來擴充性，建議傳回 TRUE。
