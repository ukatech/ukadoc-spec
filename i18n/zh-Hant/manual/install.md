# 安裝

關於如何建立發行用封存檔，請參閱「[建立發行用檔案](../dev/nar.md)」頁面。

一般會以副檔名為`nar`的封存檔發行 ghost（naru。Nanika ARchive）。

nar只是將zip的副檔名改掉，實際上是zip，因此有時也會因伺服器而以zip發行。

只要有解壓縮DLL，雖然也能使用lzh安裝，但除非有非常充分的理由，否則請勿使用。

SSP也可以安裝cab或自我解壓縮exe。

雖然也可以解壓縮封存檔後手動安裝，但只要妥善準備`install.txt`，就能透過拖放等方式啟動安裝程式功能，自動安裝。

將包含install.txt的ghost資料夾拖放到baseware（SSP）本體，即可建立nar。

這與手動壓縮成zip後重新命名的結果相同，但請注意不要讓資料夾層級過深。

發行ghost時，請注意不要包含ghost與shell資料夾中的profile資料夾或儲存資料等。

網路更新也是同樣的道理。

SSP提供了`developer_options.txt`來控制這項行為。

- **標準的 ghost**:

  ```filetree
  +-(myghost)
  　　+-ghost
  　　+-shell
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-readme.txt
  　　+-thumbnail.png
  　　:
  　　:
  ```

  !!! tip "提示"

      若為*supplement*，請保持上述的*資料夾結構不變*，只將要新增的檔案打包成封存檔。

      例如，若要將名為dic_supplement.txt的檔案新增至ghost/master/，

      ```filetree
      +-(mysupplement)
      　　+-install.txt
      　　+-developer_options.txt (SSPのみ)
      　　+-ghost
      　　　　+-master
      　　　　　　+-dic_supplement.txt
      ```

      即如下所示。

- **標準的追加 shell**:

  ```filetree
  +-(additional_shell)
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-descript.txt
  　　+-readme.txt
  　　+-thumbnail.png
  　　+-surface*.png
  　　+-surfaces.txt
  　　:
  　　:
  ```

- **標準的 balloon**:

  ```filetree
  +-(myballoon)
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-descript.txt
  　　+-balloonc*.png
  　　+-balloons*.png
  　　+-balloonk*.png
  　　:
  　　:
  ```

- **在 ghost 中附帶 balloon 等內容時**:

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

  plugin等也相同（若要附帶shell，無須如此處理，直接放在一般的shell資料夾底下即可）。

  此外，被附帶的內容（上例中的balloon）不需要install.txt。即使存在也會被忽略。

- **(僅限SSP) 多項目安裝用套件**:

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

  請注意，套件與各個內容都需要各自的install.txt。

  不限於ghost，凡是可以單獨製作成封存檔的項目都可以附帶，但若是shell或supplement等有特定對象的項目，請注意不要混入不同對象的內容。

其他項目，如headline sensor、單獨發行plugin等也相同，請將install.txt放在最上層目錄。

- **[install.txt](../descript/install/index.md)**: 記載安裝設定的文字檔。

  若沒有此檔案，便不會啟動透過拖放等方式自動安裝的功能。

  可設定封存檔內容的類型、封存檔名稱、目錄名稱等。

  詳情請參閱[連結頁面](../descript/install/index.md)。

- **[developer_options.txt](../descript/install/developer_options.txt/index.md)**: 僅限SSP。可省略。

  請放在與install.txt相同的位置。

  但若為多項目安裝用套件，請注意應放在各內容的install.txt所在位置，而非最上層的install.txt所在位置。

  在SSP中建立nar時，用於設定不納入封存檔的檔案等項目。

  格式等詳細資訊請參閱[連結頁面](../descript/install/developer_options.txt/index.md)。
