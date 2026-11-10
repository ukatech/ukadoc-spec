# OnXUkagakaLinkOpen

**カテゴリ:** URL 拖放事件

開啟或拖放下列格式的 Web 關聯連結時，會通知指定的 ghost。<br />
x-ukagaka-link:type=event&ghost=(descript.txt 的「name」或「sakura.name」)&info=(放入Reference0的字串)<br />
字元編碼固定為UTF-8，並已進行URL編碼<br />
範例：[x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)<br />
*SecurityLevel必定為external。*

- **Reference0**: info=之後指定的字串（已進行URL解碼）

**対応:** SSP
