# 备忘

## baseware 功能比较

| 功能列表 | MATERIA | SSP | CROW | ninix-kagari |
| --- | --- | --- | --- | --- |
| 控制台 | ○ | × | × | △ |
| 校时 | ○ | ○ | ○ | × |
| headline sensor | ○ | ◎ | ○ | × |
| 邮件检查 | ○ | ○ | ○ | × |
| plugin | ○ | ◎ | × | × |
| 主体更新 | × | △ | ○ | × |
| shell 缩放 | × | ○ | ○ | ○ |
| dressup | △ | ○ | × | △ |
| 日历 | × | ○ | × | × |
| IM | × | ○ | × | × |
| 多开 | △ | ◎ | ○ | ○ |
| ghost 自由移动 | × | ○ | × | × |
| 多个搭档 | × | ○ | × | ○ |

SSP 的 headline sensor 也可以使用 RSS。

SSP 的主体更新仅有检查功能。

有许多 SSP 专用 plugin。

MATERIA583 存在 bug，因此无法为搭档进行 dressup。

MATERIA 可以通过使用多个可执行文件来多开。

SSP 可以在一个进程中启动多个角色。

## 推荐网站的横幅

仅 MATERIA、SSP 支持显示。

将横幅放入\*/ghost/master/banner/文件夹中。

按照各 SHIORI 的格式，在 urllist 中按以下顺序填写

“网站名称” “URL” “横幅文件名（不含扩展名）”

。

## 有关兼容性的制作注意事项和备忘

- 在 MATERIA 中，邮件检查、网络更新计数等从 0 开始计数。

  SSP、CROW 从 1 开始计数。

  在 SSP 中，将 SHIORI Resource 的 useorigin1 设为 0，即可像 MATERIA 一样使用零起始索引。

- 只有 MATERIA 的 surface 编号上限为 8192。

- 在 MATERIA、CROW 中，overlay 使用 pna 时无法正常实现透明效果。

- MATERIA 的 surface 动画等待时间最多只能识别到 10。

  如果要设置更长的等待时间，请重复指定相同的动画。

- 只有 SSP、CROW 可以加载通过 dft/dfp/dgt/dgp 加密的文件。

- SSP 的动画速度稍快（更轻快）。

- SSP 的 inputbox 可以与其他操作同时使用。

- SSP、CROW 的 balloon 也可以使用半透明效果。

  但 inputbox 类控件无法透显。

## 仅限 SSP 的功能

- 可以处理以下图像格式。

  BMP/PNG/JPEG/GIF/MAG/XBM/PI/ICO/CUR

- 可以显示 32bitPNG 透明图像。

- 可以安装以下压缩文件。

  CAB/自解压文件

- surfacetable.txt（替代显示 surface 测试窗口）

  surfaces2.txt（可用于覆盖 SSP 的 surfaces.txt）

  developer_options.txt（在 SSP 中生成 updates2.dau 或 nar 时，用于指定排除文件的文本文件）

- 通过拖放 SSF 文件播放对话。
