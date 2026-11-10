# OnWeatherStation.Astro

**カテゴリ:** プラグイン「Weather Station」

太陽と月に関する情報を、起動中のすべてのゴーストに送る。`\![raiseplugin]`で呼び出す必要がある。追加の引数で、どの日のデータを送るかを指定できる。0は今日、1は明日、2は明後日。引数がなければ今日になる。

- **Reference0**: 以下の情報が対象とする日。0は今日、1は明日、2は明後日。
- **Reference1**: 日の出の時刻。12時間表記で、形式は##:## \*M
- **Reference2**: 日の入りの時刻。12時間表記で、形式は##:## \*M
- **Reference3**: 月の出の時刻。12時間表記で、形式は##:## \*M
- **Reference4**: 月の入りの時刻。12時間表記で、形式は##:## \*M
- **Reference5**: 日の出の時刻。24時間表記で、形式は##:##
- **Reference6**: 日の入りの時刻。24時間表記で、形式は##:##
- **Reference7**: 月の出の時刻。24時間表記で、形式は##:##
- **Reference8**: 月の入りの時刻。24時間表記で、形式は##:##
- **Reference9**: 月相を表す文字列。"New Moon"、"Waxing Crescent"、"First Quarter"、"Waxing Gibbous"、"Full Moon"、"Waning Gibbous"、"Last Quarter"、"Waning Crescent"のいずれか。
- **Reference10**: 月相の番号。数値は次の月相に対応する。
  - 0 - New Moon
  - 1 - Waxing Crescent
  - 2 - First Quarter
  - 3 - Waxing Gibbous
  - 4 - Full Moon
  - 5 - Waning Gibbous
  - 6 - Last Quarter
  - 7 - Waning Crescent
- **Reference11**: 月の輝面比。パーセントで表す。
