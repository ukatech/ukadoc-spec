# 轉換器

ghost 將轉換器稱為MAKOTO。

可以放置在ghost端或shell端（CROW僅限ghost端）。

在ghost端使用時，master目錄下必須有`makoto.dll`。

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-makoto.dll
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　:
　　　　　　:
```

在shell端使用時，各shell資料夾下必須有makoto.dll。

```filetree
+-(myghost)
　　+-shell
　　　　+-master(またはadditional_shell)
　　　　　　+-makoto.dll
　　　　　　+-descript.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-surfaces.txt
　　　　　　:
　　　　　　:
```

這是一種機制，會對SHIORI建立的腳本發揮篩選器的作用，並替換字串。

如果ghost端和shell端都有轉換器，會先執行ghost端的轉換，再接著執行shell端的轉換。

轉換會在即將顯示於balloon之前進行。

與SHIORI相同，可作為MAKOTO使用的檔案有許多種，詳細用法請參閱各自的文件。

過去在尚未有SHIORI的時代，轉換器曾用來改變對話內容；現在這類工作主要由SHIORI負責。

目前有時會利用轉換器，實現依shell改變說話方式等效果。

也可以透過SHIORI Event的OnTranslate進行轉換（＝SHIORI兼任ghost端的MAKOTO）。

若同時使用MAKOTO和SHIORI進行轉換，處理順序為SHIORI→MAKOTO。
