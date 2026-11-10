# OnOtherGhostTalk

**カテゴリ:** 其他事件

其他ghost说话时会触发此事件。使用`\![set,otherghosttalk,true]`启用。

- **Reference0**: ghost名称。
- **Reference1**: ghost的本体侧名称。
- **Reference2**: 中断对话时为break。<br />
  Communicate时为communicate。<br />
  SSTP SEND时为sstp-send。<br />
  Owned SSTP时为owned。<br />
  非本地SSTP时为remote。<br />
  指定不进行翻译时为notranslate<br />
  来自plugin的脚本时为plugin-script<br />
  来自plugin的事件响应时为plugin-event<br />
  符合条件的项目以逗号分隔后返回。
- **Reference3**: 其他ghost说话时的事件ID。
- **Reference4**: 其他ghost说话内容的脚本。
- **Reference5**: 以字节值1分隔的传递给其他ghost的Reference。

**対応:** SSP / Ninix
