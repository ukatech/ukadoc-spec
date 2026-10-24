# OnPoker

**カテゴリ:** ゴースト「卓上誘技」

応答が必要なイベント。応答方法はraiseotherかnotifyotherを使う。

- **Reference0**: プロトコルバージョン(POKER/1.0)
- **Reference1**: サーバーゴースト名
- **Reference2**: サーバーのイベント名

## POKER/1.0におけるReference3以降の追加情報

- **Reference3**: hello（参加申請をする。断られることもある。）

- **Reference3**: action（Reference4以降に使用可能なアクションが入っている。）
- **Reference\***: 使用可能なアクションはbet,raise,allin,check,call,foldの6つの内のいくつか。<br />
  返答しない場合は自動的にfoldになるので注意。<br />
  bet/raiseする場合はレイズ額も送る必要がある。
