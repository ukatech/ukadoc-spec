# OnMahjongResponse

**カテゴリ:** Mahjong communication event

Reply to the OnMahjong event. See [※Client commands](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報) below.

- **Reference0**: Version (UKAJONG/0.2)
- **Reference1**: [※Client commands](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)
- **Reference\***: Additional information corresponding to [※Client commands](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)

## Client commands and their additional information in UKAJONG/0.2

- **Reference1**: hello (connection confirmation reply)
- **Reference2**: ump=(UMP version)※It does not strictly conform to UMP, so I do not check it in particular. ump=? is OK
- **Reference3**: name=(player name)※Specify sakura.name.

- **Reference1**: sutehai? (discard reply)
- **Reference2**: (sutehai|ankan|kakan|richi|tsumo)
- **Reference3**: Selected tile (can be empty for tsumo)

- **Reference1**: naku? (reply on whether to call a tile)
- **Reference2**: (no|ron|kan|pon|chi)
- **Reference3**: Selected tile 1 (required for chi. Specify, for example, 1m and 3m or 3m and 4m for 2m. This is the first of the two tiles)
- **Reference4**: Selected tile 2 (the second tile described above)

- **Reference1**: tenpai? (reply on whether to declare tenpai)
- **Reference2**: (yes|no)
