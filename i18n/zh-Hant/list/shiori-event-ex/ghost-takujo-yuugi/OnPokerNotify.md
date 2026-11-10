# OnPokerNotify

**カテゴリ:** ghost「卓上誘技」

不需要回應的事件。

- **Reference0**: 通訊協定版本(POKER/1.0)

## POKER/1.0的Reference1以後的追加資訊

- **Reference1**: game_start
- **Reference\***: 成功參加的ghost名稱

- **Reference1**: round_start
- **Reference2**: 盲注金額
- **Reference\***: ghost名稱(位元組值1)籌碼

- **Reference1**: hand
- **Reference2**: 發到的牌面資訊
- **Reference3**: 發到的牌面資訊<br />
  花色為首字母(S,H,C,D)其中之一，後面接數字。<br />
  例：<br />
  Reference2: S1<br />
  Reference3: H12<br />
  FLIP也使用此格式。

- **Reference1**: flip
- **Reference2**: 目前底池
- **Reference\***: 公共牌資訊<br />
  若為翻牌前階段，則沒有Reference3以後的資料

- **Reference1**: blind_bet
- **Reference2**: 強制下注金額<br />
  會通知玩家已在SB或BB位置進行強制下注。

- **Reference1**: bet（進行動作的玩家與下注相關資訊。）
- **Reference2**: 目前下注總額
- **Reference3**: 目前下注額
- **Reference4**: 進行動作的玩家ghost名稱
- **Reference5**: 執行的動作

- **Reference1**: show_down（會傳送攤牌時的牌面資訊。）
- **Reference\***: ghost名稱(位元組值1)第一張牌(位元組值1)第二張牌

- **Reference1**: round_result（該回合勝者及參加者剩餘籌碼的資訊。）
- **Reference2**: 目前回合的勝者以位元組值1分隔列出。
- **Reference\***: ghost名稱(位元組值1)籌碼<br />
  勝者通常只有一人，但也可能有兩人以上。<br />
  請注意，只有在此處才會通知籌碼歸零的情況。

- **Reference1**: game_result
- **Reference2**: 遊戲勝者的ghost名稱
