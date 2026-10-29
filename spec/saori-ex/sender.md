# 送信側の手順

SHIORIなどの送信側は次の手順でSAORI over DirectSSTPを使います。

1. [FMO](../fmo-mutex/index.md)などから、自分のゴーストの窓（`hwnd`）を得る。
2. 返事を受ける窓を用意する。
3. SAORI/1.0の要求を組み立てて、`Module`と`HWnd`（返事を受ける窓）を付ける。
4. ゴーストの窓へ`WM_COPYDATA`（`dwData = 9801`）をSendMessage系の関数で送る。
5. 返事を受ける窓に`WM_COPYDATA`（`dwData = 9801`）で届いた、`SAORI/`で始まるデータを応答として読む。

使えるかどうかは最初に[GET Version](directsstp.md)で確かめてください。

## 記述例

YAYA・里々では、上の手順をSHIORI自身が行います。DLLのSAORIと同じ書き方で、モジュール名を`internal_`で始まる名前にするだけです。使えない場合（旧SSPなど）の扱いは、各SHIORIの説明を参照してください。

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

結果が`Result`、追加の値が`Value0`以降として扱われるのは、DLLのSAORIと同じです。`--async`を付けた呼び出しの戻り値は空になります。
