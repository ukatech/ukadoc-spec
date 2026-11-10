# 支持网络更新

*如果使用 SSP2.3.00 及更高版本，请注意：如果没有在 owner draw（右键菜单）的“设置”→“本体设置”→“常规”中启用“启用开发者功能”，就无法使用本页介绍的“投放文件夹以创建 updates2.dau”功能。*

本文介绍支持网络更新所需的设置和准备工作。

此外，SSP 不仅支持 ghost 的网络更新，还支持 shell、balloon、plugin 和 headline sensor 的网络更新，本文也会一并介绍。

## 目次

1. [准备服务器](update.md#サーバを用意する)
2. [设置更新用 URL](update.md#更新用urlを設定する)
3. [移除不需要的文件](update.md#不要なファイルを取り除く)
4. [创建 updates2.dau](update.md#updates2dauを作る)
5. [上传到服务器](update.md#サーバにアップロードする)

1. [关于 developer_options.txt](update.md#developer_optionstxtについて)
2. [关于 ghost 发布自动化系统 (GDM)](update.md#ゴースト配布系自動化システムgdmについて)
3. [关于“.dau”被服务器拒绝的情况](update.md#dauがサーバに弾かれてしまう場合について)

第二次及之后的更新，主要是重复执行 3、4、5。

## 准备服务器

首先，准备好网络更新所需的服务器。

使用免费租用服务器即可，例如用于开设个人网站的服务器。

租用服务器（尤其是免费服务）可能会因限制或设置而导致网络更新无法正常进行。

请特别注意以下几点。

- 可以上传所需扩展名的文件。
- 文本文件不会被自动插入广告。

如果要寻找免费租用服务器，以下页面应该可以作为参考。

[駄でべwiki：发布 ghost 的话，选哪里好？（免费空间版）](http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89)（外部网站）

## 设置更新用 URL

基本上，需要在 `descript.txt` 中进行设置。

在 `descript.txt` 中写入以下内容。

```
homeurl,http://xxx.yyy/myghost/
```

这里填写的 URL，是网络上指向包含网络更新内容的文件夹（之后创建 `updates2.dau` 的位置）的 URL。

因此，具体的 URL 取决于服务器。假设该服务器的根目录为 http://xxx.yyy/，而要支持网络更新的 ghost 文件夹（myghost）以如下结构放置在服务器上：

```filetree
+-root
　　+-ukagaka
　　　　+-myghost1
　　　　　　+-ghost
　　　　　　+-shell
　　　　　　+-readme.txt
　　　　　　+-updates2.dau
+-index.html
+-hogehoge.html
+-style.css
:
:
```

那么，descript.txt 中应写入：

```
homeurl,http://xxx.yyy/ukagaka/myghost1/
```

这就是写法。

另外，如果更新内容是 ghost，除了在 `descript.txt` 中填写之外，还可以为 [SHIORI Resource](../list/shiori-resource/index.md) 中的“[homeurl](../list/shiori-resource/ghost/homeurl.md)”指定 URL。

具体来说，在 ghost 一侧使用 SHIORI Resource 指定 homeurl 的方法取决于 SHIORI，因此本文不作介绍。请参阅各 SHIORI 的文档。

## 移除不需要的文件

接下来，移除用户不需要的文件。例如：

- 各类 SHIORI 等的存档文件（但如果设置初始值等需要这些文件，则应保留）
- 所有 profile 文件夹（ghost、shell 内都会生成。SSP 会自动移除）
- 开发工具（Satori 附带的 Satorite、Resebar 等）
- （仅限 MATERIA）目录根目录下的 profile.txt
- desktop.ini 等 Windows 生成的设置文件（SSP 会在一定程度上自动移除）
- 其他开发用词典文件、设置文件、日志文件等

如果使用 SSP，觉得逐一手动移除很麻烦，可以使用 `developer_options.txt`。

详情请阅读[后文的说明](update.md#developer_optionstxtについて)。

如果在*不需要的文件混入其中的状态下进行了更新*，或者在反复更新的过程中*曾经使用过的文件变得不再需要*（例如更改了文件名），该怎么办？

在这种情况下，*仅从服务器删除不需要的文件，并不能删除用户一侧的文件*。

这是因为网络更新会用服务器上的文件覆盖用户一侧的文件，而不是进行同步（镜像）。

要通过网络更新移除已经发布的不需要的文件，请使用 `delete.txt`。

将 `delete.txt` 放在网络更新内容的最上层文件夹中（例如，ghost 的情况下，放在包含 ghost 文件夹、shell 文件夹和 `readme.txt` 等文件的位置；其他情况下，放在包含 descript.txt 的位置）。

配置示例请参阅页面左侧菜单“文件结构”中的“[网络更新](../manual/update.md)”。

## 创建 updates2.dau

接下来创建网络更新用文件（`updates2.dau`）。

这是通过检查服务器端和客户端的文件内容是否一致，来检测损坏、篡改等异常的机制。

使用 MATERIA 或 CROW 创建 `updates2.dau` 时，需要先在最上层目录（例如 ghost 文件夹、shell 文件夹、readme.txt 等所在的位置）创建一个名为 `updates2.dau` 的空文本文件。

SSP 会自动创建该文件。

然后启动 baseware[※](update.md#dauがサーバに弾かれてしまう場合について)，将包含 `updates2.dau` 和待更新文件的文件夹拖放到主程序中。

此时，在 MATERIA 或 CROW 中，如果文件夹内包含 `install.txt`，则会优先创建 nar 文件，导致无法创建 `updates2.dau`，请注意不要将其包含在内。

拖放后，文件夹中应该会创建（如果已存在则保留）一个名为 `updates2.dau` 的文件，且其中应该写入了一些内容。

可以通过右键菜单等方式，用记事本之类的普通文本编辑器打开 `updates2.dau`，请检查其中的内容（不需要理解内容本身）。

## 上传到服务器

到这里，接下来只要使用 FTP 通信软件等将文件上传到服务器即可。

但请注意，通信模式必须设置为*以二进制模式上传所有文件*。

如果以 ASCII 模式上传，网络更新将会失败。

此时，最好在本地的 baseware 中保留「网络更新前」的文件，并在上传后确认网络更新正常完成，这样会更安全。

## 关于 developer_options.txt

使用 SSP 创建归档或 `updates2.dau` 时，可以在最上层目录（创建归档时放置 install.txt 的位置）准备一个名为 `developer_options.txt` 的文件，以设置要处理的文件。

有关写法的说明和示例，请参阅[Install/Update设置页面中关于developer_options.txt的章节](../descript/install/developer_options.txt/index.md)。

请注意，该文件仅在使用 SSP 创建归档或 `updates2.dau` 时生效，因此在使用后文所述的[ghost发布自动化系统](update.md#ゴースト配布系自動化システムgdmについて)或其他 baseware 创建这些文件时无效。

## 关于ghost发布自动化系统(GDM)

ghost发布自动化系统(GDM)是一款辅助工具，可以一并完成创建 `updates2.dau`、打包 ghost 归档以及上传到服务器。

安装并正确配置后，本页所述的大部分内容就不再需要手动处理了。

目前，该工具由下文所述的「整备班」发布。

[ghost发布自动化系统](http://ms.shillest.net/#TOOL)

有关更详细的安装和配置说明，请参考以下网站（无需阅读「1」的内容）。

[ghost发布自动化系统(GDM)的使用方法](http://navy.nm.land.to/post/jidouhaihu.html)（[存档](https://web.archive.org/web/20260205013109/http://navy.nm.land.to/post/jidouhaihu.html)）

虽然名称中有「ghost」，但实际上它可以用于打包 shell、balloon 及其他各种内容的归档，并上传网络更新用文件。

此外，对于多个目标（例如 ghost1、ghost2、shell1、shell2、shell3、balloon……），可以分别保存创建归档、网络更新等操作的设置，并选择当时需要执行的操作后一次性运行。

如果管理着大量内容，这会非常有帮助。

初次安装和配置需要处理的事项稍多，会比较麻烦，但只要完成一次，之后就可以一键完成多个内容的网络更新和归档更新，非常方便。

不仅如此，它还能彻底防止因创建 `updates2.dau` 后修改文件，或将 FTP 通信设置为 ASCII 模式后上传等失误导致的 md5 不一致错误。

当然，通过适当配置，它也能很好地帮助防止混入不需要的文件。

如前文所述，[developer_options.txt](update.md#developer_optionstxtについて)是使用 SSP 的功能创建 nar 或 `updates2.dau` 时生效的配置文件，因此请注意，使用 GDM 创建时与它无关。

不过，GDM 本身就可以设置要上传或不上传的文件，所以通常不需要此文件。

## 关于服务器拒绝「.dau」文件的情况

根据租用服务器的设置，有时可能无法处理扩展名陌生的「.dau」文件。

遇到这种情况时，可以用 `updates.txt` 代替。

使用方法是将本页中出现的所有「`updates2.dau`」替换为「`updates.txt`」。

!!! tip "提示"

    - **[※1 baseware](update.md#updates2dauを作る)**: 指 SSP、MATERIA（本家伺か）、CROW 等用于运行 ghost 的基础软件。
