# OnNotifyHolidayInfo

**カテゴリ:** Notifyイベント

今日の祝日名を通知。起動時、[OnNotifyUserInfo](OnNotifyUserInfo.md)の直後に送られる。*\[NOTIFY\]*<br />
SSPの言語フォルダにある祝日表(holidays.txt、地域設定の国別の表があればholidays-XX.txt)から今日の祝日名が取れたときだけ送られ、祝日でない日や、名前の載っていない祝日表では送られない。<br />
「今日」はSSPの「現在時刻の仮想的変更」(タイムマシン)の影響を受ける。

- **Reference0**: 祝日名。(元日、Christmas Day など。振替休日は「振替休日」や「Christmas Day (substitute day)」のようになる)
- **Reference1**: 日付。(2026,01,01のようにカンマ区切りで)
- **Reference2**: 読み込んだ祝日表の国コード(ISO 3166。holidays-GB.txtならGB)。国別でない既定の表(holidays.txt)なら空。

**対応:** SSP 2.9.11
