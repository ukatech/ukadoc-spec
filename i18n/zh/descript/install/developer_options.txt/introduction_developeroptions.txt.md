# developer_options.txt

## 概要

也可参考[文件结构「网络更新」](../../../manual/update.md)和[文件结构「安装」](../../../manual/install.md)。

此文件用于在 SSP 创建归档或网络更新信息文件时，为目标文件设置选项。<br />
SSP 提供将 ghost 等软件包的文件夹拖放到 SSP 上以创建归档（.nar）或 update 文件（updates2.dau）的功能；此文件会在执行该功能时被读取。<br />
因此，原则上如果使用其他工具（如「そだて」或「ghost 分发自动化系统」）创建这些文件，则*完全无关*，请注意。<br />
但也有例外，例如「さとりすと」实现了读取并使用 developer_options.txt 的功能。

## 記述例

```
ghost/master/savedata.txt,noupdate
shell/old/,nonar
ghost/master/profile/,nonar,noupdate
```

## 注意点

请注意，每个目标（文件或文件夹）的设置都要*写在同一行*。例如，如果写成下面这样，*只会应用后面（下方）的设置，nonar 选项将失效*。

```
ghost/master/profile/,nonar
ghost/master/profile/,noupdate
```

如果要指定两个选项，正确写法如前所述：

```
ghost/master/profile/,nonar,noupdate
```

即为如此。
