# `\![execute,install,url,URL,種別]`

**カテゴリ:** Uncategorized command

Download the file at the specified URL and perform the installation or registration process appropriate to its type.<br />
The file is automatically downloaded to a temporary-file folder, and installation is performed as appropriate.<br />
OnURLQuery is not raised for downloads performed using this tag.

The type is optional. If omitted, it is detected automatically from the Content-Type and file contents.

- nar……Install as a nar file
- feed……Register as a [headline sensor](../../../descript/install/install-txt/type.md) (RSSFeed)
- homeurl……Treat the URL as homeurl and perform a network update
- ical……Register as a [schedule sensor](../../../descript/install/install-txt/type.md) that subscribes to iCal (.ics). A descript.txt is automatically created in the calendar folder, making the calendar available for display and including it in [OnScheduleTodayNotify](../../shiori-event/calendar/OnScheduleTodayNotify.md) from then on
- ssf……Retrieve as an SSF file and play the talk

**対応:** SSP

## 記述例

```sakurascript
\![execute,install,url,http://ssp.shillest.net/ghost/emily4.nar,nar]Emily/Phase4.5のnarをダウンロードしてきてインストールする。
```
