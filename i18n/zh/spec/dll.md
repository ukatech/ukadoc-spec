# DLL通用规范

## DLL通用规范

本规范定义了 SHIORI、SAORI 及其他伺か系统中使用的 DLL 模块的通用接口。

## 内存管理

所有参数和返回值的传递均使用 Windows Global Memory。具体按以下步骤处理：

- baseware 使用 GlobalAlloc() 并指定 GMEM_FIXED 标志分配内存，然后写入数据
- 模块将收到的 HGLOBAL 强制转换为 (char\*)，直接访问数据
- 模块参照 len 参数获取数据长度，并读取所需数据
- 模块使用 GlobalFree() 释放内存
- 返回处理结果时，模块使用 GlobalAlloc() 新分配内存，并指定 GMEM_FIXED
- 模块将结果写入已分配的内存，并在 len 中设置新的数据长度
- baseware 使用返回的内存句柄后，通过 GlobalFree() 释放内存

注意事项：

- 使用 GMEM_FIXED 标志时，无需调用 GlobalLock()/GlobalUnlock()
- 将 HGLOBAL 强制转换为 (char\*) 即可直接访问内存
- 传入的内存不保证以 NULL 结尾，因此必须参照 len 参数限制访问范围
- 为确保在不同 baseware 实现下均能可靠运行，建议为返回值分配比 len 多 1 字节的内存，并以零结尾

## request 函数

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

所有请求均通过唯一的函数 request 处理。request 函数是伺か模块的主要接口，用于处理来自 baseware 的所有请求。

请求数据的格式参考了 HTTP 和 SSTP 的标头格式，并遵循以下规则：

- 所有行均以 CR+LF（0x0D, 0x0A）分隔
- 第 1 行写入命令名称和协议版本
- 第 2 行及之后为任意数量的标头，格式为「标头名称: 值」
- 在标头部分末尾连续放置两个 CR+LF（添加空行），以表示标头部分结束
- 字符编码遵循标头中指定的方式（通常为 UTF-8 或默认的 OEM codepage）

## 生命周期函数

DLL 加载和卸载时，会调用以下函数。

### loadu 函数

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

用于初始化模块的函数。<br />
第 1 个参数的全局内存中存储着模块目录路径，编码为*UTF-8*。

该函数自 SSP 2.6.92 (2025/1/16) 起实现。在此之前仅实现了 load。

处理示例：

- 将传入的路径设为当前目录，并读取所需的数据文件
- 初始化模块运行所需的资源
- 根据需要初始化日志文件或数据库

注意事项：

- 即使不需要字符串数据，也必须释放传入的全局内存
- 初始化成功时返回 TRUE，失败时返回 FALSE
- baseware 会优先使用此函数

#### load 函数

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

loadu 函数的旧版。<br />
除第 1 个参数中的模块目录路径使用默认 OEM codepage（在日语环境中为 CP932）编码外，其规范与 loadu 函数相同。

注意事项：

- 未实现 loadu 函数时，将使用此函数作为回退
- 为确保兼容性，建议同时实现 load 和 loadu；如果 loadu 已完成初始化后又调用 load，则忽略该调用
- 为支持 Unicode，需要将接收的路径转换为适当的宽字符串

#### unload 函数

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

用于结束模块运行的函数。模块卸载时由 baseware 调用。

应实现的处理：

- 释放通过 CreateFile 等函数打开的文件句柄
- 释放通过 CreateMutex 等函数创建的同步对象
- 等待通过 CreateThread 等函数创建的线程结束，并执行后续清理
- 释放模块分配的所有其他系统资源

当前不会使用返回值，但考虑到将来的扩展性，建议返回 TRUE。
