# 建立散布用檔案

*若使用 SSP2.3.00 以後的版本，請注意：若未在「設定」→「本體設定」的「一般」中，透過オーナードロー（右鍵選單）開啟「啟用開發者功能」，就無法使用本頁所述的「拖放資料夾以建立 updates2.dau 或 nar 的功能」。*

本文將說明建立散布用檔案（封存檔）的步驟。

本文不只涵蓋 ghost，也一併介紹如何建立追加 shell、balloon 及其他伺か/SSP 相關內容的封存檔。

請一併閱讀「[安裝](../manual/install.md)」頁面，了解檔案結構。

請注意，本文不會說明「如何製作 ghost（或 shell、balloon）」本身。

本文假設您已經完成這些工作。

## 目次

1. [準備檔案](nar.md#ファイルの準備)
2. [建立初始 updates2.dau](nar.md#初期updates2dauの作成)
3. [準備 install.txt](nar.md#installtxtの準備)
4. [封存](nar.md#アーカイブ化)

1. [關於 developer_options.txt](nar.md#developer_optionstxtについて)
2. [關於 ghost 散布自動化系統 (GDM)](nar.md#ゴースト配布系自動化システムgdmについて)
3. [關於 refreshinstall](nar.md#refreshinstallについて)
4. [關於隨附散布 balloon 等內容](nar.md#バルーンなどの同梱配布について)
5. [關於 ghost 的追加檔案](nar.md#ゴーストへの追加ファイルについて)
6. [關於多重安裝套件](nar.md#複数インストール用パッケージについて)
7. [使用 initial_install.nar 進行靜默安裝](nar.md#initial_installnarによるサイレントインストールについて)

## 準備檔案

首先，準備要包含在封存檔中的內容（若是 ghost，則準備構成該 ghost 的所有檔案）。

若您直接編輯安裝在 baseware[※](nar.md#initial_installnarによるサイレントインストールについて)中的內容來進行開發，建議先將整份內容複製到其他位置，並以複製品作為散布用檔案，再進行以下作業。

如需了解所需檔案，請參考左側選單「檔案結構」分類中的「[整體結構](../manual/directory.md)」及「[ghost](../manual/ghost.md)」、「[shell](../manual/shell.md)」等各頁面。

`install.txt`、`updates2.dau`、`developer_options.txt` 等檔案會在本文後續準備，目前沒有也沒關係。

接著，移除使用者不需要的檔案，例如以下項目。

- 各類 SHIORI 的存檔資料檔（若初始值設定等需要則除外）
- 所有 profile 資料夾（ghost、shell 內都可能有。SSP 會自動移除）
- 開發工具（例如隨 Satori 附帶的さとりて、れしば等）
- （僅 MATERIA）根目錄下的 profile.txt
- desktop.ini 等 Windows 產生的設定檔（SSP 會自動移除部分檔案）
- 其他開發用字典檔、設定檔、記錄檔等

若使用 SSP，可以考慮設定 `developer_options.txt`。

詳情請參閱後文的「[關於 developer_options.txt](nar.md#developer_optionstxtについて)」。

## 建立初始 updates2.dau

接著，建立網路更新用檔案（`updates2.dau`）的初始檔案。

這是透過比對網路更新時伺服器端與用戶端的檔案內容，偵測損毀、竄改等異常的機制。

因此，若不打算支援網路更新功能，或內容本身不支援網路更新（例如[ghost 的追加檔案](nar.md#ゴーストへの追加ファイルについて)），即可略過並繼續下一步。

事實上，封存檔並非一定要包含網路更新用檔案。

不過，事先建立該檔案可以減少使用者首次進行網路更新時，必須由 baseware 在使用者端處理的工作。

封存檔包含許多檔案時，事先建立會更貼心。

首先，若要在 MATERIA 或 CROW 中建立 `updates2.dau`，必須先在最上層目錄（例如 ghost 的 ghost 資料夾、shell 資料夾、readme.txt 所在的位置）建立一個名稱為 `updates2.dau` 的空白文字檔。

SSP 會自動建立該檔案。

接著啟動 baseware，將含有 `updates2.dau` 或要更新檔案的資料夾拖放到本體上。

此時，在 MATERIA 或 CROW 中，若資料夾內含有 `install.txt`，會優先建立封存檔，因而不會建立 `updates2.dau`，請注意不要包含該檔案。

相反地，在 SSP 中，先建立 `install.txt` 再拖放資料夾，就能一次完成建立 `updates2.dau` 和封存檔。

拖放後，資料夾中應會建立（或已存在）名為 `updates2.dau` 的檔案，且其中應已寫入一些內容。

可從右鍵選單等處使用記事本等一般文字編輯器開啟 `updates2.dau`，請確認其內容（不必理解內容本身）。

## 準備 install.txt

接著，準備用來記述及設定安裝內容的檔案 `install.txt`。

在最上層目錄（例如 ghost 的話，就是有 ghost 資料夾、shell 資料夾、readme.txt 等檔案的地方），準備一個名為 `install.txt` 的文字檔，並依照內容撰寫檔案。

要寫入的內容會依照想要發佈的是 ghost 還是 shell 等而有所不同，請參閱 [Install/Update 設定](../descript/install/index.md)頁面。該頁面也有範例。

## 封存

終於進入封存階段，不過到了這一步，已經沒有多少事情要做了。

這是因為 baseware 具備將含有 `install.txt` 的資料夾拖放到 baseware 上時，將其製作成封存檔的功能。

因此，要做的事情就是將目前準備好的資料夾整個拖放到 baseware（正在其中執行的 ghost）上。

這樣應該就會產生名為「\[資料夾名稱\].nar[※](nar.md#initial_installnarによるサイレントインストールについて)」的檔案。這就是供發佈使用的封存檔。

接著只要將這個 nar 檔案上傳至伺服器或上傳網站，就可以正式開始發佈了。

## 關於 developer_options.txt

使用 SSP 建立封存檔或 `updates2.dau` 時，在最上層目錄（建立封存檔時放置 install.txt 的位置）準備名為 `developer_options.txt` 的檔案，即可設定處理對象檔案。

撰寫方式的說明與範例，請參閱 [Install/Update 設定頁面中關於 developer_options.txt 的章節](../descript/install/developer_options.txt/index.md)。

請注意，此檔案只會在使用 SSP 建立封存檔或 `updates2.dau` 時生效，因此使用後述的[ghost 發佈自動化系統](nar.md#ゴースト配布系自動化システムgdmについて)，或使用其他 baseware 建立這些檔案時，設定都不會生效。

## 關於 ghost 發佈自動化系統 (GDM)

ghost 發佈自動化系統 (GDM) 是一種支援工具，可以一次完成 `updates2.dau` 的建立、ghost 封存，以及上傳至伺服器。

安裝並完成設定後，本頁所述的大部分內容就不再需要了。

目前由「整備班」發佈，詳情如下。

[ghost 發佈自動化系統](http://ms.shillest.net/#TOOL)

詳細的安裝與設定說明，請參考以下網站（不需要「1」的內容）。

[ghost 發佈自動化系統 (GDM) 使用方法](http://navy.nm.land.to/post/jidouhaihu.html)（[封存](https://web.archive.org/web/20260205013109/http://navy.nm.land.to/post/jidouhaihu.html)）

雖然名稱中有「ghost」，但實際上也能用來建立 shell、balloon 等各種項目的封存檔，以及上傳網路更新用檔案。

此外，可以為多個對象（例如 ghost1、ghost2、shell1、shell2、shell3、balloon 等）儲存建立封存檔、網路更新等各項操作的設定，並依照需求選擇要執行的操作，一次完成。

如果需要管理許多內容，這項工具會非常方便。

初次安裝及設定需要處理的事情稍多，會比較麻煩，但只要設定完成，之後就能按一下按鈕，完成多個內容的網路更新與封存檔更新，非常方便。

除此之外，也能完全避免因為建立 `updates2.dau` 後修改檔案，或將 FTP 通訊設為 ASCII 模式後再上傳等失誤，造成 md5 不符錯誤。

當然，透過適當設定，也能有效防止混入不需要的檔案。

如前所述，[developer_options.txt](nar.md#developer_optionstxtについて) 是使用 SSP 功能建立 nar 或 `updates2.dau` 時生效的設定檔，因此請注意，使用 GDM 建立時不會用到它。

不過，GDM 本身就能設定要上傳或不上传的檔案，因此通常不需要這個設定檔。

## 關於 refreshinstall

如果 install.txt 中包含以下記述，安裝方式就會有所不同。

```
refresh,1
```

如果指定此設定，而要安裝的資料夾中已經有檔案，安裝時就不會覆寫檔案，而是先全部刪除再進行安裝。

當資料夾或檔案結構有所變更，覆寫後會留下不需要的檔案時，可以使用此設定。

不過請注意，重新整理安裝會*連儲存資料等也一併刪除*。

如果想在重新整理安裝時保留某些檔案，可以如下指定。

```
refreshundeletemask,save1.txt:save2.txt
```

詳細格式等資訊，也請參閱 [Install/Update 設定](../descript/install/index.md)頁面。

## 隨附發佈 balloon 等內容

透過在 install.txt 中記述設定並配置檔案，可以將 balloon 隨 ghost 一起發佈。

此外，在 SSP 中，除了 balloon 之外，也可以隨附 plugin 和 headline；而且也可以將這些內容隨 shell 一起發佈，而非隨 ghost 發佈。

以下以將 balloon 隨 ghost 一起發佈為例。

檔案結構如下。

```filetree
+-(myghost)
　　+-install.txt
　　+-developer_options.txt (SSPのみ)
　　+-ghost
　　+-shell
　　+-(myballoon)
　　　　+-descript.txt
　　　　+-balloons0.png
　　　　:
　　　　:
```

此時只要將 install.txt 寫成以下內容，就能與 ghost 一起安裝 balloon。

```
charset,Shift_JIS
type,ghost
name,ゴースト名
directory,myghost（※ゴーストのフォルダ名。英数）
balloon.directory,myballoon（※バルーンのフォルダ名。英数）
```

balloon 端不需要 install.txt<br />
※即使有也會被忽略。為了日後單獨發佈而放入也沒有問題。

另外，如果安裝後的 balloon 資料夾名稱與發佈時的資料夾名稱不同，請如下設定。

```
charset,Shift_JIS
type,ghost
name,ゴースト名
directory,myghost（※ゴーストのフォルダ名。英数）
balloon.directory,hoge_balloon（※インストール後のバルーンフォルダ名。英数）
balloon.source.directory,myballoon（※アーカイブ内のバルーンフォルダ名。英数）
```

如此一來，上例中名為 myballoon 的 balloon 資料夾，<br />
在實際安裝後就會使用 hoge_balloon 作為資料夾名稱。

隨附檔案的 refresh 設定如下。

```
balloon.refresh,1
balloon.refreshundeletemask,hoge.png:huga.txt:...
```

若要隨附 balloon 以外的內容（僅 SSP 支援），請將「balloon.directory」、「balloon.source.directiory」、「balloon.refresh」等設定中的「balloon」部分，改成想要隨附的內容，也就是以下其中之一：

- headline
- plugin
- calendar.skin
- calendar.plugin

接著，請比照上例的 balloon 隨附檔案。

## 關於新增至 ghost 的檔案

若要建立 ghost 的附加檔案（supplement）封存檔，請保留 ghost 原有的資料夾結構，只將要新增的檔案放入封存檔。

例如，若要在 ghost/master 新增「dic_supplement.txt」檔案，結構如下。

```filetree
+-(mysupplement)
　　+-install.txt
　　+-developer_options.txt (SSPのみ)
　　+-ghost
　　　　+-master
　　　　　　+-dic_supplement.txt
```

此時，install.txt 的內容如下。

```
charset,Shift_JIS
name,追加トークパッチ
type,supplement
accept,対象ゴーストの本体側名
```

## 多重安裝套件

此方法僅適用於 SSP。

使用以下檔案結構建立封存檔，即可建立可同時安裝多項內容的套件。

```filetree
+-(mypackage)
　　+-install.txt (package用)
　　+-(myghost1)
　　　　+-install.txt (myghost1用)
　　　　+-developer_options.txt (SSPのみ)
　　　　+-ghost
　　　　+-shell
　　　　:
　　+-(myghost2)
　　　　+-install.txt (myghost2用)
　　　　+-developer_options.txt (SSPのみ)
　　　　+-ghost
　　　　+-shell
　　　　:
```

在資料夾中準備供 package 使用的 `install.txt`，並將各項內容放入該資料夾。

各項內容都有*各自的 install.txt*，是可單獨封存的一般安裝結構。

可以想成是將多項內容放進資料夾中「打包」，再另外附上作為外箱標籤的 package 用 `install.txt`。

最上層資料夾中的 package 用 install.txt 請依照以下方式撰寫。

```
charset,Shift_JIS
type,package
name,パッケージ名
```

各個 install.txt 依照一般方式撰寫（請參閱 [Install/Update 設定](../descript/install/index.md)等）。

此外，使用 [developer_options.txt](nar.md#developer_optionstxtについて) 時，請注意要將它放在*各項內容中*，而非最上層資料夾。

上例的檔案結構是包含兩個 ghost 的範例，但實際上當然不限於 ghost，任何可作為封存檔的內容都可以包含在內。

不過，請注意不要將指定 accept 的內容（例如 type,shell 或 type,supplement）混在一起，尤其是指定目標各不相同時。

## 使用 initial_install.nar 靜默安裝

若將名為 `initial_install.nar` 的 nar 檔案放在與 ssp.exe 相同的資料夾中並啟動 SSP，該 nar 檔案會在啟動時自動以靜默方式（不顯示確認對話方塊）覆蓋安裝。

安裝完成後，`initial_install.nar` 會自動刪除。

此功能主要供開發者使用；若要在 SSP 發佈套件中附帶 ghost 等內容一併發佈，便很方便。

例如，若要製作與 SSP 本體一同附帶特定 ghost 的發佈套件，只要將 `initial_install.nar` 放在與 ssp.exe 相同的位置，使用者首次啟動時就會自動安裝該 ghost。

**対応:** SSP 2.7.52

!!! tip "提示"

    - **[※1 baseware](nar.md#ファイルの準備)**: 指 SSP、MATERIA（本家伺か）、CROW 等用來執行 ghost 的基礎軟體。
    - **[※2 nar](nar.md#アーカイブ化)**: Nanika ARchive 的縮寫。「Nanika」指的是伺か的舊稱之一「何か」。讀音為「naː」。
