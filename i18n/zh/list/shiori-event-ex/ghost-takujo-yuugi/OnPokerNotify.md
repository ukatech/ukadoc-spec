# OnPokerNotify

**カテゴリ:** ゴースト「桌上诱技」

无需响应的事件。

- **Reference0**: 协议版本(POKER/1.0)

## POKER/1.0中的Reference1及之后的附加信息

- **Reference1**: game_start
- **Reference\***: 成功加入的ghost名称

- **Reference1**: round_start
- **Reference2**: 盲注金额
- **Reference\***: ghost名称(以字节值1分隔)筹码

- **Reference1**: hand
- **Reference2**: 发到的卡牌信息
- **Reference3**: 发到的卡牌信息<br />
  花色由首字母(S,H,C,D)中的一个表示，后面接数字。<br />
  示例:<br />
  Reference2: S1<br />
  Reference3: H12<br />
  FLIP也使用此格式。

- **Reference1**: flip
- **Reference2**: 当前底池
- **Reference\***: 公共牌信息<br />
  如果是翻牌前，则不存在Reference3及之后的内容

- **Reference1**: blind_bet
- **Reference2**: 强制下注金额<br />
  通知已通过SB或BB进行强制下注。

- **Reference1**: bet（执行操作的玩家及下注相关信息。）
- **Reference2**: 当前下注总额
- **Reference3**: 当前下注额
- **Reference4**: 执行操作的玩家的ghost名称
- **Reference5**: 执行的操作

- **Reference1**: show_down（会发送摊牌时的卡牌信息。）
- **Reference\***: ghost名称(以字节值1分隔)第一张牌(以字节值1分隔)第二张牌

- **Reference1**: round_result（该轮获胜者及参与者剩余筹码的信息。）
- **Reference2**: 当前轮的获胜者以字节值1分隔后存入。
- **Reference\***: ghost名称(以字节值1分隔)筹码<br />
  通常只有一名获胜者，但也可能有两名或更多。<br />
  另外，筹码变为0只会在此处通知，请注意。

- **Reference1**: game_result
- **Reference2**: 游戏获胜者的ghost名称
