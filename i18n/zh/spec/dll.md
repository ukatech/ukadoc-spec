# DLL通用规范

## DLL通用规范

本规范定义了 SHIORI、SAORI 及其他伺か (Ukagaka) 系统中使用的 DLL 模块的通用接口。

## 内存管理

所有参数和返回值均通过 Windows Global Memory 传递。具体处理步骤如下：

- baseware 使用 GlobalAlloc() 并指定 GMEM_FIXED 标志分配内存，然后写入数据
- 模块将收到的 HGLOBAL 强制转换为 (char\*)，直接访问数据
- 模块通过 len 参数获取数据长度，读取所需数据
- 模块使用 GlobalFree() 释放内存
- 返回处理结果时，模块使用 GlobalAlloc() 并指定 GMEM_FIXED 重新分配内存
- 模块将结果写入分配的内存，并将 len 设置为新的数据长度
- baseware 使用完返回的内存句柄后，通过 GlobalFree() 释放内存

注意事项：

- 使用 GMEM_FIXED 标志时，无需调用 GlobalLock()/GlobalUnlock()
- 将 HGLOBAL 强制转换为 (char\*) 即可直接访问内存
- 传入的内存不保证以 NULL 结尾，因此必须通过 len 参数限制访问范围
- 为确保不依赖 baseware 实现的稳健运行，建议为返回值分配比 len 多 1 字节的内存，并以零结尾

## request函数

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

所有请求都通过唯一的 request 函数处理。request 函数是伺か (Ukagaka) 模块的主要接口，处理来自 baseware 的所有请求。

请求数据的格式参考 HTTP 和 SSTP 的头部格式设计，遵循以下规则：

- 所有行以 CR+LF（0x0D, 0x0A）分隔
- 第 1 行记录命令名和协议版本
- 第 2 行及后续行包含任意数量的头部，格式为“头部名: 值”
- 连续放置两个 CR+LF（添加空行）表示头部结束
- 字符编码遵循头部指定的方式（通常为 UTF-8 或默认的 OEM codepage）

## 生命周期函数

DLL 加载和卸载时会调用以下函数。

### loadu函数

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

用于初始化模块的函数。<br />
第 1 个参数指定的全局内存中存储模块目录路径，采用 *UTF-8 编码*。

自 SSP 2.6.92 (2025/1/16) 起实现。在此之前只实现了 load。

处理内容示例：

- 以传入的路径为当前目录，读取所需的数据文件
- 初始化模块运行所需的资源
- 根据需要初始化日志文件和数据库

注意事项：

- 即使不需要字符串数据，也必须释放传入的全局内存
- 初始化成功时返回 TRUE，失败时返回 FALSE
- baseware 会优先使用本函数

#### load函数

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

loadu 函数的旧版。<br />
除第 1 个参数中的模块目录路径使用默认的 OEM codepage（日本语环境下为 CP932）编码外，规范与 loadu 函数相同。

注意事项：

- 在未实现 loadu 函数时用作回退函数
- 为确保兼容性，建议同时实现 load 和 loadu，若 loadu 已完成初始化后又调用了 load，则忽略该调用
- 为支持 Unicode，需要将收到的路径适当转换为宽字符串

#### unload函数

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

用于执行模块终止处理的函数。模块卸载时由 baseware 调用。

应实现的处理：

- 释放通过 CreateFile 等打开的文件句柄
- 释放通过 CreateMutex 等创建的同步对象
- 等待通过 CreateThread 等创建的线程结束，并执行后续处理
- 释放模块分配的所有其他系统资源

返回值目前未使用，但考虑到将来的扩展性，建议返回 TRUE。

## 多实例函数（可选）

`load` / `request` / `unload` 对每个 DLL 只能拥有一个实例。对于希望在一个进程中从同一个 DLL 创建多个实例的 baseware，可以**选择性地**实现以下使用 id 区分实例的函数。即使不实现，模块仍可正常使用，在不调用这些函数的 baseware 中也能照常运行。

```
extern "C" __declspec(dllexport) long __cdecl multi_loadu(HGLOBAL h, long len);
extern "C" __declspec(dllexport) long __cdecl multi_load(HGLOBAL h, long len);
extern "C" __declspec(dllexport) BOOL __cdecl multi_unload(long id);
extern "C" __declspec(dllexport) HGLOBAL __cdecl multi_request(long id, HGLOBAL h, long *len);
```

- **multi_loadu / multi_load**: 使用与 `loadu` / `load` 相同的参数创建新实例。模块目录路径的字符编码也分别与 `loadu`（UTF-8）和 `load`（默认的 OEM codepage）相同。返回值是指向该实例的 id（大于等于 1 的整数），失败时建议返回 `-1`。baseware 将小于等于 0 的返回值视为失败。与 `loadu` / `load` 一样，内存由模块释放
- **multi_unload**: 终止 id 指定的实例。成功时返回 TRUE，id 不存在时返回 FALSE
- **multi_request**: 向 id 指定的实例传递与 `request` 格式相同的请求。id 不存在时返回 NULL

注意事项：

- id 0 分配给传统的 `load` / `request` / `unload` 所处理的实例。`multi_load*` 不得返回 0
- 传统函数和多实例函数可以同时在同一个 DLL 中实现。两者的实例作为独立实例处理
- YAYA 的 `multi_load*` 即使加载辞典失败也会返回 id（与 `load` 始终返回 TRUE 一样，使用 `CI_check_failed` 检查是否失败）
- SSP 不使用这些函数（该规范面向 SSP 以外的 baseware）

## YAYA 专有函数

以下函数由 YAYA（`yaya.dll`）自行实现，用于与调试检查工具配合，不属于 SHIORI 规范。其他模块无需实现，baseware 也无需调用。

!!! note "注"
    规范可能因 YAYA 的需要而发生变化。带 `multi_` 的函数与上一节的多实例函数一样，对 id 指定的实例操作。

### CI_check_failed函数

```
extern "C" __declspec(dllexport) BOOL __cdecl CI_check_failed(void);
extern "C" __declspec(dllexport) BOOL __cdecl multi_CI_check_failed(long id);
```

当辞典加载失败且运行受到抑制，或进入紧急模式时返回 TRUE。id 不存在时（`multi_` 版）或调用 `load` 之前返回 FALSE。

### Set_loghandler函数

```
extern "C" __declspec(dllexport) void __cdecl Set_loghandler(void (*loghandler)(const wchar_t *str, int mode, int id));
extern "C" __declspec(dllexport) void __cdecl multi_Set_loghandler(long id, void (*loghandler)(const wchar_t *str, int mode, int id));
```

注册接收 YAYA 日志的回调函数。注册后将启用日志输出。`multi_` 版只能为通过 `multi_load*` 创建后的实例注册，id 不存在时不执行任何操作。

回调参数如下。

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
- **16 / 17 / 32**: 通知后续日志中多字节字符的编码。16 为 Shift_JIS，17 为 UTF-8，32 为 OS 默认编码。在日志开始时调用 1 次

回调在调用 `load` / `request` / `unload` 的线程中执行。

### logsend函数

```
extern "C" __declspec(dllexport) BOOL __cdecl logsend(long hwnd);
```

仅 Windows DLL 版提供。传入通过 `WM_COPYDATA` 接收日志的窗口句柄（HWND）。始终返回 TRUE。通过 `Set_loghandler` 注册了回调时，优先使用回调。

`WM_COPYDATA` 的 `dwData` 中存放与 `Set_loghandler` 的 `mode` 相同的值，`lpData` 中存放日志字符串（UTF-16，以 NUL 结尾）。
