# OnMahjongResponse

**カテゴリ:** 麻將通訊事件

回覆 OnMahjong 事件。請參閱下述[※用戶端指令](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)。

- **Reference0**: 版本（UKAJONG/0.2）
- **Reference1**: [※用戶端指令](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)
- **Reference\***: 依據[※用戶端指令](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)而定的附加資訊

## UKAJONG/0.2 的用戶端指令及其附加資訊

- **Reference1**: hello（回覆確認連線）
- **Reference2**: ump=(UMP 版本)※並非嚴格遵循 UMP，因此沒有特別檢查。ump=? 即可
- **Reference3**: name=(玩家名稱)※請指定 sakura.name。

- **Reference1**: sutehai?（回覆打出的牌）
- **Reference2**: (sutehai|ankan|kakan|richi|tsumo)
- **Reference3**: 選取的牌（tsumo 時可留空）

- **Reference1**: naku?（回覆是否鳴牌）
- **Reference2**: (no|ron|kan|pon|chi)
- **Reference3**: 選取的牌1（chi 時需要。對 2m 指定 1m 和 3m，或 3m 和 4m 等；此為其中第 1 張）
- **Reference4**: 選取的牌2（上述第 2 張）

- **Reference1**: tenpai?（回覆是否宣告聽牌）
- **Reference2**: (yes|no)
