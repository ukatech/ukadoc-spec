# OnBalloonBreak

**カテゴリ:** 氣球事件

以 SSTP 以外的方式中斷時觸發。

- **Reference0**: 發生中斷操作的腳本。
- **Reference1**: 發生中斷操作之氣球的 scope 編號。主方為0，搭檔方為1，依此類推。
- **Reference2**: 中斷位置。以從腳本開頭算起的字元數表示。字元數也包含 Sakura Script 標籤。<br />
  例如）在 `\s[2]`あいうえお 中斷於「あ」之前時，為6

**対応:** SSP / Ninix
