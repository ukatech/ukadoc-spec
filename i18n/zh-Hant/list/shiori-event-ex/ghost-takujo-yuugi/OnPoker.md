# OnPoker

**カテゴリ:** ghost「卓上誘技」

需要回應的事件。請使用raiseother或notifyother回應。

- **Reference0**: 通訊協定版本(POKER/1.0)
- **Reference1**: 伺服器ghost名稱
- **Reference2**: 伺服器事件名稱

## POKER/1.0的Reference3以後的追加資訊

- **Reference3**: hello（申請參加。也可能遭到拒絕。）

- **Reference3**: action（Reference4以後會列出可使用的動作。）
- **Reference\***: 可使用的動作為bet、raise、allin、check、call、fold六種中的部分動作。<br />
  請注意，若未回應，系統會自動執行fold。<br />
  若要執行bet/raise，也必須傳送加注金額。
