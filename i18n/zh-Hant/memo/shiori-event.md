# 補充：什麼是 SHIORI Event

## 關於本頁

本頁概述「SHIORI Event」。

以下文章*並非*SHIORI/3.0的正式規格書，而只是協助理解其概念的大致指南。

個別SHIORI Event的說明，請參閱「[SHIORI Event](../list/shiori-event/index.md)」頁面的列表。

## 目次

- [什麼是 SHIORI Event（栞事件）](shiori-event.md#shiori-event栞イベントとは)
- [Reference（參照）](shiori-event.md#referenceリファレンス)
- [GET 命令與 NOTIFY 命令](shiori-event.md#getコマンドとnotifyコマンド)

## 什麼是 SHIORI Event（栞事件）

[![ghost 是透過 baseware 與 ghost（SHIORI）互動的結果而運作](../assets/image/shiori-event.jpg)](../assets/image/shiori-event.jpg)

*從啟動到 ghost 開始運作*

所謂 ghost 運作（說話、改變表情等），究竟是指什麼呢？

簡單來說，這是由*baseware*（MATERIA、CROW、SSP等）與*SHIORI*（作為 ghost 核心的元件）協作而實現的功能。

SHIORI Event 是理解 baseware 和 SHIORI 在這個過程中各自扮演什麼角色的重要關鍵詞。

在 ghost 的運作過程中，首先開始執行工作的是 baseware。

baseware 首要負責的重要工作，是創造*ghost 說話或活動的時機*。

baseware 會監控時間、滑鼠輸入等各種狀態，並以特定的變化（例如經過１秒或１分鐘，或是滑鼠游標碰到 ghost 等）為契機，向 ghost（其核心 SHIORI）發出通知。

這個通知稱為*SHIORI Event*。

另一方面，SHIORI 從這裡開始工作。SHIORI 收到 SHIORI Event 後，會利用稱為自身辭典的檔案內容等，*建立 ghost 的動作指示*（這個動作指示稱為 Sakura Script）。

接著，SHIORI 將動作指示*傳回給 baseware*，收到指示的 baseware 會讀取其內容，並呈現 ghost 的動作。

就這樣，ghost 每次發生 SHIORI Event 時，都會實際在使用者的螢幕上運作。

反過來說，*SHIORI 在收到 SHIORI Event 之前，無法讓 ghost 運作*。原則上，所有 ghost 的動作都是在 SHIORI Event 中執行的，因此屬於被動行為。

即使乍看之下並非如此，也請注意，許多 ghost 具備的「隨機對話」或「AI對話」功能，在許多 SHIORI 中都是透過處理每秒發出的[OnSecondChange](../list/shiori-event/time/OnSecondChange.md)來實作（這部分終究取決於各 SHIORI 的實作，詳細資訊請參閱各 SHIORI 的文件）。

## Reference（參照）

許多 SHIORI Event 除了 SHIORI Event 的 ID（名稱、種類）之外，也會以*Reference*的形式通知相關資訊。

以 ghost 被點擊時發出的[OnMouseClick](../list/shiori-event/mouse/OnMouseClick.md) ID 為例，Reference 會通知點擊的是哪個 scope（本體側、搭檔側、第三人等）、該 scope 的哪個碰撞區域，以及使用哪個按鈕（右鍵、左鍵、滾輪等）點擊。

例如，SHIORI 可以利用 Reference 為 ghost 的動作增添變化。

以 OnMouseClick 為例，許多 ghost 會根據哪個 scope 的哪個部位被點擊，改變執行的功能或對話。

*所有 Reference 都會被賦予從 0 開始的連續編號*，同一個 ID 的 SHIORI Event 所帶有的 Reference，基本上*總是由相同編號對應相同內容*。

查看[SHIORI Event 列表頁面](../list/shiori-event/index.md)中各 ID 小節所列出的、隨 ID 一同通知的 Reference 清單，或許會更容易理解這一點。

不過，依 ID 而定，Reference 的數量也可能不固定。

例如，在 SHIORI Event 列表頁面中查看[installedghostname](../list/shiori-event/notify/installedghostname.md)這個 SHIORI Event 的 Reference，可以看到編號並未明確標示，而是以「Reference\*」的形式表示。

installedghostname 是在啟動後立即等時機發生的 SHIORI Event，會告知該 baseware 中安裝的所有 ghost 名稱。使用者安裝的 ghost 數量自然各不相同，因此 Reference 的數量也不固定。

即使 Reference 的總數不固定，所有 Reference 都以從 0 開始的連續編號表示，這項原則仍然不變。

## GET 命令與 NOTIFY 命令

[![所有 SHIORI Event 都會以兩種封裝之一送達 SHIORI：附有回郵信封的「GET 命令」，以及沒有回郵信封的「NOTIFY 命令」。](../assets/image/shiori-command.png)](../assets/image/shiori-command.png)

*如果把 SHIORI Event 比喻成郵件……*

事實上，所有 SHIORI Event 不僅有各種不同的 ID，其發出方式也有兩種不同的形式與目的。

其中一種就是前面提到的，作為 ghost 運作時機而發出的 SHIORI Event。

這稱為*GET 命令*，顧名思義，是為了讓 baseware 從 SHIORI 接收（get）動作指示（Sakura Script）等內容而發出的 SHIORI Event。

另一種是稍微特殊的*NOTIFY 命令*；透過 NOTIFY 命令發出的 SHIORI Event，無法讓 ghost 運作。

這是因為即使 SHIORI 對 NOTIFY 命令的 SHIORI Event 傳回動作指示，baseware 也會忽略它。

NOTIFY 命令的目的是向 SHIORI 通知（notify）資訊（Reference）。

SHIORI 收到的資訊，與其說是用於該 SHIORI Event，不如說是可以用來協助 ghost 後續的運作。

前面提到的[installedghostname](../list/shiori-event/notify/installedghostname.md)，就是透過 NOTIFY 命令發出的典型 ID。SHIORI 可以透過其中的 Reference，得知使用者環境中安裝了哪些 ghost。ghost 可以根據這些資訊設計機制，例如「如果安裝了特定 ghost，就在選單中顯示用來呼叫該 ghost 的項目」。

需要注意的是，兩種命令的存在，*並不代表*所有 SHIORI Event ID 會被分成兩個「群組」。

這是因為原則上*所有 ID 的 SHIORI Event 都有可能透過 NOTIFY 或 GET 發出*。命令種類與 ID 種類彼此獨立，本質上沒有依存關係（然而，觀察實際實作時，可以發現某些傾向或規則。詳情請參閱[SHIORI Event 列表頁面](../list/shiori-event/index.md)中的各個小節）。
