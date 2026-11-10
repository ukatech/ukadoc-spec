# OnWeatherStation.Error

**カテゴリ:** 插件「Weather Station」

将错误信息发送给所有正在运行的 ghost。发生任何错误时，会发送此事件，而非前述事件。

- **Reference0**: 错误消息。可能的错误消息请参阅[※下文](note-1.md#エラーの理由)。
- **Reference1**: weatherapi.com提供的更详细错误消息。*此错误消息与weatherapi的在线文档不一致，因此不得用于识别错误。*
- **Reference2**: weatherapi.com文档中列出的错误代码。
- **Reference3**: 插件上次尝试更新天气数据的时间。自EPOCH（1970/1/1 00:00:00）起的秒数。
- **Reference4**: 插件当前的版本号。
- **Reference5**: 有插件更新时为1，否则为0。用户处于离线状态时始终为0。
