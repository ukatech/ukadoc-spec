# Open File / Save File / Select Folder / Select Color Palette Parameters

- **--title=テキスト**: Text displayed in the dialog title bar<br />
  If omitted, the default is “Open File” for the open dialog, “Save File” for the save dialog, blank for the folder dialog, and “色の設定” for the color dialog.

- **--dir=パス**: Initial folder, specified as an absolute path<br />
  If omitted, the folder opened in the previous dialog is used.

  <br />
  Specify one of the following in the path to use a special Windows folder<br />
  \_\_system_mydocument\_\_<br />
  \_\_system_mypictures\_\_<br />
  \_\_system_myvideo\_\_<br />
  \_\_system_mymusic\_\_<br />
  \_\_system_desktop\_\_

- **--filter=フィルタ**: Specify in the format BMP|\*.bmp|Other|\*.png;\*.gif<br />
  Valid only for the open and save dialogs.

- **--ext=拡張子**: Default extension when saving<br />
  Valid only for the save dialog.

- **--name=ファイル名**: Default file name when saving<br />
  Valid only for the save dialog.

- **--id=イベントID**: ID to send with OnSystemDialog/OnSystemDialogCancel<br />
  If the event ID starts with On～, an event with that ID is triggered. The references are the same as those for OnSystemDialog.<br />
  Reference0 contains one of “open”, “save”, or “folder”, depending on the dialog type.
