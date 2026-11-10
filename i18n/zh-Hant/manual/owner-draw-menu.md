# Owner draw 選單

用於 owner draw 選單（右鍵選單）的圖檔。

```filetree
+-(myghost)
　　+-shell
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-readme.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-(element).png
　　　　　　+-(element).pna
　　　　　　+-surfaces.txt
　　　　　　+-surfaces**.txt
　　　　　　+-alias.txt
　　　　　　+-thumbnail.png
　　　　　　+-makoto.dll
　　　　　　+-surfacetable.txt
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
```

實際上，檔案不一定要位於上述位置，也可以放在資料夾內等位置。

若透過SHIORI Resource設定 owner draw 選單，放在ghost/master端會比較方便（因為指定路徑時，是以ghost/master為基準的相對路徑）。

- **menu_background.png**: owner draw 選單的背景圖。

  選單區域的大小會由選單本身決定，而非由圖片決定。

  可省略（會顯示標準選單）。

- **menu_foreground.png**: owner draw 選單樹狀結構中游標選取部分的圖片。

  可省略（會顯示標準選單）。

- **menu_sidebar.png**: 可新增至 owner draw 選單樹狀結構左側的圖片。

  只有寬度會與圖片的寬度相同。

  可省略。

以上圖片、文字顏色等設定，都透過shell的[descript.txt](../descript/shell/index.md)或[SHIORI Resource](../list/shiori-resource/index.md)進行。

若透過SHIORI Resource指定，對於角色會輪替，或具有模式切換等功能的ghost，可以用來根據狀態變更選單顯示等。

若同時在shell端的descript.txt和SHIORI Resource中指定，SHIORI Resource的設定會優先採用。

此外，各圖片的檔名不一定要與上例相同（可任意命名）。

詳細資訊也請參閱[owner draw 選單設定](../dev/ownerdraw.md)頁面。

選單圖片未覆蓋到的部分，會以該邊緣的顏色填滿。

若未指定，則會顯示一般的彈出式選單。
