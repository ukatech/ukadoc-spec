# `\![execute,install,url,URL,種別]`

**カテゴリ:** 未分類命令

下載指定 URL 的檔案，並依類型執行安裝／註冊處理。<br />
檔案會自動下載至暫存檔資料夾，並視情況執行安裝處理。<br />
透過此標籤執行的下載處理不會觸發 OnURLQuery。

類型可省略。若省略，會根據 Content-Type 和檔案內容自動判別。

- nar……以 nar 檔案安裝
- feed……註冊為[headline sensor](../../../descript/install/install-txt/type.md)（RSSFeed）
- homeurl……將該 URL 視為 homeurl，並執行 network update
- ical……註冊為訂閱 iCal（.ics）的[行程 sensor](../../../descript/install/install-txt/type.md)。會在行事曆資料夾中自動建立 descript.txt，之後會成為顯示行事曆及[OnScheduleTodayNotify](../../shiori-event/calendar/OnScheduleTodayNotify.md)的對象
- ssf……以 SSF 檔案取得，並播放對話

**対応:** SSP

## 記述例

```sakurascript
\![execute,install,url,http://ssp.shillest.net/ghost/emily4.nar,nar]Emily/Phase4.5のnarをダウンロードしてきてインストールする。
```
