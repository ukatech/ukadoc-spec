# 全体の構成

## ゴーストとシェル

ゴーストの構成ファイルは、ベースウェア(SSP,materiaなど)のゴースト格納フォルダに配置される。

全てのゴーストは必ずひとつのmasterゴーストとmasterシェルを持つ必要がある。

シェルの立場から見ると、全てのシェルは必ずいずれか一つのゴーストに所属している。

従って両者のファイル構成は、下記のようにシェルがゴーストに含まれる形になる。

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　+-makoto.dll
　　　　　　+-updates2.dau
　　　　　　+-*.ico
　　　　　　+-*.cur
　　+-shell
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-(element).png
　　　　　　+-(element).pna
　　　　　　+-surfaces.txt
　　　　　　+-makoto.dll (必要な時のみ)
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
　　　　　　+-readme.txt (必要な時のみ)
　　　　　　+-thumbnail.png
　　　　　　+-surfaces**.txt (SSPのみ）
　　　　　　+-surfacetable.txt (必要な時のみ)(SSPのみ)
　　　　　　+-alias.txt (必要な時のみ)(旧仕様）
　　　　+-(additional_shell)
　　+-delete.txt (必要な時のみ)
　　+-delete1.txt (delete[数字].txtも追加で認識できる)
　　+-developer_options.txt (必要な時のみ)(SSPのみ)
　　+-.narignore (必要な時のみ)(SSPのみ)
　　+-.updateignore (必要な時のみ)(SSPのみ)
　　+-.narinclude (必要な時のみ)(SSPのみ)
　　+-.updateinclude (必要な時のみ)(SSPのみ)
　　+-readme.txt または readme.md (必要な時のみ)
　　+-terms.txt または terms.md (必要な時のみ)
　　+-thumbnail.png
```

## バルーン

バルーンはゴーストごとでなく、一つのベースウェアの元に統括的に管理され、全ゴーストで共有される。

各バルーン構成ファイルはベースウェアのバルーン格納フォルダ以下に、下記のような形で配置される。

```filetree
+-(myballoon)
　　+-descript.txt
　　+-balloons*s.txt
　　+-balloonk*s.txt
　　+-readme.txt または readme.md (必要な時のみ)
　　+-terms.txt または terms.md (必要な時のみ)
　　+-balloons*.png
　　+-balloonk*.png
　　+-balloons*.pna （MATERIA不可）
　　+-balloonk*.pna （MATERIA不可）
　　+-balloonc*.png
　　+-online*.png
　　+-sstp.png
　　+-arrow*.png
　　+-thumbnail.png
　　+-ok_down.png/ok_up.png （SSPのみ）
　　+-cancel_down.png/cancel_up.png （SSPのみ）
　　+-mode_down.png/mode_up.png （SSPのみ）
　　+-sstp_new.png （SSPのみ）
　　+-marker.png （SSPのみ）
　　+-delete.txt (SSPのみ・必要な時のみ)
　　+-delete1.txt (delete[数字].txtも追加で認識できる)
```

- **(myghost)\\**: 各ゴーストホームディレクトリ（ルートフォルダ）。

  フォルダ名称は英数推奨。

- **(myghost)\\ghost\\**: ゴーストの内部動作用ファイルのフォルダ。

- **(myghost)\\ghost\\master\\**: ゴーストのデフォルトで使用されるフォルダ。

  現在はmasterしか使用されない（過去の設計の名残）。

ゴーストフォルダ内のファイル構成の詳細は「[ゴースト](ghost.md)」のページへ。

makoto.dllについては「[トランスレータ](translator.md)」のページへ。

- **(myghost)\\shell\\**: ゴーストのシェル（グラフィック表示用ファイル群）のフォルダを格納するフォルダ。

- **(myghost)\\shell\\master\\**: デフォルトシェルのフォルダ。必須。

- **(myghost)\\shell\\(additional_shell)\\**: 追加シェルのフォルダ。任意名（英数字推奨）。ファイル構成はmasterと同じ。

  いくつでも存在できる。存在するとオーナードローメニューなどから切替選択できる。

シェルフォルダ内のファイル構成の詳細は「[シェル](shell.md)」のページへ。

menu_background.png、menu_foreground.png、menu_sidebar.pngについては「[オーナードローメニュー](owner-draw-menu.md)」のページへ。

makoto.dllについては「[トランスレータ](translator.md)」のページへ。

- **(myghost)\\[delete.txt](../descript/install/delete.txt/index.md)**: ファイルの削除設定ファイル。

  詳細は[リンク先](../descript/install/delete.txt/index.md)を参照。

  省略可能。

- **(myghost)\\[developer_options.txt](../descript/install/developer_options.txt/index.md)**: SSP専用。narおよび更新ファイル作成機能の設定ファイル。

  詳細は[リンク先](../descript/install/developer_options.txt/index.md)を参照。

  省略可能。

- **(myghost)\\readme.txt または readme.md**: ゴースト全体のreadme。

  配布者や配布元など明記するのが一般的。

  1行目にcharset,UTF-8と書いておくか、BOMを含んでおけばShift JIS以外も使える。

  インストール時に開かれるほか、オーナードローメニューなどからも開ける。

  省略可能だが存在するのが望ましい。

  readme.txtの代わりにreadme.mdを使用することができ、その場合はMarkdown形式を解釈して文字サイズや表などの装飾つきで表示される。<br />
  画像埋込 `\![画像説明]`(画像パス) も解釈できるが、画像パスが相対パスで、ゴーストの中に実際にファイルが存在し、かつPNGかJPEGの場合のみ利用可能となる。

- **(myghost)\\terms.txt または terms.md**: 利用条件表示。NAR/ZIPファイルのインストール前にこの内容を表示するダイアログが出る。

  インストールを中断してダイアログ表示するので、どうしても必要な場合のみ入れること。

  readmeと同じく、1行目にcharset,UTF-8と書いておくか、BOMを含んでおけばShift JIS以外も使える。

  省略可能、かつ*不要なら省略することが望ましい*。

  readme.mdと同じ条件でterms.mdも利用可能。

- **(myghost)\\thumbnail.png**: メニューツリーでゴーストの選択時に表示されるサムネイル。

  使用可能な画像形式はpngもしくはjpg。

  pngをpnrにリネームすると画像左上の1ドット(座標0,0)と同色が透過される。

  省略可能。

- **(myballoon)\\**: 各バルーンホームディレクトリ（ルートフォルダ）。

  フォルダ名称は英数推奨。

バルーンフォルダ内のファイル構成の詳細は「[バルーン](balloon.md)」のページへ。
