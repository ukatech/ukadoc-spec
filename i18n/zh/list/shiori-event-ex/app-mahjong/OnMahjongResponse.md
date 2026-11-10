# OnMahjongResponse

**カテゴリ:** 麻将通信事件

对 OnMahjong 事件的回复。参见下文的[※客户端命令](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)。

- **Reference0**: 版本（UKAJONG/0.2）
- **Reference1**: [※客户端命令](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)
- **Reference\***: 根据[※客户端命令](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)提供的附加信息

## UKAJONG/0.2中的客户端命令及其附加信息

- **Reference1**: hello（回复连接确认）
- **Reference2**: ump=(UMP 版本)※并未严格遵循 UMP，因此实际上不会特别检查。ump=? 即可
- **Reference3**: name=(玩家名称)※请指定 sakura.name。

- **Reference1**: sutehai?（回复弃牌）
- **Reference2**: (sutehai|ankan|kakan|richi|tsumo)
- **Reference3**: 选择的牌（tsumo 时可以留空）

- **Reference1**: naku?（回复是否鸣牌）
- **Reference2**: (no|ron|kan|pon|chi)
- **Reference3**: 选择的牌1（chi 时必需。对于 2m，指定 1m 和 3m 或 3m 和 4m 等；这是其中的第 1 张）
- **Reference4**: 选择的牌2（上述第 2 张）

- **Reference1**: tenpai?（回复是否宣告听牌）
- **Reference2**: (yes|no)
