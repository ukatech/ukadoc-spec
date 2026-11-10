# install.txt

## 概要

也可参考[文件结构「安装」](../../../manual/install.md)页面。

这是用于设置 ghost、balloon、shell 等伺か（Ukagaka）/SSP 内容归档（如 .nar）的安装设置文件。所有归档都可以解压后手动安装，但如果存在正确设置的 install.txt，便可启用安装程序功能，通过拖放归档等简单方式进行安装。

## 記述例与基本写法

ghost 的情况（balloon 和 plugin 也基本相同，只需更改 type 部分）

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
```

追加 shell 的情况

```
charset,Shift_JIS
name,凡例さんアルティメットフォーム
type,shell
directory,ultimate
accept,凡例さん
```

ghost 的补充包（追加文件）的情况

```
charset,Shift_JIS
name,凡例さん猫化パッチ
type,supplement
accept,凡例さん
```

在 ghost 中附带 balloon 的情况

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
balloon.directory,example_balloon
balloon.source.directory,balloon
```

※仅限 SSP　用于同时安装多个内容的软件包时，放在最上层的文件<br />
（每个附带内容中的 install.txt 按通常方式编写即可）

```
charset,Shift_JIS
name,凡例さんファミリー一括入居パッケージ
type,package
```

charset 必须写在第1行（Shift_JIS 时可以省略）。

name 和 type 为必填项。type 不是 supplement 或 package 时，directory 也为必填项。<br />
其他项目可按需指定。

追加 shell 或补充包可使用 accept 设置，以避免安装到非预期的 ghost 上。<br />
尤其是补充包，几乎必须设置，因为存在意外覆盖文件并导致损坏的风险。<br />
请注意，accept 指定的是*主体侧名称*，而不是 ghost 名称。

在 SSP 中，将 balloon 或 plugin 附带到 ghost 或 shell 时，请使用 \*.directory。<br />
详情请参阅[「同时安装」](introduction_install_multi.md)。

此外，name 主要用于在[安装相关 SHIORI Event](../../../list/shiori-event/install/OnInstallComplete.md)的 Reference 中通知相关内容。<br />
有些 ghost 会利用此信息，实现安装后立即切换到安装对象的功能；但如果 descript.txt 中实际 ghost 的 name 与 install.txt 中的名称不同，该切换可能无法正常工作，请注意。
