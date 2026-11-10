# 打开文件 / 保存文件 / 选择文件夹 / 选择调色板参数

- **--title=テキスト**: 对话框标题栏中显示的文本<br />
  省略时，open对话框显示“Open File”，save对话框显示“Save File”，folder对话框为空，color对话框显示“色の設定”。

- **--dir=パス**: 初始显示的文件夹，使用绝对路径指定<br />
  省略时使用上次在对话框中打开的文件夹

  <br />
  路径部分指定以下内容时，可以指定windows的特殊文件夹<br />
  \_\_system_mydocument\_\_<br />
  \_\_system_mypictures\_\_<br />
  \_\_system_myvideo\_\_<br />
  \_\_system_mymusic\_\_<br />
  \_\_system_desktop\_\_

- **--filter=フィルタ**: 按照 BMP|\*.bmp|其他|\*.png;\*.gif 的格式编写<br />
  仅对open对话框和save对话框有效。

- **--ext=拡張子**: 保存时的默认扩展名<br />
  仅对save对话框有效。

- **--name=ファイル名**: 保存时的默认文件名<br />
  仅对save对话框有效。

- **--id=イベントID**: 发送给OnSystemDialog/OnSystemDialogCancel的ID<br />
  将事件ID设为On～时，会触发该ID的事件。Reference的内容与OnSystemDialog相同。<br />
  根据对话框类型，Reference0中会填入“open”“save”或“folder”。
