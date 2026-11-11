# UKADOC 首页

## 关于 ukadoc

这是由伺か相关规格文档汇总项目[UKADOC project](https://github.com/ukatech/ukadoc-spec)编辑的文档集。

*[SSP](http://ssp.shillest.net/)相关内容以此处的文档作为官方文档*。

如需指出错误、提问、发表意见或建议、提供信息等，请联系[ばぐとら研究所待办事项](http://ssp.shillest.net/bts/?project=misc&action=top)。

管理员：[UKADOC Project](https://github.com/ukatech/ukadoc-spec)

链接用横幅：

![ukadoc横幅](assets/image/ukadoc_banner1.png)

本站文章依据[知识共享署名 4.0 国际（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/deed.ja)许可使用。不仅限于 ghost 制作，引用、转载和改编均可自由进行。此时请注明「原作者署名」，即本项目（UKADOC project）的名称，或本站链接。

> 我们提供了[ukadoc-spec-offline.zip](https://ukatech.shillest.net/ukadoc-spec/ukadoc-spec-offline.zip)，其中打包了本站的 HTML、CSS、JS 和图像，供离线阅读。解压后可从 `ukadoc-spec/index.html` 阅读。
>
> 我们为 AI agent 提供了查找指南 [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt)。各页面的 Markdown 原稿可通过与仓库相同路径下的 `.md` 获取（例如：`https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`）。

## 目标版本

- [SSP](http://ssp.shillest.net/) 最新版（官方规格书）
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2（开发版）
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) 最近版本

## 外部链接

- [伺か开发信息搜索](http://ukadev.shillest.net/)
- [SSP 启动选项（SSP 帮助）](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [伺か官方规格书](http://usada.sakura.vg/contents/specification.html)
- [CROW・SSP 规格书](http://crow.aqrs.jp/reference/all/)
- [大八州.NET　非官方规格书](http://www.ooyashima.net/db/)
- [駄でべwiki　规格备忘](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## 如何阅读 ukadoc

侧边栏中的文章按类别分别介绍以下内容。

- **文件结构**：介绍构成各类伺か相关内容的文件，以及目录结构。

  在想要了解需要哪些文件、可以使用哪些文件的整体情况时，可参考此处。

- **配置文件**：介绍各类伺か相关内容所使用的各个配置文件的书写内容。

  在编写各个配置文件时可参考此处。我们也尽可能准备了示例。

- **Sakura Script**：介绍作为 ghost 动作指令的「Sakura Script」中的各项命令。

  在想要了解可使用哪些命令并实际使用时，可参考此处。

- **事件**：介绍 baseware 向 SHIORI、PLUGIN 等通知的各个事件 ID。

  制作 ghost、PLUGIN、SHIORI 等时，如果想了解各个事件及其 Reference，可参考此处。

- **规格**：汇总各类伺か相关内容涉及的各种规格。

  主要是与 SHIORI、SAORI、baseware 等系统核心部分相关的信息。

- **HowTo**：介绍制作各类伺か相关内容的基础方法。

  但是，要涵盖针对具体个别情况的 TIPS 在现实中较为困难，因此如需更具体的信息，请查找外部网站。

- **其他**：其他内容，例如有关 SSP 等 baseware 规格的备忘和补充文章。

## 目次

### 文件结构

- [整体结构](manual/directory.md)
- [ghost](manual/ghost.md)
- [shell](manual/shell.md)
- [owner draw 菜单](manual/owner-draw-menu.md)
- [安装](manual/install.md)
- [network update](manual/update.md)
- [转换器](manual/translator.md)
- [balloon](manual/balloon.md)

### 配置文件

- Ghost
  - [descript.txt](descript/ghost/index.md)
- Shell
  - [descript.txt](descript/shell/index.md)
  - [surfaces.txt](descript/shell-surfaces/index.md)
  - [surfacetable.txt](descript/shell-surfacetable/index.md)
- Balloon
  - [descript.txt](descript/balloon/index.md)
  - [balloon(s/k)\*s.txt](descript/balloon/balloonsoption/index.md)
- Plugin
  - [descript.txt](descript/plugin/index.md)
- Headline
  - [descript.txt](descript/headline/index.md)
- Install/Update
  - [install.txt](descript/install/index.md)
  - [delete.txt](descript/install/delete.txt/index.md)
  - [developer_options.txt](descript/install/developer_options.txt/index.md)
  - [updates2.dau/updates.txt](spec/update-file/index.md)

### Sakura Script

- [SAKURA Script](list/sakura-script/index.md)
- [Property System](list/propertysystem/index.md)

### 事件

- SHIORI
  - [SHIORI Event](list/shiori-event/index.md)
  - [SHIORI Event（外部）](list/shiori-event-ex/index.md)
  - [SHIORI Resource](list/shiori-resource/index.md)
- PLUGIN
  - [PLUGIN Event](list/plugin-event/index.md)

### 规格

- [SHIORI/3.0](spec/shiori3/index.md)
- [SSTP/1.x](spec/sstp/index.md)
- [SAORI/1.0（外部网站）](http://www.boreas.dti.ne.jp/~sdn/saori.html)
- [SAORI over DirectSSTP](spec/saori-ex/index.md)
- [PLUGIN/2.0](spec/plugin.md)
- [HEADLINE/2.0](spec/headline.md)
- [DLL](spec/dll.md)
- [FMO/Mutex](spec/fmo-mutex/index.md)
- [Web 相关](spec/web/index.md)
- [规格备忘（外部网站）](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

### HowTo

- [制作分发用文件](dev/nar.md)
- [支持 network update](dev/update.md)
- [制作 shell](dev/shell.md)
- [dressup 设置](dev/bind.md)
- [owner draw 菜单设置](dev/ownerdraw.md)
- [解决错误消息](dev/shell-error.md)

### 其他

- [补充：关于 SHIORI Event](memo/shiori-event.md)
- [备忘](memo/memo.md)
