# SAORI over DirectSSTP

## 发送方式

与[Direct SSTP](../sstp/direct.md)相同，使用`WM_COPYDATA`（`dwData = 9801`），将SAORI/1.0请求而非SSTP请求放入`lpData`，发送到自己的ghost窗口（[FMO](../fmo-mutex/index.md)的`hwnd`）。<br />
窗口和`WM_COPYDATA`的处理方式（使用SendMessage系列发送、`cbData`等）与Direct SSTP相同。

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

- **Module**: 【必需】要调用的模块名称。去掉DLL名中的`.dll`后填写（例如：`internal_crypto`、`string`）。不区分大小写。<br />
  如果缺少该项，则返回400（`ErrorDescription: invalid parameter`）；如果模块未知，则返回400（`ErrorDescription: unknown module`）。
- **HWnd**: 接收响应的窗口。省略时使用`WM_COPYDATA`的`wParam`窗口（规则与Direct SSTP的SSTP相同）。
- **Charset**: 请求的字符编码。响应也会使用相同的字符编码返回。
- **SecurityLevel**: 在Direct SSTP中始终按`Local`处理（不检查标头值）。
- **Sender**: 调用方的名称。baseware不会使用此项。
- **Argument\[n\]**: 参数。与SAORI/1.0相同。

## 接收响应

响应会通过`WM_COPYDATA`（`dwData = 9801`）返回到`HWnd`（或`wParam`）窗口。内容是以`SAORI/`开头的SAORI/1.0响应。<br />
baseware会在处理请求期间发送响应，因此发送端的SendMessage返回之前就会收到响应。

## 接受请求的路径

SAORI over DirectSSTP只通过Direct SSTP接受请求。<br />
通过套接字SSTP或SSTP over HTTP发送SAORI/1.0请求时，会返回`SAORI/1.0 400 Bad Request`和`ErrorDescription: direct sstp only`（对于SSTP over HTTP，此响应会作为HTTP 200的正文返回）。<br />
SAORI请求不会记录在SSTP日志中。

## 调用方的ghost

发送到ghost窗口时，该ghost会成为调用方。<br />
例如，发送到baseware主窗口时，如果无法确定调用方的ghost，则按“没有ghost”处理（不会像Direct SSTP的SSTP那样，用当前显示的ghost代替）。不依赖ghost的处理可以正常运行；依赖ghost的处理（通过事件传递结果的[异步调用](async.md)、以ghost文件夹为基准的相对路径等）则会返回400（`ErrorDescription: ghost required`）。<br />
不会检查`ReceiverGhostName` / `ReceiverGhostHWnd`标头。

## 防止响应错认

baseware会将以`SAORI/`（以及`SSTP/`）开头的接收内容视为响应，不会将其作为请求处理。

## 功能检查

要确认模块是否可用，请在`GET Version SAORI/1.0`中添加`Module`并发送。若可用，则会返回`SAORI/1.0 200 OK`（在SSP中为`Result: SSP Internal`）。<br />
不支持此扩展的SSP（2.9.12及更早版本）会将SAORI/1.0请求当作SSTP请求读取，并返回SSTP错误（`GET Version`会返回`SSTP/1.0 501 Not Implemented`，`EXECUTE`会返回`SSTP/1.0 400 Bad Request`）。<br />
发送端应判断“只有响应以`SAORI/1.0 200`开头时才可用”以及“没有收到响应时不可用”。<br />
SSP内置模块及其函数的列表可通过[internal_system](internal_system/index.md)获取。函数接受的选项和算法名称（包括较新SSP中新增的名称）可通过[Describe](internal_system/internal_system.Describe.md)查询。

## ErrorDescription

失败时，响应会通过`ErrorDescription`标头附带失败原因（固定的英文字符串）。SAORI/1.0原始规范中没有此标头；它参照了SHIORI/3.0中的同名标头。<br />
所有模块通用的原因如下。其他原因请参阅各模块的说明。

- **direct sstp only**: 400。通过Direct SSTP以外的路径发送时。
- **unknown module**: 400。`Module`指定的模块不存在时。
- **unknown function**: 400。模块中不存在函数名（`Argument0`）时。
- **ghost required**: 400。无法确定调用方ghost，却请求了依赖ghost的处理时。
- **invalid parameter**: 400。`Module`缺失，或参数缺失、错误时。

兼容模块（兼容DLL的SAORI）有时会像原作一样返回不带`ErrorDescription`的400。

## 标头值中不能填写的内容

SAORI标头值中不能填写换行符以及开头或结尾的空白（可以填写逗号）。对于这类数据，请使用内置模块支持的`--data-in=base64`等[格式](internal.md#バイト列の入力の形式)传入。
