# OnOtherGhostTalk

**カテゴリ:** PLUGIN Event

ghost 说话时触发。<br />
可通过 descript.txt 中的 [otherghosttalk 进行设置。](../../../descript/plugin/descript-txt/otherghosttalk.md)

- **Reference0**: ghost 名称。
- **Reference1**: ghost 的 baseware 侧名称。
- **Reference2**: 中断对话时为 break。<br />
  通过沟通触发时为 communicate。<br />
  通过 SSTP SEND 触发时为 sstp-send。<br />
  通过 Owned SSTP 触发时为 owned。<br />
  通过非本地 SSTP 触发时为 remote。<br />
  指定不进行翻译时为 notranslate<br />
  脚本来自插件时为 plugin-script<br />
  事件响应来自插件时为 plugin-event<br />
  符合条件的项目以逗号分隔后返回。
- **Reference3**: ghost 说话时触发的事件 ID。
- **Reference4**: ghost 所说内容的脚本。
- **Reference5**: 以字节值1分隔的传递给 ghost 的 Reference。

**対応:** SSP
