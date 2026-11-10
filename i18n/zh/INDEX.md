# UKADOC 首页

## 关于 ukadoc

由伺か（Ukagaka）相关规格文档汇总项目 [UKADOC project](https://github.com/ukatech/ukadoc-spec) 编辑的文档集。

*[SSP](http://ssp.shillest.net/)相关文档以本站文档作为官方文档*。

如需指出错误、提问、发表意见或需求，或提供信息，请前往[ばぐとら研究所ToDo](http://ssp.shillest.net/bts/?project=misc&action=top)。

本站文章采用[知识共享署名 4.0 国际许可协议（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/deed.ja)。无论是否用于 ghost 制作，均可自由引用、转载和修改。使用时，请注明「原著作者」，即标注本项目（UKADOC project）的名称或本站链接。

> 本站提供了将本站 HTML、CSS、JS 和图片文件打包而成的 [ukadoc-spec-offline.zip](https://ukatech.shillest.net/ukadoc-spec/ukadoc-spec-offline.zip)，可供离线阅读。解压后可从 `ukadoc-spec/index.html` 开始阅读。
>
> 本站为 AI 代理提供了查找指南 [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt)。每个页面的 Markdown 原稿可通过与仓库相同路径的 `.md` 文件获取（例如：`https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`）。

## 目标版本

- [SSP](http://ssp.shillest.net/) 最新版（官方规格文档）
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2（开发版）
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) 最近版本

## 外部链接

- [伺か（Ukagaka）开发信息搜索](http://ukadev.shillest.net/)
- [SSP 启动选项（SSP 帮助）](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [伺か（Ukagaka）官方规格文档](http://usada.sakura.vg/contents/specification.html)
- [CROW・SSP 规格文档](http://crow.aqrs.jp/reference/all/)
- [大八州.NET 非官方规格文档](http://www.ooyashima.net/db/)
- [駄でべwiki 规格备忘](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## 如何阅读 ukadoc

侧边栏中的文章按类别分别介绍以下内容。

- **文件结构**：介绍构成各类伺か（Ukagaka）相关内容的文件，以及目录结构。

  如果想了解需要哪些文件、可以使用哪些文件的整体情况，可参考此处。

- **设置文件**：介绍各类伺か（Ukagaka）相关内容所用的单个设置文件的具体写法。

  编写各个设置文件时可参考此处。文档尽可能提供了示例。

- **Sakura Script**：介绍用于指示 ghost 执行动作的「Sakura Script」中的各项命令。

  可参考此处了解有哪些命令，以及如何使用这些命令。

- **事件**：介绍 baseware 向 SHIORI 或 PLUGIN 等发送通知的各个事件 ID。

  制作 ghost、PLUGIN、SHIORI 等内容时，如果想了解各个事件及其 Reference，可参考此处。

- **规格**：汇总各种与伺か（Ukagaka）相关内容有关的规格。

  这里的信息主要涉及 SHIORI、SAORI、baseware 等系统的核心部分。

- **HowTo**：介绍创建各类伺か（Ukagaka）相关内容的基础方法。

  但要涵盖针对各种具体情况的 TIPS 并不现实；如果需要更具体的信息，请尝试查找外部网站。

- **其他**：其他内容，例如有关 SSP 等 baseware 规格的备忘和补充文章。

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

- [制作分发文件](dev/nar.md)
- [支持网络更新](dev/update.md)
- [制作 shell](dev/shell.md)
- [设置 dressup](dev/bind.md)
- [设置 owner draw 菜单](dev/ownerdraw.md)
- [解决错误消息](dev/shell-error.md)

### 其他

- [补充：什么是 SHIORI Event](memo/shiori-event.md)
- [备忘](memo/memo.md)
