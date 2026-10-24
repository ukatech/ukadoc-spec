# OnMahjong

**カテゴリ:** 麻雀通信イベント

ゲームの各タイミングで通知。後述の[※サーバコマンド](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)参照。

- **Reference0**: バージョン（UKAJONG/0.2）
- **Reference1**: [※サーバコマンド](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)
- **Reference\***: [※サーバコマンド](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)に応じた追加情報

## UKAJONG/0.2におけるサーバコマンドとその追加情報

- **Reference1**: gamestart（ゲーム開始時）
- **Reference2**: 席（東|南|西|北）
- **Reference3**: プレイヤー名1
- **Reference4**: プレイヤー名2
- **Reference5**: プレイヤー名3
- **Reference6**: プレイヤー名4

- **Reference1**: gameend（ゲーム終了時）
- **Reference2**: プレイヤー名1（バイト値１）点数
- **Reference3**: プレイヤー名2（バイト値１）点数
- **Reference4**: プレイヤー名3（バイト値１）点数
- **Reference5**: プレイヤー名4（バイト値１）点数

- **Reference1**: kyokustart（一局開始時）
- **Reference2**: 場風（東|南|西|北）
- **Reference3**: 親プレイヤー名
- **Reference4**: 本場（例 1）
- **Reference5**: 供託（例 1000）

- **Reference1**: kyokuend（一局終了時）

- **Reference1**: point（プレイヤーの点数を通知）
- **Reference2**: プレイヤー名
- **Reference3**: (=|+|-) =は点数の直指定、+-は増減を意味する
- **Reference4**: 点数

- **Reference1**: haipai（配牌を配る時）
- **Reference2**: プレイヤー名
- **Reference3**: 配牌（例 1m2m3m4p5p6p7s8s9s1z5z6z7z）

- **Reference1**: dora（ドラ表示牌を送る時）
- **Reference2**: 牌（例 7z）

- **Reference1**: open（手牌を公開する時 チー、ポン、カン等）
- **Reference2**: プレイヤー名
- **Reference3**: 牌（例 1p2p3p）

- **Reference1**: tsumo（ツモの時）
- **Reference2**: プレイヤー名（自分）
- **Reference3**: 残り枚数
- **Reference4**: 牌（例 7z）

- **Reference1**: sutehai（捨牌時）
- **Reference2**: プレイヤー名（自分）
- **Reference3**: 牌（例 7z）

- **Reference1**: say（発声時）
- **Reference2**: プレイヤー名
- **Reference3**: 発声内容（chi|pon|kan|ron|tsumo|richi|tenpai|noten）

- **Reference1**: agari（あがりの時）
- **Reference2**: プレイヤー名
- **Reference3**: 符
- **Reference4**: 役,ハン数
- **Reference5**: 以降、Reference4同様

- **Reference1**: ryukyoku（流局時）

以下のコマンドは返信が要求されている。要求元がGHOSTである場合は`\![raiseother]`等で返信しても良いが、要求元が外部アプリでSSTPによる通知であった場合はX-SSTP-PassThru-\*ヘッダを用いて返信する必要がある。

`\![raiseother]`で返信する場合はOnMahjongResponseイベントを返す。SHIORIレスポンスヘッダを用いる場合はX-SSTP-PassThru-ID: OnMahjongResponseとする。

要求された対象に空文字を設定した場合、サーバーに対応を委任したものとみなす。

- **Reference1**: hello（接続確認）

- **Reference1**: sutehai?（捨牌を尋ねる）

- **Reference1**: naku?（牌を鳴くか尋ねる。クライアントが可能なコマンドも送る）
- **Reference2**: (ron|kan|pon|chi)
- **Reference3**: 以降、Reference2同様

- **Reference1**: tenpai?（テンパイを宣言するか尋ねる）
