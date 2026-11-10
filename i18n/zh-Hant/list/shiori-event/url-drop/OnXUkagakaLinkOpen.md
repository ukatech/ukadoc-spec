# OnXUkagakaLinkOpen

**カテゴリ:** URL drop event

Notifies the specified ghost when a web association in the following format is opened or dropped.<br />
x-ukagaka-link:type=event&ghost=(descript.txt "name" or "sakura.name")&info=(string passed in Reference0)<br />
Character encoding is fixed to UTF-8 and URL-encoded.<br />
Sample: [x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)<br />
*SecurityLevel is always external.*

- **Reference0**: String specified after info= (URL-decoded)

**対応:** SSP
