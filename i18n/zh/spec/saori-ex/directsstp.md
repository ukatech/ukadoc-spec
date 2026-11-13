# SAORI over DirectSSTP

## 发送方法

与[Direct SSTP](../sstp/direct.md)一样，使用`WM_COPYDATA`（`dwData = 9801`），在`lpData`中放入SAORI/1.0请求而非SSTP请求，并发送到自己的ghost窗口（[FMO](../fmo-mutex/index.md)的`hwnd`）。<br />
窗口和`WM_COPYDATA`的处理方式（通过SendMessage系列函数发送、`cbData`等）与Direct SSTP相同。

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

- **Module**: 【必需】要调用的模块名称。填写去掉`.dll`的DLL名称（例如：`internal_crypto`、`string`）。不区分大小写。<br />
  如果缺失，返回400（`ErrorDescription: invalid parameter`）；如果模块未知，返回400（`ErrorDescription: unknown module`）。
- **HWnd**: 接收响应的窗口。省略时使用`WM_COPYDATA`的`wParam`指定的窗口（与Direct SSTP的SSTP规则相同）。
- **Charset**: 请求的字符编码。响应也使用相同的字符编码。
- **SecurityLevel**: 在Direct SSTP中始终按`Local`处理（不检查头字段的值）。
- **Sender**: 调用方名称。baseware不使用此字段。
- **Argument\[n\]**: 参数。与SAORI/1.0相同。

## 接收响应

响应通过`WM_COPYDATA`（`dwData = 9801`）返回到`HWnd`（或`wParam`）指定的窗口。内容是以`SAORI/`开头的SAORI/1.0响应。<br />
baseware在处理请求时发送响应，因此发送方的SendMessage返回之前就会收到响应。

## 接收途径

SAORI over DirectSSTP仅通过Direct SSTP接收。<br />
如果通过套接字SSTP或SSTP over HTTP发送SAORI/1.0请求，将返回`SAORI/1.0 400 Bad Request`和`ErrorDescription: direct sstp only`（在SSTP over HTTP中，此响应作为HTTP 200的正文返回）。<br />
SAORI请求不会记录在SSTP日志中。

## 调用方ghost

发送到ghost窗口时，该ghost即为调用方。<br />
发送到baseware主窗口等情况下，如果无法确定调用方ghost，则按“无ghost”处理（不会像Direct SSTP的SSTP那样使用正在显示的ghost代替）。不使用ghost的处理正常运行；依赖ghost的处理（通过事件传递结果的[异步调用](async.md)、以ghost文件夹为基准的相对路径等）返回400（`ErrorDescription: ghost required`）。<br />
不检查`ReceiverGhostName` / `ReceiverGhostHWnd` / `ReceiverGhostUUID`头字段。

## 防止混淆响应

baseware将以`SAORI/`（以及`SSTP/`）开头的接收内容视为响应，不作为请求处理。

## 功能检测

要确认模块是否可用，可发送带有`Module`的`GET Version SAORI/1.0`。如果可用，将返回`SAORI/1.0 200 OK`（在SSP中为`Result: SSP Internal`）。<br />
不支持此扩展的SSP（2.9.12及以前版本）会将SAORI/1.0请求作为SSTP请求读取，并返回SSTP错误（`GET Version`返回`SSTP/1.0 501 Not Implemented`，`EXECUTE`返回`SSTP/1.0 400 Bad Request`）。<br />
发送方应在“响应不是以`SAORI/1.0 200`开头”或“没有收到响应”时判定为不可用。<br />
SSP内置模块及其函数列表可通过[internal_system](internal_system/index.md)获取。函数接受的选项和算法名称（包括较新SSP中新增的项目）可通过[Describe](internal_system/internal_system.Describe.md)查询。

## ErrorDescription

失败时，响应中会包含`ErrorDescription`头字段，说明失败原因（固定的英文字符串）。该头字段不在SAORI/1.0原始规范中，而是参照SHIORI/3.0中的同名头字段。<br />
各模块共用的错误如下。其他错误请参阅各模块的说明。

- **direct sstp only**: 400。通过Direct SSTP以外的途径发送时。
- **unknown module**: 400。`Module`指定的模块不存在时。
- **unknown function**: 400。模块中不存在指定的函数名（`Argument0`）时。
- **ghost required**: 400。无法确定调用方ghost，却请求依赖ghost的处理时。
- **invalid parameter**: 400。`Module`缺失、参数缺失或错误时。

兼容模块（兼容DLL版SAORI的模块）可能按照原作返回不带`ErrorDescription`的400。

## 头字段值中不能填写的内容

SAORI头字段的值不能包含换行以及开头或末尾的空白（可以包含逗号）。对于此类数据，使用内置模块时请通过`--data-in=base64`等[格式](internal.md#バイト列の入力の形式)传递。
