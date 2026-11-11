# UKADOC 首页

## 关于 ukadoc

这是由伺か相关规范文档汇总项目 [UKADOC project](https://github.com/ukatech/ukadoc-spec) 编辑的文档集。

*关于 [SSP](http://ssp.shillest.net/) 的内容，以此处的文档作为官方文档*。

如需指出错误、提出问题、意见或需求，或提供信息，请联系[ばぐとら研究所ToDo](http://ssp.shillest.net/bts/?project=misc&action=top)。

如果想提议添加或修改新规范或事件，但不熟悉 GitHub 或 git 的操作，则无需创建拉取请求。只要在[ばぐとら研究所ToDo](http://ssp.shillest.net/bts/?project=misc&action=top)或 [GitHub Issue](https://github.com/ukatech/ukadoc-spec/issues)中提交详细内容，我们就会处理。

管理员：[UKADOC Project](https://github.com/ukatech/ukadoc-spec)

用于链接的横幅：

![ukadoc 横幅](assets/image/ukadoc_banner1.png)

本站内容可依据[知识共享署名 4.0 国际版（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/deed.ja)使用。无论是否用于制作 ghost，均可自由引用、转载和修改。使用时，请注明「原作者」为本项目（UKADOC project），或提供本站链接。

> 本站提供归档文件 [ukadoc-spec-offline.zip](https://ukatech.shillest.net/ukadoc-spec/ukadoc-spec-offline.zip)，其中包含本站的 HTML、CSS、JS 和图像文件，可供离线阅读。解压后可从 `ukadoc-spec/index.html` 开始阅读。
>
> 我们为 AI 代理提供了查找指南 [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt)。各页面的 Markdown 原稿可通过与仓库中相同路径的 `.md` 文件获取（例如：`https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`）。

## 目标版本

- [SSP](http://ssp.shillest.net/) 最新版（官方规范书）
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2（开发版）
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) 最近版本

## 外部链接

- [伺か开发信息搜索](http://ukadev.shillest.net/)
- [SSP 启动选项（SSP 帮助）](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [伺か官方规范书](http://usada.sakura.vg/contents/specification.html)
- [CROW・SSP 规范书](http://crow.aqrs.jp/reference/all/)
- [大八州.NET　非官方规范书](http://www.ooyashima.net/db/)
- [駄でべwiki　规范备忘](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## 如何阅读 ukadoc

侧边栏中的文章按类别分别介绍以下内容。

- **文件结构**：介绍构成各类伺か相关内容的文件，以及目录结构。

  如果想了解需要或可以使用哪些文件的整体情况，可参考此处。

- **设置文件**：介绍各类伺か相关内容所使用的各个设置文件的内容。

  编写各个设置文件时可参考此处。我们也尽可能提供了示例。

- **Sakura Script**：介绍作为 ghost 动作指令的「Sakura Script」中的各条命令。

  可在了解能够使用哪些命令，以及实际使用时参考此处。

- **事件**：介绍 baseware 向 SHIORI、PLUGIN 等发送通知的各个事件 ID。

  制作 ghost、PLUGIN、SHIORI 等内容时，如果想了解各个事件及其 Reference，可参考此处。

- **规范**：汇总与各类伺か相关内容有关的各种规范。

  主要涉及 SHIORI、SAORI、baseware 等系统的核心部分。

- **HowTo**：介绍制作各类伺か相关内容时的基本方法。

  但要涵盖针对个别情况的所有技巧，实际上并不现实。如果需要更具体的信息，请尝试搜索外部网站。

- **其他**：其他与 SSP 等 baseware 规范有关的备忘和补充文章。

## 目次

### 文件结构

- [整体结构](manual/directory.md)
- [ghost](manual/ghost.md)
- [shell](manual/shell.md)
- [owner draw 菜单](manual/owner-draw-menu.md)
- [安装](manual/install.md)
- [网络更新](manual/update.md)
- [转换器](manual/translator.md)
- [balloon](manual/balloon.md)

### 设置文件

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

### 规范

- [SHIORI/3.0](spec/shiori3/index.md)
- [SSTP/1.x](spec/sstp/index.md)
- [SAORI/1.0（外部网站）](http://www.boreas.dti.ne.jp/~sdn/saori.html)
- [SAORI over DirectSSTP](spec/saori-ex/index.md)
- [PLUGIN/2.0](spec/plugin.md)
- [HEADLINE/2.0](spec/headline.md)
- [DLL](spec/dll.md)
- [FMO/Mutex](spec/fmo-mutex/index.md)
- [Web 相关](spec/web/index.md)
- [规范备忘（外部网站）](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

### HowTo

- [创建分发文件](dev/nar.md)
- [支持网络更新](dev/update.md)
- [制作 shell](dev/shell.md)
- [设置 dressup](dev/bind.md)
- [设置 owner draw 菜单](dev/ownerdraw.md)
- [解决错误消息](dev/shell-error.md)

### 其他

- [补充：什么是 SHIORI Event](memo/shiori-event.md)
- [备忘](memo/memo.md)
