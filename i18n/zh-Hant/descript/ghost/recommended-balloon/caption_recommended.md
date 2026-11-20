# 預設與推薦的使用區別

- **預設**: 首次啟動或重設設定時應選用的項目。<br />
  使用者日後可自由變更。
- **推薦**: 行為與「預設」相同，但*表示更強的依賴關係*。<br />
  嘗試切換至其他 balloon 時可能會出現警告。<br />
  隨意設定會剝奪使用者的選擇權，因此除非有非常強的依賴關係，否則*不要隨意指定*。<br />
  若只是想避免部分 balloon 被刪除，即使指定為「預設」也會出現警告。
- **shell 的預設值**: 也可在 shell 的 descript.txt 的 [balloon](../../shell/descript-txt/balloon.md) 中指定預設值。使用者未明確切換 balloon 時，每次切換 shell，balloon 都會依照該 shell 的指定切換。<br />
  優先順序為：使用者明確切換的 balloon ＞ ghost 的推薦值 ＞ shell 的預設值 ＞ ghost 的預設值。
- **其他**: 也可從 balloon 端設定「推薦」關係。詳情請參閱 [Balloon 的 descript.txt 記述](../../balloon/index.md)。
