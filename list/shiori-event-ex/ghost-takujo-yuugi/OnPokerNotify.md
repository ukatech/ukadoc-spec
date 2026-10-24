# OnPokerNotify

**カテゴリ:** ゴースト「卓上誘技」

応答する必要の無いイベント。

- **Reference0**: プロトコルバージョン(POKER/1.0)

## POKER/1.0におけるReference1以降の追加情報

- **Reference1**: game_start
- **Reference\***: 参加できたゴースト名

- **Reference1**: round_start
- **Reference2**: ブラインドの金額
- **Reference\***: ゴースト名(バイト値1)スタック

- **Reference1**: hand
- **Reference2**: 配られたカードの情報
- **Reference3**: 配られたカードの情報<br />
  スートは頭文字(S,H,C,D)の4つのいずれか、その後に数字が続く。<br />
  例:<br />
  Reference2: S1<br />
  Reference3: H12<br />
  この形式はFLIPでも一緒。

- **Reference1**: flip
- **Reference2**: 現在のポット
- **Reference\***: コミュニティカードの情報<br />
  プリフロップならReference3以降は存在しない

- **Reference1**: blind_bet
- **Reference2**: 強制ベットの金額<br />
  SBやBBでの強制ベットをしたことが通知される。

- **Reference1**: bet（アクションを行ったプレイヤーとベット周りの情報。）
- **Reference2**: 現在のベット総額
- **Reference3**: 現在のベット額
- **Reference4**: アクションを行ったプレイヤーのゴースト名
- **Reference5**: 行ったアクション

- **Reference1**: show_down（ショーダウン時のカード情報が送られてくる。）
- **Reference\***: ゴースト名(バイト値1)1枚目のカード(バイト値1)2枚目のカード

- **Reference1**: round_result（そのラウンドの勝者、および参加者の残りスタックの情報。）
- **Reference2**: 現在のラウンドの勝者がバイト値1区切りで入っている。
- **Reference\***: ゴースト名(バイト値1)スタック<br />
  基本的に勝者は1人だが2人以上になるケースもある。<br />
  また、スタックが0になったのはここでしか通知しないため注意。

- **Reference1**: game_result
- **Reference2**: ゲームの勝者のゴースト名
