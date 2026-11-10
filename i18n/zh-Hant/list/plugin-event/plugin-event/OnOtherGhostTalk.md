# OnOtherGhostTalk

**カテゴリ:** PLUGIN Event

ghost 說話時發生。<br />
可在descript.txt的[otherghosttalk中設定。](../../../descript/plugin/descript-txt/otherghosttalk.md)

- **Reference0**: ghost 名稱。
- **Reference1**: ghost 的 baseware 端名稱。
- **Reference2**: 中斷對話時為 break。<br />
  Communicate 時為 communicate。<br />
  SSTP SEND 時為 sstp-send。<br />
  Owned SSTP 時為 owned。<br />
  非本機 SSTP 時為 remote。<br />
  指定不進行翻譯時為 notranslate<br />
  來自 plugin 的 script 時為 plugin-script<br />
  來自 plugin 的事件回應時為 plugin-event<br />
  符合的項目會以逗號分隔後傳回。
- **Reference3**: ghost 說話時的事件 ID。
- **Reference4**: ghost 說話內容的 script。
- **Reference5**: 傳給 ghost、以位元組值1分隔的 Reference。

**対応:** SSP
