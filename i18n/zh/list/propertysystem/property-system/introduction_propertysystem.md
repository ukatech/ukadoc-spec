# 属性系统

## 概述

属性系统是一种机制，允许ghost访问并读写baseware运行时持有的各种参数。

- [参考：CROW 测试项目资料](http://crow.aqrs.jp/devtest.html)

## 記述例

使用属性系统有两种方式：环境变量和普通标签。<br />
另请参阅Sakura Script和环境变量中的属性系统相关章节。

- **[%property\[属性名\]](../../sakura-script/environment-variable/pct-property.md)**：将属性作为环境变量引用，并嵌入其值。<br />
  用于直接显示属性值。<br />
  以下示例会将baseware的名称和版本嵌入当前位置（并显示）。

  ```
  %property[baseware.name] ver,%property[baseware.version]
  ```

- **[`\![get,property,事件名,属性名]`](../../sakura-script/property-system-operation/bang-get-property.md)**：通过Sakura Script标签触发任意名称的SHIORI Event，并通过其Reference获取属性。<br />
  用于根据属性在SHIORI侧执行操作。<br />
  以下示例会触发ID为「OnGetSakuraName」的SHIORI Event，并通过其reference0通知ghost「Emily/Phase4.5」的搭档名称（Teddy）。

  ```
  \![get,property,OnGetSakuraName,ghostlist(Emily/Phase4.5).keroname]
  ```

- **[`\![set,property,属性名,值]`](../../sakura-script/property-system-operation/bang-set-property.md)**：通过Sakura Script标签改写属性。<br />
  并非所有属性都允许写入，但本页面中标有*\[SET有效\]*的项目可以通过这种方式操作。<br />
  以下示例会将shell「ULTIMATE FORM」从owner draw菜单中的shell切换菜单里隐藏。

  ```
  \![set,property,currentghost.shelllist(ULTIMATE FORM).menu,hidden]
  ```
