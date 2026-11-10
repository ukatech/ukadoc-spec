# SAORI/1.0 概要

SAORI/1.0的正確定義請參閱原始規格（外部網站）。此處僅簡要整理閱讀本頁所需的內容。

## 要求

```
EXECUTE SAORI/1.0
Charset: UTF-8
Sender: 呼び出し元の名前
SecurityLevel: Local
Argument0: 1つ目の引数
Argument1: 2つ目の引数
```

換行使用 CR+LF，並以空白行結尾。引數從`Argument0`開始依序排列。值為空的引數也會計入其位置。<br />
`Charset`是要求的字元編碼，回應也會使用相同的字元編碼。<br />
使用`GET Version SAORI/1.0`確認功能是否可用。

## 回應

```
SAORI/1.0 200 OK
Charset: UTF-8
Result: 結果
Value0: 複数の値を返すときの1つ目
```

- **200 OK**: 成功。`Result`為結果。需要回傳多個值時，也會放入`Value0`、`Value1`…。
- **204 No Content**: 成功，但沒有要回傳的值（結果為空字串）。
- **400 Bad Request**: 呼叫方式錯誤。
- **500 Internal Server Error**: 處理失敗。
