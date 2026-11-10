# SAORI/1.0 概述

SAORI/1.0 的正式定义请参阅原始规范（外部网站）。此处仅简要总结阅读本页所需的内容。

## 请求

```
EXECUTE SAORI/1.0
Charset: UTF-8
Sender: 呼び出し元の名前
SecurityLevel: Local
Argument0: 1つ目の引数
Argument1: 2つ目の引数
```

换行符为 CR+LF，并以空行结束。参数按 `Argument0` 起的编号顺序排列。值为空的参数也计入其所在位置。<br />
`Charset` 是请求的字符编码，响应也会使用相同的字符编码返回。<br />
检查功能是否可用时，请使用 `GET Version SAORI/1.0`。

## 响应

```
SAORI/1.0 200 OK
Charset: UTF-8
Result: 結果
Value0: 複数の値を返すときの1つ目
```

- **200 OK**: 成功。`Result` 中是结果。返回多个值时，也会放入 `Value0`、`Value1` 等字段。
- **204 No Content**: 成功，但没有要返回的值（结果为空字符串）。
- **400 Bad Request**: 调用方式错误。
- **500 Internal Server Error**: 处理失败。
