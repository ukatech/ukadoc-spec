# OnStampInfo

**カテゴリ:** plugin「印章簿」

通知印章相關資訊的事件。<br />
在 ghost 啟動時、plugin 載入或卸載時，以及傳送 OnStampInfoCall 的任意時間點發生。

- **Reference0**: 印章總數。
- **Reference1**: 是否有此 ghost 的印章。有則為 1，無則為 0。<br />
  同時啟動多個 ghost 時，資訊的可信度會降低；若要確實確認，建議透過 OnStampInfoCall 主動觸發此事件。
- **Reference2**: plugin 的路徑。
- **Reference3**: 所有印章資訊。ghost 名稱、印章圖片檔名、印章標題、印章留言及蓋印時間以位元組值 1 分隔；依印章數量重複各組資料，並以位元組值 2 分隔。
- **Reference4**: 此 plugin 正在執行時為 1，否則為 0。
