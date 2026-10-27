# インストール

配布用アーカイブの作成方法自体は「[配布用ファイルの作成](../dev/nar.md)」のページを参照。

ゴーストは一般的に`nar`という拡張子のアーカイブで配布される（なー。Nanika ARchive）。

narはzipの拡張子を変えただけのもので、実体はzipなので、サーバによってはzipで配布する場合もある。

lzhでも解凍DLLがあればインストール可能ではあるがよほどの理由が無い場合は使用しない。

SSPではcabや自己解凍exeでも一応インストール可能。

アーカイブは解凍して手動でインストールすることもできるが、`install.txt`が適切に用意されていれば、D&Dなどの手段でインストーラ機能が働き、自動的にインストールできる。

narはinstall.txtを含んだゴーストフォルダをベースウェア（SSP）本体にD&Dすることによって作成可能。

手動でzip圧縮しリネームしたものと同等だが、その場合フォルダの階層を深くしてしまわないように注意。

ゴーストを配布する際にゴーストとシェルのフォルダにあるprofileフォルダや、セーブデータ等を含めないように注意すること。

ネットワーク更新でも同じことがいえる。

SSPでは、その制御のために`developer_options.txt`が用意されている。

- **標準的なゴーストの場合**:

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

  !!! tip "ヒント"

      *supplement*の場合、上記の内容の*フォルダ構造はそのまま*、追加するファイルのみ含めた状態でアーカイブ化する。

      例えばdic_supplement.txtというファイルをghost/master/に追加したいなら

      ```filetree
      +-(mysupplement)
      　　+-install.txt
      　　+-developer_options.txt (SSPのみ)
      　　+-ghost
      　　　　+-master
      　　　　　　+-dic_supplement.txt
      ```

      となる。

- **標準的な追加シェルの場合**:

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

- **標準的なバルーンの場合**:

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

- **ゴーストにバルーンなどを同梱する場合**:

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

  プラグインなどでも同様（シェルを同梱する場合はこうせずに普通にshellフォルダ以下に置けばよい）。

  また、同梱される側（上例のバルーン）にはinstall.txt不要。あっても無視される。

- **(SSP専用)複数インストール用パッケージ**:

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

  パッケージ用および個別の内容用それぞれに、別のinstall.txtが必要な点に注意。

  ghostに限らず単体のアーカイブにできるあらゆるものを同梱可能だが、shellやsupplementなど特定の対象があるものは、異なる対象のものを混ぜないように注意。

その他、ヘッドラインセンサ、プラグイン単体配布なども同様に、その一番上のディレクトリにinstall.txtを置く。

- **[install.txt](../descript/install/index.md)**: インストール設定を記載するテキスト。

  このファイルがなければD&Dなどによる自動インストール機能は動作しない。

  アーカイブの内容種別、アーカイブ名称、ディレクトリ名などを設定する。

  詳細は[リンク先](../descript/install/index.md)を参照。

- **[developer_options.txt](../descript/install/developer_options.txt/index.md)**: SSPのみ。省略可。

  install.txtと同じ場所に配置する。

  ただし複数インストール用パッケージの場合、最上位のinstall.txtではなく、各コンテンツのinstall.txtのある場所に用意する点に注意。

  SSPでnarを作る場合に、対象に含めないファイルなどを設定するためのファイル。

  書式など詳しくは[リンク先](../descript/install/developer_options.txt/index.md)を参照。
