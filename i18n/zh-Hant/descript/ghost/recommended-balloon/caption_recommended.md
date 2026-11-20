# 預設與推薦的使用區別

- **預設**：首次啟動或重設設定時應選擇的項目。<br />
  之後使用者可以自由變更。
- **推薦**：行為與「預設」相同，但*表示更強的相依關係*。<br />
  嘗試切換到其他 balloon 時可能會出現警告。<br />
  隨意設定會剝奪使用者的選擇權，因此除非有非常強的相依關係，否則*不要任意指定*。<br />
  如果只是想防止部分 balloon 被刪除，指定為「預設」也會出現警告。
- **shell 的預設值**：也可在 shell 的 descript.txt 的 [balloon](../../shell/descript-txt/balloon.md) 中指定預設值。<br />
  切換 shell 時，若使用者曾在該 shell 中切換過 balloon，則切換至該 balloon；否則依「ghost 的推薦值 ＞ shell 的預設值 ＞ ghost 的預設值」順序決定切換目標。
- **其他**：也可從 balloon 側設定「推薦」關係。詳情請參閱 [Balloon 的 descript.txt 設定](../../balloon/index.md)。
