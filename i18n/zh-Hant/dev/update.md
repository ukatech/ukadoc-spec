# 支援網路更新

*在SSP2.3.00以後的版本中，若未在「右鍵選單」的「設定」→「本體設定」之「一般」中開啟「啟用開發者功能」，就無法使用本頁所述的「拖放資料夾以建立updates2.dau功能」，請特別留意。*

本節說明支援網路更新所需的設定與準備事項。

另外，SSP除了ghost之外，也支援shell、balloon、plugin、headline sensor的網路更新；本節也會一併說明這些內容。

## 目次

1. [準備伺服器](update.md#サーバを用意する)
2. [設定更新用URL](update.md#更新用urlを設定する)
3. [移除不需要的檔案](update.md#不要なファイルを取り除く)
4. [建立updates2.dau](update.md#updates2dauを作る)
5. [上傳至伺服器](update.md#サーバにアップロードする)

1. [關於developer_options.txt](update.md#developer_optionstxtについて)
2. [關於ghost散布自動化系統(GDM)](update.md#ゴースト配布系自動化システムgdmについて)
3. [關於「.dau」遭伺服器拒絕的情況](update.md#dauがサーバに弾かれてしまう場合について)

第二次以後的更新，主要會重複執行3、4、5。

## 準備伺服器

首先準備網路更新所需的伺服器。

使用免費租用伺服器等服務即可，這類服務常用於架設個人網站。

使用租用伺服器時（尤其是免費服務），可能會因為限制或設定而不利於網路更新。

請特別留意以下事項。

- 必須能上傳所需副檔名的檔案。
- 不會自動在文字檔中插入廣告。

若要尋找免費租用伺服器，以下頁面應該能作為參考。

[駄でべwiki：要散布ghost的話，哪裡比較好？（免費空間版）](http://emily.shillest.net/specwiki/index.php?%E7%A5%9E%E5%A4%9C%E3%81%BF%E3%82%85%E3%82%93%2F%E3%82%B4%E3%83%BC%E3%82%B9%E3%83%88%E9%85%8D%E5%B8%83%E3%81%99%E3%82%8B%E3%81%AA%E3%82%89)（外部網站）

## 設定更新用URL

基本上會在`descript.txt`中記述。

在`descript.txt`中加入以下一行來設定。

```
homeurl,http://xxx.yyy/myghost/
```

此處填寫的url，是網路上指向包含網路更新內容的資料夾（之後會在此處建立`updates2.dau`）的url。

因此，url的形式取決於伺服器。假設該伺服器的根目錄是http://xxx.yyy/，而要支援網路更新的ghost資料夾（myghost）以如下方式

```filetree
+-root
　　+-ukagaka
　　　　+-myghost1
　　　　　　+-ghost
　　　　　　+-shell
　　　　　　+-readme.txt
　　　　　　+-updates2.dau
+-index.html
+-hogehoge.html
+-style.css
:
:
```

放在伺服器上時，descript.txt中應該寫入：

```
homeurl,http://xxx.yyy/ukagaka/myghost1/
```

這就是要寫入的內容。

另外，若內容是ghost，除了寫在`descript.txt`中，也可以在[SHIORI Resource](../list/shiori-resource/index.md)的「[homeurl](../list/shiori-resource/ghost/homeurl.md)」中指定url。

如何在ghost端使用SHIORI Resource指定homeurl，取決於SHIORI，因此此處不予說明。請參閱各SHIORI的文件。

## 移除不需要的檔案

接著，移除使用者不需要的檔案。例如：

- 各種SHIORI的存檔資料檔（但若初始值設定等需要這些檔案則例外）
- 所有profile資料夾（ghost、shell中都可能建立。SSP會自動移除）
- 開發工具（例如隨里々附帶的さとりて、れしば等）
- （僅限MATERIA）目錄底下的profile.txt
- desktop.ini等Windows產生的設定檔（SSP會自動移除部分檔案）
- 其他開發用字典檔、設定檔、記錄檔等

使用SSP時，如果覺得每次手動移除很麻煩，可以使用`developer_options.txt`。

詳細內容請參閱[後述說明](update.md#developer_optionstxtについて)。

如果不小心在*混入了這些不需要的檔案*的狀態下進行更新，或是在多次更新後，*以前使用的檔案變得不再需要*（已更名），該怎麼辦呢？

遇到這種情況，*只從伺服器刪除不需要的檔案，並無法刪除使用者端的檔案*。

這是因為網路更新的做法，是使用伺服器上的檔案覆寫使用者端的檔案，而不是進行同步（鏡像）。

若要透過網路更新移除已經散布出去的不需要檔案，請使用`delete.txt`。

`delete.txt`要放在網路更新內容的最上層資料夾（例如ghost的情況下，放在包含ghost資料夾、shell資料夾、`readme.txt`等的目錄；其他情況則放在有descript.txt的目錄）。

配置範例請參閱頁面左側選單「檔案結構」中的「[網路更新](../manual/update.md)」。

## 建立 updates2.dau

接著建立網路更新用檔案（`updates2.dau`）。

這是透過檢查伺服器端與用戶端的檔案內容是否一致，來偵測損毀、竄改等異常的機制。

若要使用MATERIA或CROW建立`updates2.dau`，必須事先在最上層目錄（例如 ghost 的話，就是有ghost資料夾、shell資料夾、readme.txt等項目的位置）建立一個名為`updates2.dau`的空白文字檔。

SSP會自動建立。

接著啟動baseware[※](update.md#dauがサーバに弾かれてしまう場合について)，並將含有`updates2.dau`或要更新檔案的資料夾拖放到主程式上。

此時在MATERIA或CROW中，如果資料夾內含有`install.txt`，會優先建立nar檔案，因此不會建立`updates2.dau`，請注意不要包含該檔案。

拖放後，資料夾中應該會建立（存在）一個名為`updates2.dau`的檔案，且其中應該寫入了某些內容。

`updates2.dau`可以透過按右鍵等方式，用記事本等一般文字編輯器開啟，請確認檔案內容（不必理解內容本身）。

## 上傳到伺服器

到這裡，接下來只要使用FTP通訊軟體等將檔案上傳到伺服器即可。

但請注意，通訊模式必須設定為*以二進位模式上傳所有檔案*。

若以ASCII模式上傳，網路更新將會失敗。

此時，若能在自己的baseware中保留「網路更新前」的檔案，並在上傳後確認網路更新正常完成，就會比較安全。

## 關於 developer_options.txt

使用SSP建立封存檔或`updates2.dau`時，在最上層目錄（建立封存檔時放置install.txt的位置）準備名為`developer_options.txt`的檔案，即可設定要納入處理的檔案。

有關寫法的說明與範例，請參閱[Install/Update設定頁面中關於developer_options.txt的章節](../descript/install/developer_options.txt/index.md)。

請注意，此檔案僅在使用SSP建立封存檔或`updates2.dau`時生效，因此若使用後述的[ghost發佈自動化系統](update.md#ゴースト配布系自動化システムgdmについて)，或其他baseware建立這些檔案，設定將不會生效。

## 關於ghost發佈自動化系統(GDM)

ghost發佈自動化系統(GDM)是一種支援工具，可一次完成`updates2.dau`、ghost封存，以及上傳到伺服器等作業。

安裝並正確設定後，本頁所述的大部分內容都不再需要手動處理。

目前如以下所示，由「整備班」發佈。

[ghost發佈自動化系統](http://ms.shillest.net/#TOOL)

詳細的安裝與設定說明，請參考以下網站（不需要「1」的內容）。

[ghost發佈自動化系統(GDM)使用方法](http://navy.nm.land.to/post/jidouhaihu.html)（[封存](https://web.archive.org/web/20260205013109/http://navy.nm.land.to/post/jidouhaihu.html)）

雖然名稱中有「ghost」，但實際上也能用於shell、balloon及其他各種項目的封存，以及上傳網路更新用檔案。

此外，可以針對多個項目（例如ghost1、ghost2、shell1、shell2、shell3、balloon……），分別儲存建立封存檔、網路更新等操作的設定，並選擇當下要執行的操作後一次完成。

管理大量內容時，這會非常有幫助。

初次安裝與設定需要處理不少事情，稍微麻煩一些，但完成一次後，之後只要按一下滑鼠，就能完成多個內容的網路更新與封存更新，非常方便。

除此之外，也能完全避免因建立`updates2.dau`後修改檔案，或設定FTP通訊以ASCII模式上傳等失誤所造成的md5不一致錯誤。

當然，透過適當設定，也能大幅協助防止混入不需要的檔案。

請注意，前述的[developer_options.txt](update.md#developer_optionstxtについて)是使用SSP功能建立nar或`updates2.dau`時生效的設定檔，因此使用GDM建立時無關。

不過，GDM本身就能設定要不要上傳特定檔案，因此原本就不需要使用這個檔案。

## 關於「.dau」遭伺服器拒絕的情況

依租用伺服器的設定，有時可能無法處理「.dau」這種不常見副檔名的檔案。

遇到這種情況時，可以改用`updates.txt`。

使用方法是將本頁中所有的「`updates2.dau`」都替換成「`updates.txt`」。

!!! tip "提示"

    - **[※1 baseware](update.md#updates2dauを作る)**: 指SSP、MATERIA（原版伺か）、CROW等用來執行ghost的基礎軟體。
