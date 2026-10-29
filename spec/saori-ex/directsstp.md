# SAORI over DirectSSTP

## 送り方

[Direct SSTP](../sstp/direct.md)と同じく`WM_COPYDATA`（`dwData = 9801`）を使い、`lpData`にSSTPの要求の代わりにSAORI/1.0の要求を入れて、自分のゴーストの窓（[FMO](../fmo-mutex/index.md)の`hwnd`）へ送ります。<br />
窓・`WM_COPYDATA`の扱い（SendMessage系で送る、`cbData`など）はDirect SSTPと同じです。

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

- **Module**: 【必須】呼び出すモジュールの名前。DLL名から`.dll`を除いた形で書く（例：`internal_crypto`、`string`）。大文字小文字は区別しない。<br />
  無ければ400（`ErrorDescription: invalid parameter`）、知らないモジュールなら400（`ErrorDescription: unknown module`）。
- **HWnd**: 返事を受ける窓。省略時は`WM_COPYDATA`の`wParam`の窓（Direct SSTPのSSTPと同じ規則）。
- **Charset**: 要求の文字コード。応答も同じ文字コードで返る。
- **SecurityLevel**: Direct SSTPでは常に`Local`として扱う（ヘッダの値は見ない）。
- **Sender**: 呼び出し元の名前。ベースウェアは使わない。
- **Argument\[n\]**: 引数。SAORI/1.0と同じ。

## 応答の受け取り

応答は`HWnd`（または`wParam`）の窓へ、`WM_COPYDATA`（`dwData = 9801`）で返ります。内容は`SAORI/`で始まるSAORI/1.0の応答です。<br />
ベースウェアは要求の処理中に返事を送るので、送信側のSendMessageが戻る前に返事が届きます。

## 受け付ける経路

SAORI over DirectSSTPはDirect SSTPだけで受け付けます。<br />
ソケットのSSTPやSSTP over HTTPでSAORI/1.0の要求を送ると、`SAORI/1.0 400 Bad Request`と`ErrorDescription: direct sstp only`が返ります（SSTP over HTTPでは、HTTPの200の本文としてこの応答が返ります）。<br />
SAORIの要求はSSTPログに記録されません。

## 呼び出し元のゴースト

ゴーストの窓へ送った場合は、そのゴーストが呼び出し元になります。<br />
ベースウェアの主窓へ送ったときなど、呼び出し元のゴーストが分からない場合は「ゴーストなし」として扱います（Direct SSTPのSSTPのように表示中のゴーストを代わりに当てることはしません）。ゴーストを使わない処理は普通に動き、ゴーストに依存する処理（結果をイベントで届ける[非同期の呼び出し](async.md)、ゴーストのフォルダを基準にした相対パスなど）は400（`ErrorDescription: ghost required`）になります。<br />
`ReceiverGhostName` / `ReceiverGhostHWnd`ヘッダは見ません。

## 返事の取り違えを防ぐ

ベースウェアは`SAORI/`（および`SSTP/`）で始まる受信を返事とみなし、要求としては扱いません。

## 機能の判定

モジュールが使えるかどうかは、`GET Version SAORI/1.0`に`Module`を付けて送って確かめます。使えれば`SAORI/1.0 200 OK`（SSPでは`Result: SSP Internal`）が返ります。<br />
この拡張に対応していないSSP（2.9.12以前）はSAORI/1.0の要求をSSTPの要求として読み、SSTPのエラー（`GET Version`には`SSTP/1.0 501 Not Implemented`、`EXECUTE`には`SSTP/1.0 400 Bad Request`）を返します。<br />
送信側は「`SAORI/1.0 200`で始まる返事でなければ使えない」「返事が来なければ使えない」と判定してください。<br />
SSPの内蔵モジュールとその関数の一覧は、[internal_system](internal_system/index.md)で取れます。

## ErrorDescription

失敗したときは、応答に`ErrorDescription`ヘッダで失敗理由（固定の英語の文字列）が付きます。SAORI/1.0の原典には無いヘッダで、SHIORI/3.0の同名のヘッダにならっています。<br />
どのモジュールでも使うものは次のとおりです。ほかは各モジュールの説明を参照してください。

- **direct sstp only**: 400。Direct SSTP以外の経路で送った。
- **unknown module**: 400。`Module`のモジュールが無い。
- **unknown function**: 400。関数名（`Argument0`）がモジュールに無い。
- **ghost required**: 400。呼び出し元のゴーストが分からないのに、ゴーストに依存する処理を求めた。
- **invalid parameter**: 400。`Module`の欠け・引数の欠けや誤り。

互換モジュール（DLLのSAORIの互換）は、原作どおり`ErrorDescription`の付かない400を返すことがあります。

## ヘッダの値に書けないもの

SAORIのヘッダの値には、改行と、先頭・末尾の空白を書けません（カンマは書けます）。こうしたデータは、内蔵モジュールでは`--data-in=base64`などの[形式](internal.md#バイト列の入力の形式)を使って渡してください。
