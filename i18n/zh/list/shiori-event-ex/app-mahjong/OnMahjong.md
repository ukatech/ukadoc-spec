# OnMahjong

**カテゴリ:** 麻将通信事件

在游戏的各个时点发送通知。参见下文的[※服务器命令](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)。

- **Reference0**: 版本（UKAJONG/0.2）
- **Reference1**: [※服务器命令](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)
- **Reference\***: 根据[※服务器命令](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)提供的附加信息

## UKAJONG/0.2中的服务器命令及其附加信息

- **Reference1**: gamestart（游戏开始时）
- **Reference2**: 座位（东|南|西|北）
- **Reference3**: 玩家名称1
- **Reference4**: 玩家名称2
- **Reference5**: 玩家名称3
- **Reference6**: 玩家名称4

- **Reference1**: gameend（游戏结束时）
- **Reference2**: 玩家名称1（字节值１）分数
- **Reference3**: 玩家名称2（字节值１）分数
- **Reference4**: 玩家名称3（字节值１）分数
- **Reference5**: 玩家名称4（字节值１）分数

- **Reference1**: kyokustart（一局开始时）
- **Reference2**: 场风（东|南|西|北）
- **Reference3**: 庄家玩家名称
- **Reference4**: 本场数（例如 1）
- **Reference5**: 供托（例如 1000）

- **Reference1**: kyokuend（一局结束时）

- **Reference1**: point（通知玩家分数）
- **Reference2**: 玩家名称
- **Reference3**: (=|+|-) =表示指定分数，+-表示增减
- **Reference4**: 分数

- **Reference1**: haipai（发初始手牌时）
- **Reference2**: 玩家名称
- **Reference3**: 初始手牌（例如 1m2m3m4p5p6p7s8s9s1z5z6z7z）

- **Reference1**: dora（发送宝牌指示牌时）
- **Reference2**: 牌（例如 7z）

- **Reference1**: open（公开手牌时，例如吃、碰、杠等）
- **Reference2**: 玩家名称
- **Reference3**: 牌（例如 1p2p3p）

- **Reference1**: tsumo（自摸时）
- **Reference2**: 玩家名称（自己）
- **Reference3**: 剩余牌数
- **Reference4**: 牌（例如 7z）

- **Reference1**: sutehai（打出弃牌时）
- **Reference2**: 玩家名称（自己）
- **Reference3**: 牌（例如 7z）

- **Reference1**: say（发声时）
- **Reference2**: 玩家名称
- **Reference3**: 发声内容（chi|pon|kan|ron|tsumo|richi|tenpai|noten）

- **Reference1**: agari（和牌时）
- **Reference2**: 玩家名称
- **Reference3**: 符
- **Reference4**: 役种,番数
- **Reference5**: 后续内容与 Reference4 相同

- **Reference1**: ryukyoku（流局时）

以下命令需要回复。如果请求方是 GHOST，也可以使用`\![raiseother]`等方式回复；但如果请求方是通过 SSTP 通知的外部应用，则必须使用 X-SSTP-PassThru-\*标头回复。

使用`\![raiseother]`回复时，返回 OnMahjongResponse 事件。使用 SHIORI 响应标头时，设置 X-SSTP-PassThru-ID: OnMahjongResponse。

如果将请求对象设置为空字符串，则视为委托服务器处理。

- **Reference1**: hello（确认连接）

- **Reference1**: sutehai?（询问弃牌）

- **Reference1**: naku?（询问是否鸣牌，同时发送客户端可执行的命令）
- **Reference2**: (ron|kan|pon|chi)
- **Reference3**: 后续内容与 Reference2 相同

- **Reference1**: tenpai?（询问是否宣告听牌）
