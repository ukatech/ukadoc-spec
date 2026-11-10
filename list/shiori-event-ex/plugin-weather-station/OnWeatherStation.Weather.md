# OnWeatherStation.Weather

**カテゴリ:** プラグイン「Weather Station」

現在の気象状況に関する情報を、起動中のすべてのゴーストに送る。このイベントは1時間ごと、ほかのゴーストが起動するたび、いずれかのゴーストが`\![raiseplugin]`で要求したときに発生する。

- **Reference0**: 天気の状況。考えられる状況の一覧は[※下記](note-1.md#天気の状況と状況コードの一覧)を参照。
- **Reference1**: 天気の状況を表すアイコンのファイル名。weatherapiの[天気アイコンパック](https://cdn.weatherapi.com/weather.zip)と組み合わせて使う。
- **Reference2**: 天気の状況コード。考えられる状況コードの一覧は[※下記](note-1.md#天気の状況と状況コードの一覧)を参照。
- **Reference3**: 昼間かどうか。太陽が出ていれば1、沈んでいれば0。
- **Reference4**: 気温（華氏）。
- **Reference5**: 気温（摂氏）。
- **Reference6**: 「体感」温度（華氏）。
- **Reference7**: 「体感」温度（摂氏）。
- **Reference8**: 湿度（パーセント）。
- **Reference9**: 風速（マイル毎時）。
- **Reference10**: 風速（キロメートル毎時）。
- **Reference11**: 風向（16方位。例: NNEは北北東）。
- **Reference12**: 風向（度）。
- **Reference13**: 突風の風速（マイル毎時）。
- **Reference14**: 突風の風速（キロメートル毎時）。
- **Reference15**: 降水量（インチ）。
- **Reference16**: 降水量（ミリメートル）。
- **Reference17**: 雲量（パーセント）。
- **Reference18**: 「今日は雨が降るか」。降るなら1、降らないなら0。OnWeatherStation.Forecast.Dayの「今日は雨が降るか」と同じ情報。
- **Reference19**: 今日雨が降る確率（パーセント）。OnWeatherStation.Forecast.Dayの雨が降る確率と同じ情報。
- **Reference20**: 「今日は雪が降るか」。降るなら1、降らないなら0。OnWeatherStation.Forecast.Dayの「今日は雪が降るか」と同じ情報。
- **Reference21**: 今日雪が降る確率（パーセント）。OnWeatherStation.Forecast.Dayの雪が降る確率と同じ情報。
- **Reference22**: 視程（マイル）。
- **Reference23**: 視程（キロメートル）。
- **Reference24**: 気圧（インチ）。
- **Reference25**: 気圧（ミリバール）。
- **Reference26**: UV指数。
- **Reference27**: CO（一酸化炭素）。単位はμg/m3（1立方メートルあたりのマイクログラム）。
- **Reference28**: O3（オゾン）。単位はμg/m3（1立方メートルあたりのマイクログラム）。
- **Reference29**: NO2（二酸化窒素）。単位はμg/m3（1立方メートルあたりのマイクログラム）。
- **Reference30**: SO2（二酸化硫黄）。単位はμg/m3（1立方メートルあたりのマイクログラム）。
- **Reference31**: PM2.5（直径2.5ミクロン未満の粒子状物質）。単位はμg/m3（1立方メートルあたりのマイクログラム）。
- **Reference32**: PM10（直径10ミクロン未満の粒子状物質）。単位はμg/m3（1立方メートルあたりのマイクログラム）。
- **Reference33**: US EPA指数。1は良好、2は中程度、3は敏感な人に不健康、4は不健康、5は非常に不健康、6は危険。
- **Reference34**: UK Defra指数。詳細は[※下記](note-1.md#uk-defra指数の早見表)を参照。
- **Reference35**: ユーザーが選んだ単位系（ImperialまたはMetric）。
- **Reference36**: プラグインが最後に天気データを更新した時刻。EPOCH（1970/1/1 00:00:00）からの秒数。
- **Reference37**: プラグインの現在のバージョン番号。
- **Reference38**: &lt;Deprecated\>
- **Reference39**: &lt;Deprecated\>
- **Reference40**: &lt;Deprecated\>
- **Reference41**: &lt;Deprecated\>
