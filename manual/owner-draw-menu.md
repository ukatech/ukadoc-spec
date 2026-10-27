# オーナードローメニュー

オーナードローメニュー（右クリックメニュー）に使用する画像ファイル類。

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

実際には必ずしも上記位置にファイルがある必要はなく、フォルダ内などにあってもよい。

SHIORI Resourceによってオーナードローメニューの設定をする場合、ghost/master側にあった方が都合がよい（ghost/master基点の相対パスで指定するので）。

- **menu_background.png**: オーナードローメニューの背景画像。

  メニューの領域は画像ではなくメニューの大きさになる。

  省略可能（標準のメニュー表示になる）。

- **menu_foreground.png**: オーナードローメニューツリーのカーソル選択部分の画像。

  省略可能（標準のメニュー表示になる）。

- **menu_sidebar.png**: オーナードローメニューツリーの左側に追加できる画像。

  横幅のみ画像の幅となる。

  省略可能。

いずれも画像、文字色などの指定はシェルの[descript.txt](../descript/shell/index.md)または[SHIORI Resource](../list/shiori-resource/index.md)によって行う。

SHIORI Resourceで指定する場合は、キャラクターが入れ替わり制であったり、モード切替のような機能を持つゴーストで、その状態に応じてメニュー表示を変更するなどの仕掛けに使える。

shell側descript.txtとSHIORI Resourceの両方で指定した場合、SHIORI Resourceの方が優先される。

また、各画像のファイル名は必ずしも上例の通りにする必要は無い（任意名でよい）。

詳細は[オーナードローメニューの設定](../dev/ownerdraw.md)のページも参照。

メニューの画像が切れた部分はその端の色を単色で塗り潰す。

指定が無かった場合は一般的なポップアップになる。
