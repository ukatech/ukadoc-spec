# OnMenuExec

**カテゴリ:** PLUGIN Event

從 owner draw 選單執行 plugin 時發生。<br />
建議進行某種回應。

- **Reference0**: 以位元組值1分隔，呼叫 plugin 的 ghost 中`\0`之後各角色視窗的 HWND。<br />
  可能會是0，例如尚未建立視窗等情況。
- **Reference1**: 呼叫 plugin 的 ghost 名稱。
- **Reference2**: 呼叫 plugin 的 ghost 目前的 shell 名稱。
- **Reference3**: 呼叫 plugin 的 ghost ID（與 Owned SSTP 傳送的相同）。
- **Reference4**: 呼叫 plugin 的 ghost 完整路徑。

**対応:** SSP
