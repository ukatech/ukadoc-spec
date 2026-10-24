# developer.log.ログ種別.index(ID).ログプロパティ名

**カテゴリ:** プロパティシステム

ログのうちID番目のものから情報を取得。<br />
IDは新しいものから順に0,1,2...となる。範囲外のIDを指定した場合は取得失敗となる。<br />
ログ種別は[developer.log.ログ種別.count](developer.log.-.count.md)を参照。ログプロパティ名に入る文字列は以下の通り。

- **type**: ログの種類。<br />
  scriptではGhost(～)またはSSTP(～)の形式で、括弧内には該当する属性がカンマ区切りで入る（Ghost：External、Embed、SSF、Plugin　SSTP：LocalまたはRemote、TempGhost、Auth　共通：NoTranslate）。Ghostで該当する属性が無い場合は括弧ごと省略されGhostのみになる。付加情報がある場合は末尾に「:付加情報」が付く。<br />
  その他のログ種別ではInfo、Notice、Warning、Error、Critical、Systemのいずれか。
- **name**: ログの発生元の名前（ゴースト名など）。発生元が無い場合は\[SYSTEM\]。
- **value**: ログの本文。長いものも省略されずに全文が返る。
- **time**: ログが記録された日時。ローカル時刻で、OSの短い日付形式と24時間表記の時:分を半角スペースで区切ったもの。書式はOSの地域設定に依存する。

**対応:** SSP
