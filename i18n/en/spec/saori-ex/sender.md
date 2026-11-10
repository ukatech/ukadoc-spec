# Sender procedure

A sender such as SHIORI uses SAORI over DirectSSTP as follows.

1. Obtain the window (`hwnd`) of your own ghost using [FMO](../fmo-mutex/index.md) or a similar method.
2. Prepare a window to receive the response.
3. Construct a SAORI/1.0 request and add `Module` and `HWnd` (the window to receive the response).
4. Send `WM_COPYDATA` (`dwData = 9801`) to the ghost's window using a SendMessage-family function.
5. Read the data beginning with `SAORI/` that arrives at the response-receiving window in a `WM_COPYDATA` message (`dwData = 9801`) as the response.

First check whether it is available using [GET Version](directsstp.md).

## 記述例

In YAYA and Satori, SHIORI itself performs the procedure above. Use the same syntax as for DLL SAORI, with only the module name changed to a name beginning with `internal_`. For how to handle cases where it is unavailable (such as older SSP versions), see the documentation for each SHIORI.

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

- **Satori（登録は不要で、モジュール名をそのまま`（）`で呼ぶ）**:

  ```
  ＊OnBoot
  　（internal_crypto、Digest、sha256、abc）
  　（internal_crypto、HashPassword、secret、--async=OnHashDone）

  ＊OnHashDone
  　（Ｒ１）
  ```

The result is handled as `Result`, and additional values as `Value0` onward, just as with DLL SAORI. Calls with `--async` return an empty value.
