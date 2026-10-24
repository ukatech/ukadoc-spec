# OnXUkagakaLinkOpen

**カテゴリ:** URLドロップイベント

下記形式のWeb関連づけを開いた、またはドロップした場合に、指定したゴーストに通知される。<br />
x-ukagaka-link:type=event&ghost=(descript.txtの"name"か"sakura.name")&info=(Reference0に入る文字列)<br />
文字コードはUTF-8固定＋URLエンコード済<br />
サンプル：[x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)<br />
*SecurityLevelは必ずexternalになる。*

- **Reference0**: info=以降に指定した文字列(URLデコード済)

**対応:** SSP
