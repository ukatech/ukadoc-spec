# x-ukagaka-link scheme

\[目前仅限SSP\] 为了通过单击在网站上执行某些操作，提供了名为 x-ukagaka-link 的URL scheme。<br />
字符编码必须为UTF-8，且内容必须是URL编码后的字符串。<br />
格式如下。

- **x-ukagaka-link:type=event&ghost=(ghost name)&info=(additional information)**: 打开URL时会触发[OnXUkagakaLinkOpen](../../list/shiori-event/url-drop/OnXUkagakaLinkOpen.md)事件。<br />
  (ghost name)应与descript.txt的name或sakura.name相同，(additional information)中可以填写任意字符串。<br />
  示例：[x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)
- **x-ukagaka-link:type=install&url=(encoded URL)**: 打开URL时，会安装指定URL上的NAR文件。<br />
  (encoded URL)是经过URL编码的NAR文件所在位置。<br />
  示例：[x-ukagaka-link:type=install&url=http%3A%2F%2Fssp.shillest.net%2Fghost%2Fbonsyou.nar](x-ukagaka-link:type=install&url=http%3A%2F%2Fssp.shillest.net%2Fghost%2Fbonsyou.nar)
- **x-ukagaka-link:type=homeurl&url=(encoded URL)**: \[2.5.76\] 打开URL时，会将指定URL识别为更新目标URL，并以与网络更新相同的方式获取文件后进行安装。<br />
  (encoded URL)是经过URL编码的NAR文件所在位置。<br />
  示例：[x-ukagaka-link:type=homeurl&url=http%3A%2F%2Fms.shillest.net%2Fghost%2Fghost%2Fmobilemaster%2F](x-ukagaka-link:type=homeurl&url=http%3A%2F%2Fms.shillest.net%2Fghost%2Fmobilemaster%2F)
