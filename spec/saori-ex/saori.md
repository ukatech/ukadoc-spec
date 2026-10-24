# SAORI/1.0の概要

SAORI/1.0の正しい定義は原典（外部サイト）を参照してください。ここではこのページを読むのに必要な部分だけを簡単にまとめます。

## 要求

```
EXECUTE SAORI/1.0
Charset: UTF-8
Sender: 呼び出し元の名前
SecurityLevel: Local
Argument0: 1つ目の引数
Argument1: 2つ目の引数
```

改行はCR+LF、空行で終わります。引数は`Argument0`から番号順に並べます。値が空の引数も、その位置の引数として数えます。<br />
`Charset`は要求の文字コードで、応答も同じ文字コードで返ります。<br />
機能の有無の確認には`GET Version SAORI/1.0`を使います。

## 応答

```
SAORI/1.0 200 OK
Charset: UTF-8
Result: 結果
Value0: 複数の値を返すときの1つ目
```

- **200 OK**: 成功。`Result`が結果。複数の値を返すときは`Value0`、`Value1`…にも入る。
- **204 No Content**: 成功したが、返す値が無い（結果が空文字列）。
- **400 Bad Request**: 呼び出し方の誤り。
- **500 Internal Server Error**: 処理の失敗。
