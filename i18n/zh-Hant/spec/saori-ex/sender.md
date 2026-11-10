# Sender Procedure

Senders such as SHIORI use SAORI over DirectSSTP as follows.

1. Obtain the window (`hwnd`) of your own ghost from [FMO](../fmo-mutex/index.md) or another source.
2. Prepare a window to receive the response.
3. Assemble a SAORI/1.0 request and add `Module` and `HWnd` (the window to receive the response).
4. Send `WM_COPYDATA` (`dwData = 9801`) to the ghost's window using a SendMessage-family function.
5. Read the data beginning with `SAORI/` received by the response window via `WM_COPYDATA` (`dwData = 9801`) as the response.

First, check whether it is available using [GET Version](directsstp.md).

## 記述例

In YAYA and Satori, SHIORI itself performs the steps above. Use the same syntax as for DLL SAORI, but give the module a name beginning with `internal_`. For instructions on handling cases where it is unavailable (such as older versions of SSP), refer to the documentation for each SHIORI.

- **YAYA (`FUNCTIONEX`)**:

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

- **Satori (no registration is needed; call the module name directly with `（）`)**:

  ```
  ＊OnBoot
  　（internal_crypto、Digest、sha256、abc）
  　（internal_crypto、HashPassword、secret、--async=OnHashDone）

  ＊OnHashDone
  　（Ｒ１）
  ```

As with DLL SAORI, the result is treated as `Result`, and additional values as `Value0` and later entries. The return value of a call with `--async` is empty.
