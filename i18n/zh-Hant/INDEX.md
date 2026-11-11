# UKADOC 首頁

## 關於 ukadoc

這是由[UKADOC project](https://github.com/ukatech/ukadoc-spec)編輯的文件集；該專案彙整伺か相關規格文件。

*[SSP](http://ssp.shillest.net/)的相關文件以此處的文件作為官方文件*。

如要指出錯誤、提問、提供意見或需求，或提供資訊等，請前往[ばぐとら研究所ToDo](http://ssp.shillest.net/bts/?project=misc&action=top)。

管理者：[UKADOC Project](https://github.com/ukatech/ukadoc-spec)

連結用的橫幅：

![ukadoc 橫幅](assets/image/ukadoc_banner1.png)

本站文章採用[創用 CC 姓名標示 4.0 國際（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/deed.ja)授權。不限於製作 ghost，歡迎自由引用、轉載及修改。使用時，請標示本專案（UKADOC project）的名稱或本站連結，作為「原著作者的署名」。

> 本站提供將 HTML、CSS、JS 與圖片等所有檔案打包的 [ukadoc-spec-offline.zip](https://ukatech.shillest.net/ukadoc-spec/ukadoc-spec-offline.zip)，可作為離線閱讀用的封存檔。解壓縮後，可從 `ukadoc-spec/index.html` 閱讀。
>
> 本站也提供給 AI 代理程式使用的查找指南 [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt)。各頁面的 Markdown 原稿可透過與儲存庫相同路徑的 `.md` 檔案取得（例如：`https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`）。

## 適用版本

- [SSP](http://ssp.shillest.net/) 最新版（官方規格書）
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2（開發版）
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) 最近版本

## 外部連結

- [伺か開發資訊搜尋](http://ukadev.shillest.net/)
- [SSP 啟動選項（SSP 說明）](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [伺か官方規格書](http://usada.sakura.vg/contents/specification.html)
- [CROW・SSP 規格書](http://crow.aqrs.jp/reference/all/)
- [大八州.NET 非官方規格書](http://www.ooyashima.net/db/)
- [駄でべwiki 規格備忘](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## ukadoc 的閱讀方式

側邊欄中的文章依分類分別介紹以下內容。

- **檔案結構**：說明各種伺か相關內容所需的檔案，以及目錄結構。

  若想掌握需要或可使用哪些檔案的整體概況，可參閱此處。

- **設定檔**：說明各種伺か相關內容所使用的個別設定檔，其記述方式。

  編寫各設定檔時可參閱此處。也盡可能提供範例。

- **Sakura Script**：說明作為 ghost 動作指示的「Sakura Script」各項指令。

  可參閱此處，了解有哪些指令可用，以及如何使用。

- **事件**：說明 baseware 傳送給 SHIORI 或 PLUGIN 等的各個事件 ID。

  製作 ghost、PLUGIN 或 SHIORI 等內容時，若想了解個別事件或其 Reference，可參閱此處。

- **規格**：彙整各種伺か相關內容涉及的各項規格。

  這裡主要是與 SHIORI、SAORI、baseware 等系統核心部分相關的資訊。

- **HowTo**：介紹製作各種伺か相關內容所需的基礎方法。

  不過，實際上很難涵蓋適用於個別情況的 TIPS；若需要更具體的資訊，請另外搜尋外部網站。

- **其他**：其他與 SSP 等 baseware 規格相關的備忘與補充文章。

## 目次

### 檔案結構

- [整體結構](manual/directory.md)
- [ghost](manual/ghost.md)
- [shell](manual/shell.md)
- [owner draw 選單](manual/owner-draw-menu.md)
- [安裝](manual/install.md)
- [network update](manual/update.md)
- [轉換器](manual/translator.md)
- [balloon](manual/balloon.md)

### 設定檔

- Ghost
  - [descript.txt](descript/ghost/index.md)
- Shell
  - [descript.txt](descript/shell/index.md)
  - [surfaces.txt](descript/shell-surfaces/index.md)
  - [surfacetable.txt](descript/shell-surfacetable/index.md)
- Balloon
  - [descript.txt](descript/balloon/index.md)
  - [balloon(s/k)\*s.txt](descript/balloon/balloonsoption/index.md)
- Plugin
  - [descript.txt](descript/plugin/index.md)
- Headline
  - [descript.txt](descript/headline/index.md)
- 安裝／更新
  - [install.txt](descript/install/index.md)
  - [delete.txt](descript/install/delete.txt/index.md)
  - [developer_options.txt](descript/install/developer_options.txt/index.md)
  - [updates2.dau/updates.txt](spec/update-file/index.md)

### Sakura Script

- [SAKURA Script](list/sakura-script/index.md)
- [Property System](list/propertysystem/index.md)

### 事件

- SHIORI
  - [SHIORI Event](list/shiori-event/index.md)
  - [SHIORI Event（外部）](list/shiori-event-ex/index.md)
  - [SHIORI Resource](list/shiori-resource/index.md)
- PLUGIN
  - [PLUGIN Event](list/plugin-event/index.md)

### 規格

- [SHIORI/3.0](spec/shiori3/index.md)
- [SSTP/1.x](spec/sstp/index.md)
- [SAORI/1.0（外部網站）](http://www.boreas.dti.ne.jp/~sdn/saori.html)
- [SAORI over DirectSSTP](spec/saori-ex/index.md)
- [PLUGIN/2.0](spec/plugin.md)
- [HEADLINE/2.0](spec/headline.md)
- [DLL](spec/dll.md)
- [FMO/Mutex](spec/fmo-mutex/index.md)
- [Web 相關](spec/web/index.md)
- [規格備忘（外部網站）](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

### HowTo

- [建立散布用檔案](dev/nar.md)
- [支援 network update](dev/update.md)
- [建立 shell](dev/shell.md)
- [設定 dressup](dev/bind.md)
- [設定 owner draw 選單](dev/ownerdraw.md)
- [排除錯誤訊息](dev/shell-error.md)

### 其他

- [補充：什麼是 SHIORI Event](memo/shiori-event.md)
- [備忘](memo/memo.md)
