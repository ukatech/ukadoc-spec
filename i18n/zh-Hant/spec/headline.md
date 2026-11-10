# HEADLINE/2.0

最後修改：2013-08-07

參考：[HEADLINE/1.1](http://usada.sakura.vg/contents/headlinesenser.html)（外部網站）

## 前言

HEADLINE/2.0 是舊版規格（1.1）的修訂版。目前只有 SSP 實作。

主要變更是新增字元編碼指定。

## HEADLINE 的實體

需要兩個檔案：「descript.txt」和匯出 execute 函式的 dll 檔案。

## DLL

請參閱[DLL 頁面](dll.md)。

## request - response 1: 取得 version

### request 範例

```
GET Version HEADLINE/2.0
Charset: UTF-8
Sender: SSP
```

### request 標頭詳細資訊

- **Charset**: 字元編碼
- **Sender**: 事件傳送來源

### response 範例

```
HEADLINE/2.0 200 OK
Charset: UTF-8
Value: HeadlineModule 1.1
```

### response 標頭詳細資訊

- **Charset**: \[可省略\]字元編碼。省略時使用呼叫端指定的編碼。
- **Value**: \[可省略\]版本字串

## request - response 2: 取得 HEADLINE

### request 範例

```
GET Headline HEADLINE/2.0
Charset: UTF-8
Sender: SSP
Option: url
Path: C:\SSP\temp\ad9326dc37cb86a9.html
```

### request 標頭詳細資訊

- **Charset**: 字元編碼
- **Sender**: 事件傳送來源
- **Option**: \[可省略\]可在 response 中解析的選項。以逗號分隔列出。<br />
  目前只有 url。請參閱 response 的 Headline 標頭一節。
- **Path**: HEADLINE 解析目標檔案的完整路徑。

### response 範例

```
HEADLINE/2.0 200 OK
Charset: UTF-8
Headline: ほげほげ1
Headline: ほげほげ2
Headline: ほげほげ3
Headline: ほげほげ4
Headline: ほげほげ5
```

### response 標頭詳細資訊

- **Charset**: \[可省略\]字元編碼。省略時使用呼叫端指定的編碼。
- **RequestCharset**: \[可省略\]下次呼叫時希望使用的字元編碼。省略時使用 Charset。
- **Headline**: HEADLINE 的內容。<br />
  呼叫時若在 Option 標頭中加入 url，例如 Option: url，即支援 URL 擴充功能。<br />
  此時若以位元組值 1 分隔，並以「內容\[1\]URL」的格式回應，URL 也會通知 ghost；如果 ghost 端支援，點選項目後可能可以跳至該項目的詳細頁面等。<br />
  請注意，回傳的不是 Sakura Script 片段，不能使用標籤。請回傳一般純文字。

## descript.txt

請參閱[Headline 設定頁面](../descript/headline/index.md)。

## SHIORI Event

詳細資訊請參閱[SHIORI Event 頁面](../list/shiori-event/index.md)。

- **[OnHeadlinesenseBegin](../list/shiori-event/headline-rss/OnHeadlinesenseBegin.md)**: HEADLINE 感測開始時。
- **[OnHeadlinesense.OnFind](../list/shiori-event/headline-rss/OnHeadlinesense.OnFind.md)**: 有要朗讀的內容時。
- **[OnHeadlinesenseComplete](../list/shiori-event/headline-rss/OnHeadlinesenseComplete.md)**: HEADLINE 感測正常結束時。
- **[OnHeadlinesenseFailure](../list/shiori-event/headline-rss/OnHeadlinesenseFailure.md)**: HEADLINE 感測失敗時。

## 補充

GET Headline 會呼叫兩次。第一次針對舊檔案，第二次針對新檔案。不過，舊檔案到新檔案的順序可能會依實作而顛倒，因此不可撰寫依賴順序的處理。

若要在除錯期間等情況下持續顯示（不會變成 no update），請試著在 descript.txt 中寫入 alwaysdisplay,1（除錯結束後務必移除）。
