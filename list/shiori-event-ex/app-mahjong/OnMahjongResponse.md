# OnMahjongResponse

**カテゴリ:** 麻雀通信イベント

OnMahjongイベントに対する返信。後述の[※クライアントコマンド](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)参照。

- **Reference0**: バージョン（UKAJONG/0.2）
- **Reference1**: [※クライアントコマンド](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)
- **Reference\***: [※クライアントコマンド](OnMahjongResponse.md#ukajong02におけるクライアントコマンドとその追加情報)に応じた追加情報

## UKAJONG/0.2におけるクライアントコマンドとその追加情報

- **Reference1**: hello（接続確認の返信）
- **Reference2**: ump=(UMPバージョン)※厳密にUMPに準拠しているわけではないので特に見てないです。ump=?でOK
- **Reference3**: name=(プレイヤー名)※sakura.nameを指定してください。

- **Reference1**: sutehai?（捨牌の返信）
- **Reference2**: (sutehai|ankan|kakan|richi|tsumo)
- **Reference3**: 選択された牌(tsumoの時は空でよい)

- **Reference1**: naku?（牌を鳴くかの返信）
- **Reference2**: (no|ron|kan|pon|chi)
- **Reference3**: 選択された牌1(chiの時に必要。2mに対し1mと3mまたは3mと4mのように指定する。そのうちの1枚目)
- **Reference4**: 選択された牌2(上記の2枚目)

- **Reference1**: tenpai?（テンパイを宣言するかの返信）
- **Reference2**: (yes|no)
