# SAORI over DirectSSTP

## 傳送方式

與 [Direct SSTP](../sstp/direct.md) 相同，使用 `WM_COPYDATA`（`dwData = 9801`），在 `lpData` 中放入 SAORI/1.0 請求而非 SSTP 請求，並傳送至自己的 ghost 視窗（[FMO](../fmo-mutex/index.md) 的 `hwnd`）。<br />
視窗及 `WM_COPYDATA` 的處理方式（以 SendMessage 系列函式傳送、`cbData` 等）與 Direct SSTP 相同。

```
EXECUTE SAORI/1.0
Module: internal_crypto
Charset: UTF-8
Sender: YAYA
SecurityLevel: Local
HWnd: 1234
Argument0: Digest
Argument1: sha256
Argument2: abc
```

- **Module**: 【必填】要呼叫的模組名稱。以 DLL 名稱去掉 `.dll` 的形式填寫（例如：`internal_crypto`、`string`）。不區分大小寫。<br />
  未指定時回傳 400（`ErrorDescription: invalid parameter`）；模組未知時回傳 400（`ErrorDescription: unknown module`）。
- **HWnd**: 接收回覆的視窗。省略時使用 `WM_COPYDATA` 的 `wParam` 所指定的視窗（與 Direct SSTP 的 SSTP 規則相同）。
- **Charset**: 請求的字元編碼。回應也會使用相同的字元編碼。
- **SecurityLevel**: 在 Direct SSTP 中一律視為 `Local`（不檢查標頭值）。
- **Sender**: 呼叫端的名稱。baseware 不使用此值。
- **Argument\[n\]**: 引數。與 SAORI/1.0 相同。

## 接收回應

回應會透過 `WM_COPYDATA`（`dwData = 9801`）傳回 `HWnd`（或 `wParam`）指定的視窗。內容是以 `SAORI/` 開頭的 SAORI/1.0 回應。<br />
baseware 在處理請求時傳送回覆，因此回覆會在傳送端的 SendMessage 返回之前送達。

## 接受的傳送途徑

SAORI over DirectSSTP 只接受透過 Direct SSTP 傳送的請求。<br />
若透過 socket SSTP 或 SSTP over HTTP 傳送 SAORI/1.0 請求，會回傳 `SAORI/1.0 400 Bad Request` 和 `ErrorDescription: direct sstp only`（在 SSTP over HTTP 中，此回應會作為 HTTP 200 的本文回傳）。<br />
SAORI 請求不會記錄在 SSTP 日誌中。

## 呼叫端 ghost

傳送至 ghost 的視窗時，該 ghost 即為呼叫端。<br />
傳送至 baseware 的主視窗等情況下，若無法判定呼叫端 ghost，則視為「沒有 ghost」（不會像 Direct SSTP 的 SSTP 那樣以顯示中的 ghost 代替）。不使用 ghost 的處理會正常運作，依賴 ghost 的處理（透過事件傳遞結果的[非同步呼叫](async.md)、以 ghost 資料夾為基準的相對路徑等）則會回傳 400（`ErrorDescription: ghost required`）。<br />
不檢查 `ReceiverGhostName` / `ReceiverGhostHWnd` / `ReceiverGhostUUID` 標頭。

## 避免混淆回覆

baseware 將以 `SAORI/`（以及 `SSTP/`）開頭的接收內容視為回覆，不會當作請求處理。

## 功能判定

要確認模組是否可用，請在 `GET Version SAORI/1.0` 中加入 `Module` 後傳送。若可用，會回傳 `SAORI/1.0 200 OK`（在 SSP 中為 `Result: SSP Internal`）。<br />
不支援此擴充功能的 SSP（2.9.12 及之前的版本）會將 SAORI/1.0 請求當作 SSTP 請求讀取，並回傳 SSTP 錯誤（`GET Version` 回傳 `SSTP/1.0 501 Not Implemented`，`EXECUTE` 回傳 `SSTP/1.0 400 Bad Request`）。<br />
傳送端應在「回覆不是以 `SAORI/1.0 200` 開頭」或「沒有收到回覆」時，判定為不可用。<br />
可透過 [internal_system](internal_system/index.md) 取得 SSP 的內建模組及其函式清單。函式接受的選項和演算法名稱（包括在較新 SSP 中新增的項目）可透過 [Describe](internal_system/internal_system.Describe.md) 查詢。

## ErrorDescription

失敗時，回應會以 `ErrorDescription` 標頭提供失敗原因（固定的英文文字）。此標頭不存在於 SAORI/1.0 原始規格中，而是仿照 SHIORI/3.0 的同名標頭。<br />
所有模組共用的值如下。其他值請參閱各模組的說明。

- **direct sstp only**: 400。透過 Direct SSTP 以外的途徑傳送時。
- **unknown module**: 400。`Module` 指定的模組不存在時。
- **unknown function**: 400。模組中不存在指定的函式名稱（`Argument0`）時。
- **ghost required**: 400。無法判定呼叫端 ghost，卻要求執行依賴 ghost 的處理時。
- **invalid parameter**: 400。缺少 `Module`、缺少引數或引數錯誤時。

相容模組（與 DLL 的 SAORI 相容）可能依照原作回傳不含 `ErrorDescription` 的 400。

## 不能寫入標頭值的內容

SAORI 的標頭值不能包含換行，以及開頭或結尾的空白（可以包含逗號）。對於這類資料，請在內建模組中使用 `--data-in=base64` 等[格式](internal.md#バイト列の入力の形式)傳遞。
