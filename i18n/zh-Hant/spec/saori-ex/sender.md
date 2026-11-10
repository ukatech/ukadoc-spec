# 傳送端的步驟

SHIORI 等傳送端會依照下列步驟使用 SAORI over DirectSSTP。

1. 從[FMO](../fmo-mutex/index.md)等處取得自己 ghost 的視窗（`hwnd`）。
2. 準備接收回應的視窗。
3. 組成 SAORI/1.0 要求，並附上`Module`和`HWnd`（接收回應的視窗）。
4. 使用 SendMessage 類函式，將`WM_COPYDATA`（`dwData = 9801`）傳送至 ghost 的視窗。
5. 將送達接收視窗的`WM_COPYDATA`（`dwData = 9801`）中，以`SAORI/`開頭的資料讀取為回應。

請先透過[GET Version](directsstp.md)確認功能是否可用。

## 記述例

在 YAYA 和里々中，上述步驟會由 SHIORI 本身執行。寫法與 DLL 的 SAORI 相同，只需將模組名稱改為以`internal_`開頭的名稱即可。關於無法使用時（例如舊版 SSP）的處理方式，請參閱各 SHIORI 的說明。

- **YAYA（`FUNCTIONEX`）**:

  ```
  // 同期
  _hash = FUNCTIONEX('internal_crypto', 'Digest', 'sha256', 'abc')

  // 非同期：結果は OnHashDone に届く（reference[0]=識別子、reference[1]=結果）
  FUNCTIONEX('internal_crypto', 'HashPassword', 'secret', '--async=OnHashDone')
  OnHashDone
  {
  	_phc = reference[1]
  }
  ```

- **里々（登録は不要で、モジュール名をそのまま`（）`で呼ぶ）**:

  ```
  ＊OnBoot
  　（internal_crypto、Digest、sha256、abc）
  　（internal_crypto、HashPassword、secret、--async=OnHashDone）

  ＊OnHashDone
  　（Ｒ１）
  ```

結果會作為`Result`處理，其他值則從`Value0`開始處理，這點與 DLL 的 SAORI 相同。附加`--async`的呼叫，其傳回值會是空值。
