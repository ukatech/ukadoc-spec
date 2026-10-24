# ゴースト

masterゴーストフォルダのファイルは以下の通り。

```
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　+-(saori).dll
　　　　　　+-makoto.dll
　　　　　　+-updates2.dau （旧仕様）
　　　　　　+-updates.txt （旧仕様）
　　　　　　+-*.ico
　　　　　　+-*.cur
　　　　　　+-thumbnail.png
　　　　　　+-ai0.png
　　　　　　+-ai0_dark.png
```

- **[descript.txt](../descript/ghost/index.md)**: ゴーストを識別するためのファイル。

  これがないと本体に認識されない。

  テキスト内の記載事項など詳細は[リンク先](../descript/ghost/index.md)を参照。

- **[updates2.dau](update.md)**

- **[updates.txt](update.md)**: 更新情報が記載されたファイル。

  この位置にあるのは旧仕様で、基本的にルート（(myghost)直下）にのみあればよい。

  詳しくは[リンク先](update.md)参照

- **shiori.dll**: ゴーストのコア。ほぼ必須。

  汎用SHIORIが多く出ているので通常はそれを使用する。

  ベースウェア（SSPなど）から送信されてくる[SHIORI Event](../list/shiori-event/index.md)（[補足説明](../memo/shiori-event.md)）を受けて、ゴーストの動作指示である[さくらスクリプト](../list/sakura-script/index.md)を構築してベースウェアに返却する役割を果たす。

  実際のトークの書き方など、ゴーストの中核部分の作り方は、SHIORIによって全く異なるので、各SHIORI側のドキュメントを参照。

- **(saori).dll**: SHIORIの機能拡張モジュール。

  基本的にはshiori.dllと同じ階層に置く。

  ただしSHIORIから呼び出す際に相対パスを指定することもできる。

  使用手順はSHIORI次第なので、SHIORI側のドキュメントを参照。

  このファイルは省略可能。

- **[makoto.dll](translator.md)**: トランスレート用のDLL。

  詳しくは[リンク先](translator.md)参照。[シェル側](shell.md)にも設置可能。

  このファイルは省略可能。

- **\*.ico**: アイコンファイル。

  32×32と16×16を使用することができる。

  アイコン化した時やゴーストエクスプローラなどで表示される。

  このファイルは省略可能。省略時はデフォルトアイコンが使用される。

- **\*.cur**: カーソルファイル。

  ゴーストに乗ったカーソルが指定されたカーソルになる。

  このファイルは省略可能。省略時は普段のカーソルのまま。

- **thumbnail.png**: メニューツリーでゴーストの選択時に表示されるサムネイル。

  使用可能な画像形式はpngもしくはjpg。

  pngをpnrにリネームすると画像左上の1ドット(座標0,0)と同色が透過される。

  このファイルは省略可能。

- **ai0.png / ai0_dark.png**: [AIグラフの説明](../descript/ghost/descript-txt/shiori.logo.file.md)参照。

  このファイルは省略可能。

この他、「辞書」と呼ばれる文字列のリソースファイルなど、SHIORI（など）がdll外部にいくつかのファイルを備えることが一般的である（むしろゴースト製作者はそういったファイルを中心的に編集する場合も多い）。<br />
そうしたものの詳細については、利用する各SHIORIのドキュメントを参照すること。
