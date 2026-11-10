# 開啟檔案 / 儲存檔案 / 選擇資料夾 / 選擇調色盤的參數

- **--title=テキスト**: 顯示於對話框標題列的文字<br />
  省略時，open 對話框顯示「Open File」、save 對話框顯示「Save File」、folder 對話框顯示空白、color 對話框顯示「色の設定」。

- **--dir=パス**: 初始顯示的資料夾，以絕對路徑指定<br />
  省略時，使用上次在對話框中開啟的資料夾

  <br />
  在路徑部分指定以下內容，即可指定 Windows 的特殊資料夾<br />
  \_\_system_mydocument\_\_<br />
  \_\_system_mypictures\_\_<br />
  \_\_system_myvideo\_\_<br />
  \_\_system_mymusic\_\_<br />
  \_\_system_desktop\_\_

- **--filter=フィルタ**: 以 BMP|\*.bmp|其他|\*.png;\*.gif 的格式指定<br />
  僅對 open 對話框和 save 對話框有效。

- **--ext=拡張子**: 儲存時的預設副檔名<br />
  僅對 save 對話框有效。

- **--name=ファイル名**: 儲存時的預設檔名<br />
  僅對 save 對話框有效。

- **--id=イベントID**: 傳送給 OnSystemDialog/OnSystemDialogCancel 的 ID<br />
  將事件 ID 設為 On～時，會觸發該 ID 的事件。Reference 的內容與 OnSystemDialog 相同。<br />
  Reference0 會依對話框種類，設為「open」、「save」或「folder」。
