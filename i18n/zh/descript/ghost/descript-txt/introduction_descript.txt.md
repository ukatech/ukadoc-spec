# descript.txt（Ghost的）

## 概要

ghost的基本设置文件。<br />
可用于设置ghost名称、作者名、shiori设置、balloon基本位置信息、图标等各种信息。

## 記述例与基本写法

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

type、name、sakuraname、keroname、craftman、craftmanw为必填项（SSP中有些项目可以省略）。

如果使用的SHIORI是里々等DLL名称不是「shiori.dll」的项目，请注意不要忘记在shiori中指定DLL名称。

除了在descript.txt中填写homeurl之外，也可以通过响应baseware发出的[SHIORI Resource](../../../list/shiori-resource/ghost/homeurl.md)请求来设置（具体方法取决于SHIORI，此处不作说明）。<br />
原则上只需指定其中一种；如果两种方式都指定，请注意可能会在网站迁移时忘记修改其中一处。

另外，以\\或%开头的字符串会被视为Sakura Script或环境变量标签，并因安全风险而被丢弃。若要将这些字符作为普通字符包含在字符串中，必须使用\\\\或\\%等形式进行转义。
