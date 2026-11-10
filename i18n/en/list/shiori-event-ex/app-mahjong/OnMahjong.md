# OnMahjong

**カテゴリ:** Mahjong communication event

Notify at each point in the game. See [※Server commands](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報) below.

- **Reference0**: Version (UKAJONG/0.2)
- **Reference1**: [※Server commands](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)
- **Reference\***: Additional information corresponding to [※Server commands](OnMahjong.md#ukajong02におけるサーバコマンドとその追加情報)

## Server commands and their additional information in UKAJONG/0.2

- **Reference1**: gamestart (at the start of the game)
- **Reference2**: Seat (East|South|West|North)
- **Reference3**: Player name 1
- **Reference4**: Player name 2
- **Reference5**: Player name 3
- **Reference6**: Player name 4

- **Reference1**: gameend (at the end of the game)
- **Reference2**: Player name 1 (byte value １) score
- **Reference3**: Player name 2 (byte value １) score
- **Reference4**: Player name 3 (byte value １) score
- **Reference5**: Player name 4 (byte value １) score

- **Reference1**: kyokustart (at the start of a hand)
- **Reference2**: Prevailing wind (East|South|West|North)
- **Reference3**: Dealer player name
- **Reference4**: Honba (e.g. 1)
- **Reference5**: Riichi sticks (e.g. 1000)

- **Reference1**: kyokuend (at the end of a hand)

- **Reference1**: point (notify a player's score)
- **Reference2**: Player name
- **Reference3**: (=|+|-) = specifies the score directly; +- indicates an increase or decrease
- **Reference4**: Score

- **Reference1**: haipai (when dealing the starting hand)
- **Reference2**: Player name
- **Reference3**: Starting hand (e.g. 1m2m3m4p5p6p7s8s9s1z5z6z7z)

- **Reference1**: dora (when sending the dora indicator)
- **Reference2**: Tile (e.g. 7z)

- **Reference1**: open (when revealing a hand: chi, pon, kan, etc.)
- **Reference2**: Player name
- **Reference3**: Tiles (e.g. 1p2p3p)

- **Reference1**: tsumo (when drawing a tile)
- **Reference2**: Player name (self)
- **Reference3**: Remaining tiles
- **Reference4**: Tile (e.g. 7z)

- **Reference1**: sutehai (when discarding a tile)
- **Reference2**: Player name (self)
- **Reference3**: Tile (e.g. 7z)

- **Reference1**: say (when declaring an action)
- **Reference2**: Player name
- **Reference3**: Declaration (chi|pon|kan|ron|tsumo|richi|tenpai|noten)

- **Reference1**: agari (when winning)
- **Reference2**: Player name
- **Reference3**: Fu
- **Reference4**: Yaku, han count
- **Reference5**: From here on, same as Reference4

- **Reference1**: ryukyoku (at a draw)

The following commands require a reply. If the requester is a GHOST, you may reply with `\![raiseother]` or similar. However, if the requester is an external application and the notification was sent via SSTP, you must reply using the X-SSTP-PassThru-\* header.

When replying with `\![raiseother]`, return an OnMahjongResponse event. When using SHIORI response headers, set X-SSTP-PassThru-ID: OnMahjongResponse.

If an empty string is set for the requested item, the server is considered to have been delegated the response.

- **Reference1**: hello (connection check)

- **Reference1**: sutehai? (ask which tile to discard)

- **Reference1**: naku? (ask whether to call the tile; also sends commands the client can make)
- **Reference2**: (ron|kan|pon|chi)
- **Reference3**: From here on, same as Reference2

- **Reference1**: tenpai? (ask whether to declare tenpai)
