# ファイルを開く / ファイルを保存 / フォルダ選択 / カラーパレット選択 パラメータ

- **--title=テキスト**: ダイアログのタイトルバーに表示されるテキスト<br />
  省略した場合、openダイアログなら「Open File」、saveダイアログなら「Save File」、folderダイアログなら空欄、colorダイアログなら「色の設定」。

- **--dir=パス**: 初期表示フォルダ、絶対パスで指定<br />
  省略した場合は前回ダイアログで開いたフォルダ

  <br />
  パス部分に以下で、windowsの特殊なフォルダの指定が可能<br />
  \_\_system_mydocument\_\_<br />
  \_\_system_mypictures\_\_<br />
  \_\_system_myvideo\_\_<br />
  \_\_system_mymusic\_\_<br />
  \_\_system_desktop\_\_

- **--filter=フィルタ**: BMP|\*.bmp|その他|\*.png;\*.gif のように記述<br />
  openダイアログとsaveダイアログのみ有効。

- **--ext=拡張子**: 保存時の標準拡張子<br />
  saveダイアログのみ有効。

- **--name=ファイル名**: 保存時の標準ファイル名<br />
  saveダイアログのみ有効。

- **--id=イベントID**: OnSystemDialog/OnSystemDialogCancelに送るID<br />
  イベントIDをOn～にするとそのIDのイベントが発生する。Referenceの内容はOnSystemDialogと同じ。<br />
  Reference0はダイアログの種類によって「open」「save」「folder」のいずれかが入っている。
