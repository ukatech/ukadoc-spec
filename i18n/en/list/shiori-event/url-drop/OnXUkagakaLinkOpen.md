# OnXUkagakaLinkOpen

**カテゴリ:** URL drop event

Notifies the specified ghost when a web association in the format below is opened or dropped.<br />
x-ukagaka-link:type=event&ghost=(descript.txt's "name" or "sakura.name")&info=(string passed in Reference0)<br />
Character encoding is fixed to UTF-8, and the string is URL-encoded.<br />
Example: [x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)<br />
*SecurityLevel is always external.*

- **Reference0**: The string specified after info= (URL-decoded)

**対応:** SSP
