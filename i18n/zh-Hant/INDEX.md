# UKADOC 首頁

## 關於 ukadoc

由伺か（Ukagaka）相關規格文件彙整專案 [UKADOC project](https://github.com/ukatech/ukadoc-spec) 編輯的文件集。

*[SSP](http://ssp.shillest.net/) 相關文件在此處被視為官方文件*。

如要指出錯誤，或提出問題、意見、需求、提供資訊等，請至[ばぐとら研究所ToDo](http://ssp.shillest.net/bts/?project=misc&action=top)。

若想提議新增或修正規格、事件，但不熟悉 GitHub 或 git 的操作，不需要建立 pull request。只要將詳細內容發佈到[ばぐとら研究所ToDo](http://ssp.shillest.net/bts/?project=misc&action=top)或[GitHub 的 Issue](https://github.com/ukatech/ukadoc-spec/issues)，我們就會處理。

管理者：[UKADOC Project](https://github.com/ukatech/ukadoc-spec)

連結用橫幅：

![ukadoc橫幅](assets/image/ukadoc_banner1.png)

本網站的內容可依據[創用 CC 姓名標示 4.0 國際（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/deed.ja)使用。不限於製作 ghost，引用、轉載、改作皆可自由進行。使用時請在「原著作者署名」中註明本專案（UKADOC project）的名稱，或提供本網站的連結。

> 我們提供了 [ukadoc-spec-offline.zip](https://ukatech.shillest.net/ukadoc-spec/ukadoc-spec-offline.zip)，其中收錄本網站的 HTML、CSS、JS 和圖片，方便離線閱讀。解壓縮後即可從 `ukadoc-spec/index.html` 閱讀。
>
> 我們也為 AI agent 準備了尋找文件的指南 [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt)。各頁面的 Markdown 原始檔可透過與儲存庫相同路徑的 `.md` 取得（例如：`https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`）。

## 適用版本

- [SSP](http://ssp.shillest.net/) 最新版（官方規格書）
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2（開發版）
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) 近期版本

## 外部連結

- [伺か開發資訊搜尋](http://ukadev.shillest.net/)
- [SSP 啟動選項（SSP 說明）](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [伺か官方規格書](http://usada.sakura.vg/contents/specification.html)
- [CROW、SSP 規格書](http://crow.aqrs.jp/reference/all/)
- [大八州.NET　非官方規格書](http://www.ooyashima.net/db/)
- [駄でべwiki　規格備忘](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## ukadoc 的閱讀方式

側邊欄中的文章依照類別，分別涵蓋以下內容。

- **檔案結構**：說明構成各種伺か相關內容的檔案，以及目錄結構。

  想掌握需要哪些檔案、可以使用哪些檔案的整體概況時，可參考此處。

- **設定檔**：說明各種伺か相關內容所使用的個別設定檔，以及其記述內容。

  編寫各個設定檔時可參考此處，並盡可能提供範例。

- **Sakura Script**：說明用於指示 ghost 動作的「Sakura Script」各項命令。

  可參考此處了解有哪些命令，以及如何使用。

- **事件**：說明 baseware 通知 SHIORI、PLUGIN 等對象的各個事件 ID。

  製作 ghost、PLUGIN、SHIORI 等內容時，若想了解個別事件或其 Reference，可參考此處。

- **規格**：彙整各種伺か相關內容所涉及的規格。

  這部分主要是與 SHIORI、SAORI、baseware 等系統核心相關的資訊。

- **HowTo**：介紹製作各種伺か相關內容的基本方法。

  不過，要涵蓋依個別情況而異的 TIPS，在現實上有困難；若要尋找更具體的資訊，請參閱外部網站。

- **其他**：其他與 SSP 等 baseware 規格相關的備忘或補充文章。

## 目次

### 檔案結構

- [整體結構](manual/directory.md)
- [ghost](manual/ghost.md)
- [shell](manual/shell.md)
- [owner draw 選單](manual/owner-draw-menu.md)
- [安裝](manual/install.md)
- [network update](manual/update.md)
- [轉譯器](manual/translator.md)
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
- [建立 shell](dev/shell.md)
- [dressup 設定](dev/bind.md)
- [owner draw 選單設定](dev/ownerdraw.md)
- [排除錯誤訊息](dev/shell-error.md)

### 其他

- [補充：SHIORI Event 是什麼](memo/shiori-event.md)
- [備忘](memo/memo.md)
