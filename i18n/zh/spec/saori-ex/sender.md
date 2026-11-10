# 发送方步骤

SHIORI 等发送方通过以下步骤使用 SAORI over DirectSSTP。

1. 从 [FMO](../fmo-mutex/index.md) 等处获取自己 ghost 的窗口（`hwnd`）。
2. 准备一个用于接收响应的窗口。
3. 组装 SAORI/1.0 请求，并附加 `Module` 和 `HWnd`（用于接收响应的窗口）。
4. 使用 SendMessage 系列函数，向 ghost 窗口发送 `WM_COPYDATA`（`dwData = 9801`）。
5. 读取发送到响应接收窗口的、以 `SAORI/` 开头的 `WM_COPYDATA`（`dwData = 9801`）数据作为响应。

请先通过 [GET Version](directsstp.md) 确认是否可用。

## 記述例

在 YAYA 和里々中，上述步骤由 SHIORI 自身执行。写法与 DLL 的 SAORI 相同，只需将模块名设为以 `internal_` 开头的名称。无法使用时（例如旧版 SSP）的处理方式，请参阅各 SHIORI 的说明。

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

结果按与 DLL 的 SAORI 相同方式处理：`Result` 是结果，后续值从 `Value0` 起依次对应。带有 `--async` 的调用会返回空值。
