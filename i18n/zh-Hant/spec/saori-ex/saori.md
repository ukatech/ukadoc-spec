# SAORI/1.0 Overview

For the full and correct definition of SAORI/1.0, refer to the original source (external site). This page provides a brief summary of only the parts needed to read it.

## Request

```
EXECUTE SAORI/1.0
Charset: UTF-8
Sender: 呼び出し元の名前
SecurityLevel: Local
Argument0: 1つ目の引数
Argument1: 2つ目の引数
```

Lines end with CR+LF, and the request ends with a blank line. Arguments are listed in numerical order, starting from `Argument0`. An empty argument still counts as an argument in its position.<br />
`Charset` is the character encoding of the request, and the response is returned in the same encoding.<br />
Use `GET Version SAORI/1.0` to check whether the feature is available.

## Response

```
SAORI/1.0 200 OK
Charset: UTF-8
Result: 結果
Value0: 複数の値を返すときの1つ目
```

- **200 OK**: Success. `Result` contains the result. When returning multiple values, they are also placed in `Value0`, `Value1`, and so on.
- **204 No Content**: The operation succeeded, but there are no values to return (the result is an empty string).
- **400 Bad Request**: Incorrect invocation.
- **500 Internal Server Error**: Processing failed.
