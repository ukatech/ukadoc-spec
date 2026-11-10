# UKADOC 首頁

## 關於 ukadoc

這是由[UKADOC project](https://github.com/ukatech/ukadoc-spec)編輯的文件集，該專案旨在彙整伺か相關規格文件。

*[SSP](http://ssp.shillest.net/)的相關文件在此被視為官方文件*。

如要回報錯誤、提出問題、意見或需求，或提供資訊，請至[ばぐとら研究所ToDo](http://ssp.shillest.net/bts/?project=misc&action=top)。

本網站的文字可依據[創用 CC 姓名標示 4.0 國際（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/deed.ja)使用。不限於 ghost 製作，歡迎自由引用、轉載及修改。使用時請標示「原著作者的姓名」，註明本專案（UKADOC project）的名稱，或提供本網站的連結。

> 本網站提供 [ukadoc-spec-offline.zip](https://ukatech.shillest.net/ukadoc-spec/ukadoc-spec-offline.zip)，其中打包了網站的 HTML、CSS、JS 及圖片，供離線閱讀。解壓縮後即可從 `ukadoc-spec/index.html` 開始閱讀。
>
> 我們也為 AI 代理程式準備了搜尋指南 [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt)。各頁面的 Markdown 原稿可從與儲存庫相同路徑的 `.md` 檔案取得（例如：`https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`）。

## 適用版本

- [SSP](http://ssp.shillest.net/) 最新版（官方規格書）
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2（開發版）
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) 最新版

## 外部連結

- [伺か開發資訊搜尋](http://ukadev.shillest.net/)
- [SSP 啟動選項（SSP 說明）](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [伺か官方規格書](http://usada.sakura.vg/contents/specification.html)
- [CROW・SSP 規格書](http://crow.aqrs.jp/reference/all/)
- [大八州.NET 非官方規格書](http://www.ooyashima.net/db/)
- [駄でべwiki 規格備忘](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## 如何閱讀 ukadoc

側邊欄中的文章依照類別，分別介紹以下內容。

- **檔案結構**：介紹構成各種伺か相關內容的檔案，以及目錄結構。

  可參閱此處以掌握所需及可用檔案的整體概況。

- **設定檔**：說明各種伺か相關內容所使用的個別設定檔如何撰寫。

  撰寫各設定檔時可參閱此處。我們也盡可能提供範例。

- **Sakura Script**：說明用於指示 ghost 動作的「Sakura Script」各項指令。

  可參閱此處了解可使用哪些指令，以及如何使用。

- **事件**：說明 baseware 通知 SHIORI、PLUGIN 等元件的各個事件 ID。

  製作 ghost、PLUGIN、SHIORI 等內容時，可參閱此處了解個別事件及其 Reference。

- **規格**：彙整各種伺か相關內容所涉及的規格。

  主要介紹與 SHIORI、SAORI、baseware 等系統核心部分相關的資訊。

- **HowTo**：介紹製作各種伺か相關內容的基本方法。

  不過，實際上很難涵蓋因應個別情況的 TIPS；如需更具體的資訊，請另行搜尋外部網站。

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
- Install/Update
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
- [製作 shell](dev/shell.md)
- [設定 dressup](dev/bind.md)
- [設定 owner draw 選單](dev/ownerdraw.md)
- [排除錯誤訊息](dev/shell-error.md)

### 其他

- [補充：什麼是 SHIORI Event](memo/shiori-event.md)
- [備忘](memo/memo.md)
