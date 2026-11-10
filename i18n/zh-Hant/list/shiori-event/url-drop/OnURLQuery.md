# OnURLQuery

**カテゴリ:** URL 拖放事件

URL 被拖放至角色視窗時會收到通知。<br />
若對此事件回傳腳本，一般下載處理就會取消。<br />
只有在 ghost 端需要自行處理 URL 時才回傳腳本。

- **Reference0**: URL 路徑。
- **Reference1**: 本體為0，搭檔為1。SSP/CROW也可能為2以上。
- **Reference2**: 拖放的 URL MIME 類型
- **Reference3**: 若未處理，SSP 預定接下來執行的處理。<br />
  為feed、nar、homeurl、ical、ssf、unknown其中之一。<br />
  若為unknown，表示本體無法處理該 URL，因此本體端無法再進一步處理。<br />
  其他情況下，將此值與Reference0一同傳入 [`\![execute,dropdefault,url]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)\[2.9.10\] 或 [`\![execute,install,url]`](../../sakura-script/misc/bang-execute-install-url-URL.md)，即可繼續處理。

**対応:** SSP 的Ref3支援於2.6.35起
