# x-ukagaka-link scheme

\[目前僅限 SSP\] 為了讓使用者能在網站上以單擊方式執行某些操作，提供了名為 x-ukagaka-link 的 URL scheme。<br />
字元編碼必須使用 UTF-8，且內容必須是經過 URL 編碼的字串。<br />
格式如下。

- **x-ukagaka-link:type=event&ghost=(ghost 名稱)&info=(附加資訊)**：開啟 URL 時會觸發 [OnXUkagakaLinkOpen](../../list/shiori-event/url-drop/OnXUkagakaLinkOpen.md) 事件。<br />
  (ghost 名稱)需與 descript.txt 的 name 或 sakura.name 相同；(附加資訊)可為任意字串。<br />
  範例：[x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)
- **x-ukagaka-link:type=install&url=(已編碼的 URL)**：開啟 URL 時，會安裝指定 URL 中的 NAR 檔案。<br />
  (已編碼的 URL)是經過 URL 編碼的 NAR 檔案位置。<br />
  範例：[x-ukagaka-link:type=install&url=http%3A%2F%2Fssp.shillest.net%2Fghost%2Fbonsyou.nar](x-ukagaka-link:type=install&url=http%3A%2F%2Fssp.shillest.net%2Fghost%2Fbonsyou.nar)
- **x-ukagaka-link:type=homeurl&url=(已編碼的 URL)**：\[2.5.76\] 開啟 URL 時，會將指定的 URL 視為更新目的地 URL，並以與 network update 相同的方式取得檔案群後進行安裝。<br />
  (已編碼的 URL)是經過 URL 編碼的 NAR 檔案位置。<br />
  範例：[x-ukagaka-link:type=homeurl&url=http%3A%2F%2Fms.shillest.net%2Fghost%2Fghost%2Fmobilemaster%2F](x-ukagaka-link:type=homeurl&url=http%3A%2F%2Fms.shillest.net%2Fghost%2Fmobilemaster%2F)
