# OnGetValues

**カテゴリ:** ghost 間通用事件

收到 OnRequestValues 時應回傳的事件。

- **Reference0**: 傳送端 ghost 名稱。
- **Reference1**: key=value（key 是 OnRequestValues 收到的變數名稱，value 是該變數的值）。Reference2 以後也依此類推，直到列出所有要求的變數。不存在的變數不回傳。順序不受 OnRequestValues 傳送順序影響。

**対応:** SSP
