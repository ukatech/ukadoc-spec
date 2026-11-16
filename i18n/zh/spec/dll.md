# DLL 通用规范

## DLL 通用规范

本规范定义了 SHIORI、SAORI 及其他伺か (Ukagaka) 系统使用的 DLL 模块的通用接口。

## 内存管理

参数和返回值均通过 Windows Global Memory 传递。具体处理步骤如下：

- baseware 使用 GlobalAlloc() 指定 GMEM_FIXED 标志分配内存，并写入数据
- 模块将收到的 HGLOBAL 强制转换为 (char\*)，直接访问数据
- 模块通过 len 参数获取数据长度，读取所需数据
- 模块使用 GlobalFree() 释放内存
- 返回处理结果时，模块使用 GlobalAlloc() 新分配一块指定 GMEM_FIXED 的内存
- 模块将结果写入分配的内存，并将 len 设置为新的数据长度
- baseware 使用完返回的内存句柄后，用 GlobalFree() 释放内存

注意事项：

- 使用 GMEM_FIXED 标志时，无需调用 GlobalLock()/GlobalUnlock()
- 将 HGLOBAL 强制转换为 (char\*) 即可直接访问内存
- 传入的内存不保证以 NULL 结尾，因此必须参照 len 参数限制访问范围
- 为确保返回值内存的处理不依赖 baseware 的实现且能稳健运行，建议分配比 len 多 1 字节的内存并以零结尾

## request 函数

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

所有请求都通过唯一的 request 函数进行。request 函数是伺か (Ukagaka) 模块的主要接口，处理来自 baseware 的所有请求。

请求数据的格式参考 HTTP 和 SSTP 的头部格式设计，遵循以下规则：

- 所有行均以 CR+LF（0x0D, 0x0A）分隔
- 第 1 行记载命令名和协议版本
- 第 2 行及以后是任意数量的头部，格式为“头部名: 值”
- 头部以连续两个 CR+LF（即添加一个空行）表示结束
- 字符编码遵循头部中指定的方式（通常为 UTF-8 或默认的 OEM codepage）

## 生命周期函数

DLL 加载和卸载时会调用以下函数。

### loadu 函数

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

用于初始化模块的函数。<br />
第 1 个参数指定的全局内存中以 *UTF-8 编码*存储模块的目录路径。

从 SSP 2.6.92 (2025/1/16) 开始实现。此前仅实现了 load。

处理内容示例：

- 以传入的路径为当前目录，读取所需的数据文件
- 初始化模块运行所需的资源
- 根据需要初始化日志文件和数据库

注意事项：

- 即使不需要字符串数据，也必须释放传入的全局内存
- 初始化成功时返回 TRUE，失败时返回 FALSE
- baseware 优先使用此函数

#### load 函数

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

loadu 函数的传统版本。<br />
除第 1 个参数中的模块目录路径采用默认的 OEM codepage（在日语环境中为 CP932）编码外，规范与 loadu 函数相同。

注意事项：

- 未实现 loadu 函数时，使用此函数作为回退
- 为确保兼容性，建议同时实现 load 和 loadu，并在已通过 loadu 初始化后又调用 load 时忽略该调用
- 为支持 Unicode，必须将收到的路径正确转换为宽字符串

#### unload 函数

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

用于执行模块结束处理的函数。模块卸载时由 baseware 调用。

应实现的处理：

- 释放通过 CreateFile 等打开的文件句柄
- 释放通过 CreateMutex 等创建的同步对象
- 等待通过 CreateThread 等创建的线程结束，并执行后续处理
- 释放模块分配的所有其他系统资源

目前未使用返回值，但考虑到未来的扩展性，建议返回 TRUE。

## 多实例函数（可选）

`load` / `request` / `unload` 对每个 DLL 只能拥有一个实例。为便于 baseware 在同一进程中从同一个 DLL 创建多个实例，可以**选择性地**实现以下通过 id 区分实例的函数。即使不实现这些函数，模块仍然有效，也能在不调用这些函数的 baseware 上照常运行。

```
extern "C" __declspec(dllexport) long __cdecl multi_loadu(HGLOBAL h, long len);
extern "C" __declspec(dllexport) long __cdecl multi_load(HGLOBAL h, long len);
extern "C" __declspec(dllexport) BOOL __cdecl multi_unload(long id);
extern "C" __declspec(dllexport) HGLOBAL __cdecl multi_request(long id, HGLOBAL h, long *len);
```

- **multi_loadu / multi_load**: 使用与 `loadu` / `load` 相同的参数创建新实例。模块目录路径的字符编码也分别与 `loadu`（UTF-8）和 `load`（默认的 OEM codepage）相同。返回值为指向该实例的 id（大于等于 1 的整数），失败时建议返回 `-1`。baseware 将小于等于 0 的返回值视为失败。与 `loadu` / `load` 相同，内存由模块释放
- **multi_unload**: 结束 id 指定的实例。成功时返回 TRUE，id 不存在时返回 FALSE
- **multi_request**: 向 id 指定的实例传递与 `request` 格式相同的请求。id 不存在时返回 NULL

注意事项：

- id 0 分配给传统的 `load` / `request` / `unload` 所处理的实例。`multi_load*` 不得返回 0
- 传统函数和多实例函数可以同时实现在同一个 DLL 中。两者的实例作为不同实例处理
- YAYA 的 `multi_load*` 即使在字典读取失败时也会返回 id（与 `load` 始终返回 TRUE 相同，使用 `CI_check_failed` 确认是否失败）
- SSP 不使用这些函数（这是面向 SSP 以外的 baseware 的规范）

## YAYA 专有函数

以下函数由 YAYA（`yaya.dll`）独立实现。它们用于与调试检查工具协作，不属于 SHIORI 规范。其他模块无需实现，baseware 也无需调用。

!!! note "注"
    规范可能因 YAYA 的需要而改变。带有 `multi_` 的函数与上一节的多实例函数一样，针对 id 指定的实例运行。

### CI_check_failed 函数

```
extern "C" __declspec(dllexport) BOOL __cdecl CI_check_failed(void);
extern "C" __declspec(dllexport) BOOL __cdecl multi_CI_check_failed(long id);
```

字典读取失败且运行被抑制，或处于紧急模式时返回 TRUE。id 不存在（`multi_` 版本）或尚未调用 `load` 时返回 FALSE。

### Set_loghandler 函数

```
extern "C" __declspec(dllexport) void __cdecl Set_loghandler(void (*loghandler)(const wchar_t *str, int mode, int id));
extern "C" __declspec(dllexport) void __cdecl multi_Set_loghandler(long id, void (*loghandler)(const wchar_t *str, int mode, int id));
```

注册接收 YAYA 日志的回调函数。注册后将启用日志输出。`multi_` 版本只能为通过 `multi_load*` 创建后的实例注册，id 不存在时不执行任何操作。

回调函数的参数如下。

- **str**: 日志字符串（UTF-16）。`mode` 为控制值时为空字符串
- **mode**: 日志类型或控制值
- **id**: 日志消息编号（不是实例的 id）

`mode` 的值如下。

- **0**: 信息
- **1**: 致命错误
- **2**: 错误
- **3**: 警告
- **4**: 注记
- **6**: 日志结束
- **16 / 17 / 32**: 通知后续日志中多字节字符的字符编码。16 为 Shift_JIS，17 为 UTF-8，32 为 OS 默认编码。在日志开始时调用 1 次

回调函数在调用 `load` / `request` / `unload` 的线程中执行。

### logsend 函数

```
extern "C" __declspec(dllexport) BOOL __cdecl logsend(long hwnd);
```

仅 Windows DLL 版本提供此函数。传入通过 `WM_COPYDATA` 接收日志的窗口句柄（HWND）。始终返回 TRUE。通过 `Set_loghandler` 注册了回调函数时，优先使用该回调函数。

`WM_COPYDATA` 的 `dwData` 中存放与 `Set_loghandler` 的 `mode` 相同的值，`lpData` 中存放日志字符串（UTF-16、以 NUL 结尾）。
