# OnXUkagakaLinkOpen

**カテゴリ:** URL拖放事件

打开或拖放下述格式的Web关联链接时，会通知指定的ghost。<br />
x-ukagaka-link:type=event&ghost=(descript.txt中的"name"或"sakura.name")&info=(放入Reference0的字符串)<br />
字符编码固定为UTF-8，且已进行URL编码<br />
示例：[x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)<br />
*SecurityLevel必定为external。*

- **Reference0**: info=之后指定的字符串（已进行URL解码）

**対応:** SSP
