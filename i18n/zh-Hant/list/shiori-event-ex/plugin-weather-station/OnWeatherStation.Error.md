# OnWeatherStation.Error

**カテゴリ:** 外掛程式「Weather Station」

將錯誤資訊傳送給所有正在執行的 ghost。發生任何錯誤時，會傳送此事件，而非前述事件。

- **Reference0**: 錯誤訊息。可能的錯誤訊息請參閱[※下方](note-1.md#エラーの理由)。
- **Reference1**: weatherapi.com 提供的詳細錯誤訊息。*此錯誤訊息與 weatherapi 的線上文件不一致，因此不得用於識別錯誤。*
- **Reference2**: weatherapi.com 文件中記載的錯誤代碼。
- **Reference3**: 外掛程式上次嘗試更新天氣資料的時間。自 EPOCH（1970/1/1 00:00:00）起算的秒數。
- **Reference4**: 外掛程式目前的版本號。
- **Reference5**: 外掛程式有更新時為 1，沒有更新時為 0。使用者離線時一律為 0。
