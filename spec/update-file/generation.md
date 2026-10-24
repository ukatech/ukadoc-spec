# 生成処理

SSPの「更新ファイル作成」機能などにより、ゴーストのファイル一覧からupdates2.dau / updates.txtを生成できる。

- **ファイル走査**: ディレクトリを再帰的に走査する。以下のファイルは除外される。

  - 隠しファイル (`FILE_ATTRIBUTE_HIDDEN`)
  - [developer_options.txt](../../descript/install/developer_options.txt/index.md) の `noupdate` で指定されたファイル
  - .gitignore形式のフィルタファイルで除外されたファイル

- **ghost\\masterへのコピー**: ディレクトリ直下に `ghost\master` フォルダが存在する場合、生成した更新ファイルをそこにもコピーする。
