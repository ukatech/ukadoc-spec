# `\![execute,install,url,URL,種別]`

**カテゴリ:** 未分类命令

下载指定 URL 的文件，并根据类型执行安装或注册处理。<br />
文件会自动下载到临时文件文件夹，并根据需要执行安装处理。<br />
通过此标签执行的下载处理不会触发 OnURLQuery。

类型可以省略。省略时，根据 Content-Type 和文件内容自动判断。

- nar……作为 nar 文件安装
- feed……注册为[标题传感器](../../../descript/install/install-txt/type.md)（RSSFeed）
- homeurl……将该 URL 视为 homeurl 并执行网络更新
- ical……注册为订阅 iCal（.ics）的[日程传感器](../../../descript/install/install-txt/type.md)。将在日历文件夹中自动生成 descript.txt，此后会作为日历显示和[OnScheduleTodayNotify](../../shiori-event/calendar/OnScheduleTodayNotify.md)的处理对象
- ssf……作为 SSF 文件获取并播放对话

**対応:** SSP

## 記述例

```sakurascript
\![execute,install,url,http://ssp.shillest.net/ghost/emily4.nar,nar]Emily/Phase4.5のnarをダウンロードしてきてインストールする。
```
