# OnOtherGhostTalk

**カテゴリ:** 其他事件

其他 ghost 發話時會發生。使用 `\![set,otherghosttalk,true]` 啟用。

- **Reference0**: ghost 名稱。
- **Reference1**: ghost 的主程式端名稱。
- **Reference2**: 中斷談話時為 break。<br />
  對話時為 communicate。<br />
  SSTP SEND 時為 sstp-send。<br />
  Owned SSTP 時為 owned。<br />
  非本機 SSTP 時為 remote。<br />
  指定不進行轉換時為 notranslate<br />
  從 plugin 傳入腳本時為 plugin-script<br />
  回應 plugin 事件時為 plugin-event<br />
  符合的項目會以逗號分隔回傳。
- **Reference3**: 其他 ghost 發話的事件 ID。
- **Reference4**: 其他 ghost 發話內容的腳本。
- **Reference5**: 傳給其他 ghost、以位元組值 1 分隔的 Reference。

**対応:** SSP / Ninix
