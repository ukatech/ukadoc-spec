# 兼容模块

SSP内置了对以下常用SAORI DLL的兼容功能。ghost加载这些DLL时，SSP不会读取DLL，而是替换为内置功能（根据文件名判断）。<br />
\[SSP 2.9.13\] 也可以通过Direct SSTP调用这些功能，调用时使用去掉`.dll`的DLL名（例如`Module: string`）。参数和返回值与原版SAORI相同。

`houchi` `clipcopy` `textcopy` `saori_ip` `saori_cpuid` `mciaudio` `cpuusage` `httpc` `string` `hanayu` `osuwari`（`osuwari`为 \[SSP 2.9.33\]）

- Direct SSTP没有`load` / `unload`，因此，对于按ghost分别维护状态的功能（`mciaudio` / `httpc` / `string` / `hanayu`），会在该ghost首次调用时进行初始化，并在ghost结束时（包括重新加载SHIORI）丢弃状态。这些状态不会与作为DLL加载的实例共享。
- 不带ghost调用时，依赖ghost的处理（`httpc`的获取、保存和`bg`，`hanayu`的`show`，`mciaudio`的`load` / `play` / `loop` / `stop`）会返回400（`ghost required`）。
- `houchi`会在加载时生效，因此从Direct SSTP调用不会产生任何效果。
- Direct SSTP请求由SSP主线程处理，因此请使用`bg`进行`httpc`获取（否则，获取期间SSP画面会停止响应）。

## osuwari \[SSP 2.9.33\]

这是对ukiya氏的`Osuwari.dll`的兼容实现。可使ghost窗口追随前景窗口、指定窗口或屏幕矩形（与[`\![set,alignmenttodesktop,osuwari,…]`](../../list/sakura-script/surface/bang-set-alignmenttodesktop.note.md)执行相同处理，选项含义也见该页面）。参数与原版相同，采用位置参数。

- `START`: 从`Argument1`开始，依次指定控制对象的HWND / 追随目标（`ACTIVE` `FIX` `@标题` `#句柄`） / 原点（`TL` `TR` `BL` `BR`） / x偏移 / y偏移 / 更新间隔（毫秒。0表示100） / (可省略)选项（`XMOVE` `YMOVE` `NOCLIP` `BACK`，以空格分隔。`BACK`表示紧挨着目标窗口后方就座。原版没有此选项） / (可省略)无法就座时的指定（`DESKTOP` `WORKAREA`，以及以空格分隔的`CENTER` `LEFT` `RIGHT` `TOP` `BOTTOM`） / (可省略)裁切边距（`左_上_右_下`）。
  - 省略第7个及之后的参数时，会沿用上一次`START`的值。行为与原版相同。而对于`\![set,alignmenttodesktop,osuwari,…]`，每次都会将省略的选项设为默认值（不会沿用）。
  - 仅可将通过`OnHWND`事件（`hwnd`）通知的**该ghost角色的窗口**指定为控制对象HWND。不会移动其他窗口（找不到时返回500）。
- `STOP`: 停止SAORI设置的就座，并将对齐方式恢复为ghost和shell的默认值（`descript.txt`）。如果`descript.txt`的默认值为osuwari，则会重新就座到osuwari。不会停止通过`\![set,alignmenttodesktop,osuwari,…]`设置的项目。卸载SAORI时（包括重新加载SHIORI）也会停止。
- 成功时返回204；参数不足或无法解析时返回400；找不到控制对象HWND时返回500（`source window is not exist`）。
- 与原版的差异如下。
  - 窗口矩形按照视觉边框测量。
  - 基准屏幕为目标窗口所在的显示器（裁切情况则按所有显示器组成的区域判断）。
  - 没有原版在指定`DESKTOP`时`side`总是变为`TOP`的缺陷。
  - 不会就座到最小化或隐藏的窗口上。
  - shell的`descript.txt`中无需写入`seriko.alignmenttodesktop,free`。
- 改名后的DLL（如`osuwari0.dll`）不属于兼容范围，将会读取真实DLL。
