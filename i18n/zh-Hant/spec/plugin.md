# PLUGIN/2.0

最後修改：2013-08-10

參考：[PLUGIN/1.0](http://usada.sakura.vg/contents/plugin.html)（外部網站）

## 前言

PLUGIN/2.0是舊版規格（1.0）的修訂版。由SSP實作。

這是仍在整理中的規格，可能會有大幅變更。

## 版本的設計理念與影響評估

### 設計理念

為了方便地與本體或ghost互動而進行改修，並整合SAORI群中分散在各個ghost的「便利功能」，改善使用者的便利性。

將負擔從plugin開發者轉移到執行環境會比較好……大概。

### 處理系統

由於前提是將各種負擔轉移到處理系統，請做好心理準備（苦笑）。

### Plugin作者

由於會新增用於呼叫的request匯出，不必考慮與PLUGIN/1.0衝突。

向ghost通知指令碼或事件等會變得非常容易。

### Ghost作者

即使沒有支援特定plugin，也有預設指令碼規格（後述），因此不會造成致命問題。

如果無論如何都不想讓預設指令碼破壞氣氛，就請加以支援……

### 版本的影響評估

能夠集中處理分散在各個ghost的功能群，既方便又省事。

## 實體

需要兩個檔案：「descript.txt」和DLL檔案。

## DLL

請參閱[DLL頁面](dll.md)。

*※YAYA/KAWARI as PLUGIN的使用者及模組作者可以略過。*

## request規定

典型的request範例如下。※換行碼＝CR+LF

```
GET PLUGIN/2.0
ID: OnGhostChange
Charset: UTF-8
Reference0: 54
```

```
NOTIFY PLUGIN/2.0
ID: OnMenuExec
Charset: UTF-8
Sender: 晶子
Reference0: 17982
```

以空行結束。與其他DLL規格相同，請注意不一定會以零結尾。

PLUGIN/2.0的格式基本上遵循SHIORI/3.0規格。<br />
由事件識別碼的ID標頭，以及任意數量（可超過8個）的附加資訊Reference標頭構成。<br />
Reference的內容會依ID而異。

若要在Reference等內容中包含換行等字元，或規定必須包含這些字元，\*強烈建議\*僅將要跳脫的字元以URL編碼後傳送，例如%8f%73（這不是規格要求）。

如果是依照後述的ghost端呼叫規格呼叫，Sender的內容會是ghost名稱。<br />
如果是由本體呼叫，Sender標頭本身會消失，或被指定為空字串。<br />
請注意，這裡不會像SHIORI一樣填入「本體名稱（例如SSP或CROW）」。

關於會收到通知的request類型（ID），請參閱[PLUGIN Event頁面](../list/plugin-event/index.md)。

## response規定

response範例如下。※換行碼＝CR+LF

```
PLUGIN/2.0 200 OK
Charset: Shift_JIS
Target: 54
Event: OnResourceLow
EventOption: notify
Reference0: 19
Reference1: 31
Reference2: 65
Script: すくりぷと～
ScriptOption: nobreak,notranslate
```

※僅限支援多重啟動的處理系統※ 如果目前啟動中的ghost有符合Target的項目，就會由該ghost處理。<br />
指定"\_\_SYSTEM_ALL_GHOST\_\_"時，會通知「所有啟動中的ghost」。

若沒有符合項目或未指定任何項目，會由處理系統選擇適當的「一個」ghost處理。<br />
此外，若是依照後述的ghost端呼叫規格呼叫，除非在Target標頭中明確指定，否則會回傳給發出呼叫的ghost。

※不支援的處理系統本來就只有一個ghost，因此每次都會呼叫該ghost。

### Event/Reference

Event標頭和Reference標頭是傳送給ghost的事件。<br />
如果ghost沒有回應，便會播放作為預設指令碼的Script標頭。

### ScriptOption

ScriptOption是只套用於Script標頭內容的選項。

- **notranslate**: 不經過ghost的翻譯功能
- **nobreak**: 不打斷目前正在播放的對話，等它播放完畢後再執行指定的指令碼

### EventOption

EventOption是只套用於Event標頭內容的選項。

- **notify**: 以notify方式向ghost通知指定事件

Event、EventOption、Reference、Target、Script、ScriptOption都可以省略。<br />
例如，只想傳送事件而不需要預設指令碼時，請省略Script/ScriptOption標頭。<br />
※只想傳送指令碼時則相反。

## Plugin ID

請參閱[Plugin設定中的ID項目](../descript/plugin/descript-txt/id.md)。

## descript.txt

請參閱[Plugin設定頁面](../descript/plugin/index.md)。

## Ghost端擴充

### 指令碼擴充

```
\![raiseplugin,プラグイン名またはID,イベント,Reference0...]
\![notifyplugin,プラグイン名またはID,イベント,Reference0...]
```

向指定的plugin傳送指定事件。除非plugin端指定Target（system_any），否則plugin的response會優先分配給執行raiseplugin的ghost，因此也可以像SAORI一樣使用。

傳送命令方面，[`\![raiseplugin]`](../list/sakura-script/event/bang-raiseplugin-ID-r0-r1-r2.md)會使用GET，[`\![notifyplugin]`](../list/sakura-script/event/bang-notifyplugin-ID-r0-r1-r2.md)會使用NOTIFY。

### SHIORI事件擴充

請參閱[installedplugin項目](../list/shiori-event/notify/installedplugin.md)。
