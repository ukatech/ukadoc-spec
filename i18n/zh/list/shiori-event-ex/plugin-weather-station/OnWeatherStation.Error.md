# OnWeatherStation.Error

**カテゴリ:** plugin“Weather Station”

向所有运行中的ghost发送错误信息。发生任何错误时，将发送此事件以代替前述事件。

- **Reference0**: 错误消息。可能的错误消息参见[※下文](note-1.md#エラーの理由)。
- **Reference1**: 由weatherapi.com提供的更详细的错误消息。*这些错误消息与weatherapi的在线文档不一致，不得用于识别错误。*
- **Reference2**: weatherapi.com文档中列出的错误代码。
- **Reference3**: plugin最后一次尝试更新天气数据的时间，以自EPOCH（1970/1/1 00:00:00）起的秒数表示。
- **Reference4**: plugin的当前版本号。
- **Reference5**: 有可用的plugin更新时为1，否则为0。用户离线时始终为0。
