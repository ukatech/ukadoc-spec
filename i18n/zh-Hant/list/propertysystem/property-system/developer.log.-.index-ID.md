# developer.log.ログ種別.index(ID).ログプロパティ名

**カテゴリ:** 屬性系統

從指定 ID 的記錄中取得資訊。<br />
ID 會按照新到舊的順序從 0、1、2... 編號。指定超出範圍的 ID 時，取得會失敗。<br />
記錄種類請參閱[developer.log.ログ種別.count](developer.log.-.count.md)。記錄屬性名稱可使用以下字串。

- **type**: 記錄種類。<br />
  script 中會以 Ghost(～) 或 SSTP(～) 的格式表示，括號內以逗號分隔列出對應屬性（Ghost：External、Embed、SSF、Plugin　SSTP：Local 或 Remote、TempGhost、Auth　共通：NoTranslate）。Ghost 沒有對應屬性時，會省略括號，只顯示 Ghost。有附加資訊時，末尾會加上「:附加資訊」。<br />
  其他記錄種類則為 Info、Notice、Warning、Error、Critical、System 其中之一。
- **name**: 記錄來源名稱（例如 ghost 名稱）。沒有來源時為\[SYSTEM\]。
- **value**: 記錄內容。即使內容很長，也會完整回傳，不會省略。
- **time**: 記錄寫入的日期與時間。使用當地時間，並以半形空格分隔 OS 的短日期格式和 24 小時制的時:分。格式取決於 OS 的地區設定。

**対応:** SSP
