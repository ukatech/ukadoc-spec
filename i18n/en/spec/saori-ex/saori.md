# Overview of SAORI/1.0

For the formal definition of SAORI/1.0, refer to the original source (external site). This page provides a brief summary of only the parts needed to read it.

## Request

```
EXECUTE SAORI/1.0
Charset: UTF-8
Sender: 呼び出し元の名前
SecurityLevel: Local
Argument0: 1つ目の引数
Argument1: 2つ目の引数
```

Lines are separated by CR+LF, and the request ends with a blank line. Arguments are ordered by number, starting with `Argument0`. An argument with an empty value still counts as an argument at that position.<br />
`Charset` specifies the request's character encoding, and the response is returned in the same encoding.<br />
Use `GET Version SAORI/1.0` to check whether a feature is available.

## Response

```
SAORI/1.0 200 OK
Charset: UTF-8
Result: 結果
Value0: 複数の値を返すときの1つ目
```

- **200 OK**: Success. The result is in `Result`. When returning multiple values, they are also included in `Value0`, `Value1`, and so on.
- **204 No Content**: The request succeeded, but there is no value to return (the result is an empty string).
- **400 Bad Request**: Incorrect invocation.
- **500 Internal Server Error**: Processing failed.
