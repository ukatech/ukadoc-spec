# OnMahjong

**カテゴリ:** 麻將通訊事件

在遊戲的各個時點通知。請參閱下述[※伺服器指令](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)。

- **Reference0**: 版本（UKAJONG/0.2）
- **Reference1**: [※伺服器指令](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)
- **Reference\***: 依據[※伺服器指令](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)而定的附加資訊

## UKAJONG/0.2 的伺服器指令及其附加資訊

- **Reference1**: gamestart（遊戲開始時）
- **Reference2**: 座位（東|南|西|北）
- **Reference3**: 玩家名稱1
- **Reference4**: 玩家名稱2
- **Reference5**: 玩家名稱3
- **Reference6**: 玩家名稱4

- **Reference1**: gameend（遊戲結束時）
- **Reference2**: 玩家名稱1（位元組值１）分數
- **Reference3**: 玩家名稱2（位元組值１）分數
- **Reference4**: 玩家名稱3（位元組值１）分數
- **Reference5**: 玩家名稱4（位元組值１）分數

- **Reference1**: kyokustart（一局開始時）
- **Reference2**: 場風（東|南|西|北）
- **Reference3**: 莊家玩家名稱
- **Reference4**: 本場數（例如 1）
- **Reference5**: 供託（例如 1000）

- **Reference1**: kyokuend（一局結束時）

- **Reference1**: point（通知玩家分數）
- **Reference2**: 玩家名稱
- **Reference3**: (=|+|-) = 表示直接指定分數，+- 表示增減
- **Reference4**: 分數

- **Reference1**: haipai（發配牌時）
- **Reference2**: 玩家名稱
- **Reference3**: 配牌（例如 1m2m3m4p5p6p7s8s9s1z5z6z7z）

- **Reference1**: dora（傳送寶牌指示牌時）
- **Reference2**: 牌（例如 7z）

- **Reference1**: open（公開手牌時，例如吃、碰、槓等）
- **Reference2**: 玩家名稱
- **Reference3**: 牌（例如 1p2p3p）

- **Reference1**: tsumo（自摸時）
- **Reference2**: 玩家名稱（自己）
- **Reference3**: 剩餘張數
- **Reference4**: 牌（例如 7z）

- **Reference1**: sutehai（打出牌時）
- **Reference2**: 玩家名稱（自己）
- **Reference3**: 牌（例如 7z）

- **Reference1**: say（宣告時）
- **Reference2**: 玩家名稱
- **Reference3**: 宣告內容（chi|pon|kan|ron|tsumo|richi|tenpai|noten）

- **Reference1**: agari（和牌時）
- **Reference2**: 玩家名稱
- **Reference3**: 符
- **Reference4**: 役,翻數
- **Reference5**: 以下同 Reference4

- **Reference1**: ryukyoku（流局時）

以下指令需要回覆。若要求方是 GHOST，可以使用`\![raiseother]`等方式回覆；若要求方是外部應用程式，且以 SSTP 通知，則必須使用 X-SSTP-PassThru-\* 標頭回覆。

使用`\![raiseother]`回覆時，請傳回 OnMahjongResponse 事件。使用 SHIORI 回應標頭時，請設定為 X-SSTP-PassThru-ID: OnMahjongResponse。

若將要求的對象設為空字串，則視為委由伺服器處理。

- **Reference1**: hello（確認連線）

- **Reference1**: sutehai?（詢問要打出的牌）

- **Reference1**: naku?（詢問是否要鳴牌。也會傳送用戶端可執行的指令）
- **Reference2**: (ron|kan|pon|chi)
- **Reference3**: 以下同 Reference2

- **Reference1**: tenpai?（詢問是否宣告聽牌）
