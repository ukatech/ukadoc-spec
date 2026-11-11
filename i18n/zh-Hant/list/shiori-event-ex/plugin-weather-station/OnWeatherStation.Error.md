# OnWeatherStation.Error

**カテゴリ:** plugin「Weather Station」

將錯誤資訊傳送給所有執行中的 ghost。發生任何錯誤時，會傳送此事件，取代前述事件。

- **Reference0**: 錯誤訊息。可能的錯誤訊息請參閱[※下文](note-1.md#エラーの理由)。
- **Reference1**: 由 weatherapi.com 提供的更詳細錯誤訊息。*這些錯誤訊息與 weatherapi 的線上文件不一致，不應用於識別錯誤。*
- **Reference2**: weatherapi.com 文件中記載的錯誤代碼。
- **Reference3**: plugin 上次嘗試更新天氣資料的時間，以自 EPOCH（1970/1/1 00:00:00）起算的秒數表示。
- **Reference4**: plugin 目前的版本號碼。
- **Reference5**: 有 plugin 更新時為1，否則為0。使用者離線時一律為0。
