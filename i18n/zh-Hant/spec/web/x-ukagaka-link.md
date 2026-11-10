# x-ukagaka-link scheme

\[SSP only at present\] The x-ukagaka-link URL scheme is provided to execute something on a website with one click.<br />
The character encoding must always be UTF-8, and the string must be URL-encoded.<br />
The format is as follows.

- **x-ukagaka-link:type=event&ghost=(ghost name)&info=(additional information)**: Opening the URL fires the [OnXUkagakaLinkOpen](../../list/shiori-event/url-drop/OnXUkagakaLinkOpen.md) event.<br />
  (ghost name) must be the same as the name or sakura.name in descript.txt; (additional information) can be any string.<br />
  Sample: [x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)
- **x-ukagaka-link:type=install&url=(encoded URL)**: Opening the URL installs the NAR file at the specified URL.<br />
  (encoded URL) is the URL-encoded location of the NAR file.<br />
  Sample: [x-ukagaka-link:type=install&url=http%3A%2F%2Fssp.shillest.net%2Fghost%2Fbonsyou.nar](x-ukagaka-link:type=install&url=http%3A%2F%2Fssp.shillest.net%2Fghost%2Fbonsyou.nar)
- **x-ukagaka-link:type=homeurl&url=(encoded URL)**: \[2.5.76\] Opening the URL recognizes the specified URL as the update destination, retrieves the file set using the same method as a network update, and then installs it.<br />
  (encoded URL) is the URL-encoded location of the NAR file.<br />
  Sample: [x-ukagaka-link:type=homeurl&url=http%3A%2F%2Fms.shillest.net%2Fghost%2Fghost%2Fmobilemaster%2F](x-ukagaka-link:type=homeurl&url=http%3A%2F%2Fms.shillest.net%2Fghost%2Fmobilemaster%2F)
