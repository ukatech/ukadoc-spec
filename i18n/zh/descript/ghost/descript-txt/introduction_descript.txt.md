# descript.txt（ghost 的）

## 概述

ghost 的基本配置文件。<br />
可配置 ghost 名称、作者名称、shiori 设置、balloon 的基本位置信息、图标等各种信息。

!!! note "可通过 shell 的 descript.txt 覆盖的项目"
    与 shell 的 `descript.txt` 共有的项目（`sakura.name` / `kero.name`、owner draw 菜单的图像和颜色、balloon 和角色的位置、surface 位置信息、鼠标光标、`don't need ...`、`shiori.logo.*` 等）也可以写在 ghost 的 `descript.txt` 中。<br />
    写在 ghost 侧的项目成为整个 ghost 的默认值；如果 shell 的 `descript.txt` 中有相同项目，则优先使用 shell 侧的值（覆盖默认值）。<br />
    这些项目列在 [shell 设置](../../shell/descript-txt/index.md)中。相应项目注明了“也可以写在 ghost 的 descript.txt 中”。

## 記述例 与基本写法

```
charset,Shift_JIS
type,ghost
name,凡例さん
sakura.name,凡例さん
kero.name,斑糲岩
homeurl,http://ssp.shillest.net/ukadoc/manual/hogehoge/example/

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

shiori,satori.dll
```

type、name、sakuraname、keroname、craftman、craftmanw 为必填项（在 SSP 中部分项目可以省略）。

SHIORI 使用 Satori 等 dll 名称不是「shiori.dll」的程序时，注意不要忘记在 shiori 中指定 dll 名称。

homeurl 除了写在 descript.txt 中，也可以通过响应 baseware 的 [SHIORI Resource](../../../list/shiori-resource/ghost/homeurl.md) 请求来设置（方法因 SHIORI 而异，故省略）。<br />
基本上只需通过其中一种方式指定；如果两种方式都指定，须注意避免在网站迁移等情况下忘记修改其中一处。

另外，以 \\ 或 % 开头的字符串会被视为 Sakura Script 或环境变量的标签，并因安全风险而被丢弃。如果只想将它们作为普通字符使用，必须用 \\\\ 或 \\% 等形式转义。
