# FMO (File Mapping Object)

所有 baseware 在运行期间都会持有一个命名文件映射对象（FMO）。<br />
读取这块进程间共享内存，即可用相对较低的开销获取正在运行的 ghost。<br />
为避免读取到写入过程中尚未完成的信息，使用[FMO用Mutex](fmo-mutex.md)进行互斥控制。请一并确认。

- **FMO的名称和字符编码**: Sakura : 取决于操作系统，在日语操作系统上为 Shift JIS<br />
  SakuraUnicode : 固定为 UTF-8 \[SSP 2.5.26以降～\]
- **FMO的大小**: 最初的4个字节（第0～3字节）表示已分配的FMO大小。<br />
  这不是已写入信息的长度，而是表示FMO自身分配大小的固定值。<br />
  目前该值为小端序的0x00010000，即固定为64KB。<br />
  为确保与其他程序的兼容性，目前不考虑更改大小。
- **数据主体**: 从第4个字节起是FMO的数据主体，格式如下。<br />
  (32字节的识别ID).(键名)\[`\1`\]值\[`\r\n`\]<br />
  \[`\1`\]是字节值1，\[`\r\n`\]是CR+LF（换行）。<br />
  按此格式重复多行。
- **数据终止符**: 数据终止符与C语言字符串相同，是字节值0。<br />
  因此，数据主体可用的最大大小为65531字节（65536 - 4 - 1）。<br />
  如果需要写入FMO，请注意在可能超过大小上限时，不要写入不完整的信息。<br />
  如果可能超过大小上限，最好不要写入其中一整组数据；即使无法做到这一点，也请确保不要在一行中途结束。

## 数据主体示例

```
ssp_fmo_header_00004468_000f0dea.path[\1]D:\ssp\
ssp_fmo_header_00004468_000f0dea.hwnd[\1]986602
ssp_fmo_header_00004468_000f0dea.name[\1]ラーシェ
ssp_fmo_header_00004468_000f0dea.keroname[\1]ティセ
ssp_fmo_header_00004468_000f0dea.sakura.surface[\1]0
ssp_fmo_header_00004468_000f0dea.kero.surface[\1]10
ssp_fmo_header_00004468_000f0dea.kerohwnd[\1]1052114
ssp_fmo_header_00004468_000f0dea.hwndlist[\1]986602,1052114
ssp_fmo_header_00004468_000f0dea.ghostpath[\1]D:\ssp\ghost\DE10_3001\
ssp_fmo_header_00004468_00120da6.path[\1]D:\ssp\
ssp_fmo_header_00004468_00120da6.hwnd[\1]1183142
ssp_fmo_header_00004468_00120da6.name[\1]Emily
ssp_fmo_header_00004468_00120da6.keroname[\1]Teddy
ssp_fmo_header_00004468_00120da6.sakura.surface[\1]20
ssp_fmo_header_00004468_00120da6.kero.surface[\1]10
ssp_fmo_header_00004468_00120da6.kerohwnd[\1]1117626
ssp_fmo_header_00004468_00120da6.hwndlist[\1]1183142,1117626,921002,2035340,658950
ssp_fmo_header_00004468_00120da6.ghostpath[\1]D:\ssp\ghost\emily4\
```

- **32字节的识别ID**: 表示一组ghost的唯一识别ID。至少需要选择一个在FMO内不会与其他ID重复的字符串。<br />
  常见做法是组合某些唯一信息后计算MD5哈希，或者组合HWND（窗口句柄）。<br />
  Materia的规范没有规定长度，但为确保兼容性，应固定为32字节。

- **键名和值**: 表示信息类型的键和信息主体。如下所示。

  - **path**: 正在运行的baseware根文件夹的完整路径。
  - **hwnd**: 主窗口的窗口句柄。使用十进制表示。
  - **name**: 与descript.txt中的sakura.name相同。
  - **keroname**: 与descript.txt中的kero.name相同。
  - **sakura.surface**: `\0`侧当前显示的surface ID。使用十进制表示。
  - **kero.surface**: `\1`侧当前显示的surface ID。使用十进制表示。
  - **kerohwnd**: `\1`侧窗口的窗口句柄。使用十进制表示。\[SSPのみ\]
  - **hwndlist**: 以逗号分隔列出当前使用的所有窗口句柄。使用十进制表示。\[SSPのみ\]
  - **ghostpath**: 正在运行的ghost的完整路径。\[SSPのみ\]
  - **fullname**: 正在运行的ghost的descript.txt中的name条目。\[SSP 2.5.58～\]
  - **modulestate**: 以逗号分隔的字符串，表示正在运行的ghost已加载的模块状态。\[SSP 2.5.79～\]<br />
    shiori:running 表示已加载SHIORI（未加载时，该字符串本身不存在）<br />
    makoto-ghost:running 表示已加载ghost侧的MAKOTO<br />
    makoto-shell:running 表示已加载shell侧的MAKOTO<br />
    compatible:running 表示已切换到兼容模式，并已加载script.txt等文件<br />
    如果SSP与各模块之间的通信异常，会用critical代替running<br />
    示例： ssp_fmo_header_00004468_00120da6.modulestate\[`\1`\]shiori:running,makoto-ghost:running\\r\\n
