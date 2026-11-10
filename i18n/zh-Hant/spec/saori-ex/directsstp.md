# SAORI over DirectSSTP

## 傳送方式

與[Direct SSTP](../sstp/direct.md)相同，使用`WM_COPYDATA`（`dwData = 9801`），將SAORI/1.0要求放入`lpData`，取代SSTP要求，並傳送至自己的ghost視窗（[FMO](../fmo-mutex/index.md)的`hwnd`）。<br />
視窗與`WM_COPYDATA`的處理方式（使用SendMessage系列傳送、`cbData`等）與Direct SSTP相同。

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

- **Module**: 【必須】要呼叫的模組名稱。名稱要寫成去掉DLL名稱中`.dll`的部分（例如：`internal_crypto`、`string`）。不區分大小寫。<br />
  未指定時回傳400（`ErrorDescription: invalid parameter`）；模組不明時回傳400（`ErrorDescription: unknown module`）。
- **HWnd**: 接收回應的視窗。省略時使用`WM_COPYDATA`的`wParam`視窗（與Direct SSTP的SSTP採用相同規則）。
- **Charset**: 要求的字元編碼。回應會以相同的字元編碼傳回。
- **SecurityLevel**: 在Direct SSTP中一律視為`Local`（不查看標頭值）。
- **Sender**: 呼叫端名稱。baseware不會使用此值。
- **Argument\[n\]**: 引數。與SAORI/1.0相同。

## 接收回應

回應會透過`WM_COPYDATA`（`dwData = 9801`）傳回`HWnd`（或`wParam`）指定的視窗。內容是以`SAORI/`開頭的SAORI/1.0回應。<br />
baseware會在處理要求期間傳送回應，因此回應會在傳送端的SendMessage返回前送達。

## 接受的傳輸路徑

SAORI over DirectSSTP只接受Direct SSTP。<br />
若透過SSTP socket或SSTP over HTTP傳送SAORI/1.0要求，會收到`SAORI/1.0 400 Bad Request`和`ErrorDescription: direct sstp only`（SSTP over HTTP會將此回應作為HTTP 200的本文傳回）。<br />
SAORI要求不會記錄在SSTP記錄檔中。

## 呼叫端的ghost

傳送至ghost視窗時，該ghost會成為呼叫端。<br />
若無法得知呼叫端ghost，例如傳送至baseware主視窗時，會視為「沒有ghost」（不像Direct SSTP的SSTP，不會以目前顯示中的ghost代替）。不依賴ghost的處理會正常執行；依賴ghost的處理（透過事件傳送結果的[非同步呼叫](async.md)、以ghost資料夾為基準的相對路徑等）會回傳400（`ErrorDescription: ghost required`）。<br />
不會查看`ReceiverGhostName` / `ReceiverGhostHWnd`標頭。

## 防止誤認回應

baseware會將以`SAORI/`（以及`SSTP/`）開頭的接收資料視為回應，不會當成要求處理。

## 功能檢查

要確認模組是否可用，請在`GET Version SAORI/1.0`中加入`Module`並傳送。若可用，會回傳`SAORI/1.0 200 OK`（SSP會回傳`Result: SSP Internal`）。<br />
不支援此擴充功能的SSP（2.9.12以前）會將SAORI/1.0要求解讀為SSTP要求，並回傳SSTP錯誤（`GET Version`會回傳`SSTP/1.0 501 Not Implemented`，`EXECUTE`會回傳`SSTP/1.0 400 Bad Request`）。<br />
傳送端應判定「回應不是以`SAORI/1.0 200`開頭時即不可用」以及「未收到回應時即不可用」。<br />
SSP內建模組及其函式一覽可從[internal_system](internal_system/index.md)取得。函式接受的選項與演算法名稱（包括新版本SSP新增的項目）可透過[Describe](internal_system/internal_system.Describe.md)查詢。

## ErrorDescription

失敗時，回應會以`ErrorDescription`標頭附上失敗原因（固定的英文字串）。SAORI/1.0原始規格沒有此標頭，這裡是參照SHIORI/3.0的同名標頭。<br />
所有模組共用的項目如下。其他項目請參閱各模組的說明。

- **direct sstp only**: 400。透過Direct SSTP以外的路徑傳送時。
- **unknown module**: 400。`Module`指定的模組不存在時。
- **unknown function**: 400。模組中沒有指定的函式名稱（`Argument0`）時。
- **ghost required**: 400。無法得知呼叫端ghost，卻要求執行依賴ghost的處理時。
- **invalid parameter**: 400。`Module`缺漏，或引數缺漏、錯誤時。

相容模組（SAORI DLL相容模組）有時會依照原始版本的行為，回傳未附加`ErrorDescription`的400。

## 標頭值不能包含的內容

SAORI標頭值不能包含換行，也不能以空白開頭或結尾（可以包含逗號）。這類資料請透過內建模組的`--data-in=base64`等[格式](internal.md#バイト列の入力の形式)傳遞。
