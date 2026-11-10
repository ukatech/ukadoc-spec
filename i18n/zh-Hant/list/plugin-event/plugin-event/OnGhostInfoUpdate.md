# OnGhostInfoUpdate

**カテゴリ:** PLUGIN Event

ghost 資訊變更時發生。<br />
載入時也可能發生。*\[NOTIFY\]*

- **Reference0**: 以位元組值1分隔，資訊已變更的 ghost 中`\0`之後各角色視窗的 HWND。<br />
  尚未建立等情況下，可能會是0。
- **Reference1**: 資訊已變更的 ghost 名稱。
- **Reference2**: 資訊已變更的 ghost 目前的 shell 名稱。
- **Reference3**: 資訊已變更的 ghost ID（與 Owned SSTP 傳送的相同）。
- **Reference4**: 資訊已變更的 ghost 完整路徑。

**対応:** SSP
