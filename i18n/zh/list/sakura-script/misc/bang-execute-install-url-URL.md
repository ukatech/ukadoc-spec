# `\![execute,install,url,URL,種別]`

**カテゴリ:** Unclassified command

Download the file at the specified URL and perform the installation/registration process for its type.<br />
The file is automatically downloaded to a temporary files folder, and the installation process is performed as appropriate.<br />
OnURLQuery is not triggered for downloads performed with this tag.

The type is optional. If omitted, it is detected automatically from the Content-Type and the file contents.

- nar……Install as a nar file
- feed……Register as a [headline sensor](../../../descript/install/install-txt/type.md) (RSSFeed)
- homeurl……Treat the URL as homeurl and perform a network update
- ical……Register as a [schedule sensor](../../../descript/install/install-txt/type.md) subscribing to iCal (.ics). A descript.txt is automatically generated in the calendar folder, and the calendar is then eligible for display and [OnScheduleTodayNotify](../../shiori-event/calendar/OnScheduleTodayNotify.md)
- ssf……Fetch as an SSF file and play the talk

**対応:** SSP

## 記述例

```sakurascript
\![execute,install,url,http://ssp.shillest.net/ghost/emily4.nar,nar]Emily/Phase4.5のnarをダウンロードしてきてインストールする。
```
