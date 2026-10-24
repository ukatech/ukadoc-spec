# OnHandActivate

**カテゴリ:** ゴースト「The Hand」

The Handが他ゴーストを触りに行くまたは触り終わった際に発生。<br />
触っている間、Sender:The Handでゴーストに(OnMouseMove|OnMouseDoubleClick|OnMouseWheel)イベントを送る。

- **Reference0**: 通常触り開始：NormalStart<br />
  通常触り終了：NormalEnd<br />
  必殺技開始：SuperStart<br />
  必殺技途中：SuperContinue<br />
  必殺技終了：SuperEnd<br />
  必殺技途中でホーミング発動：SuperHoming
- **Reference1**: 当たり判定名。<br />
  停止された場合はescaped。<br />
  必殺技の場合は1～4。
- **Reference2**: 相手に起きるイベント。<br />
  通常時：(OnMouseMove|OnMouseDoubleClick|OnMouseWheel)<br />
  必殺技中：触った回数<br />
  必殺技終了時：(MAX触り回数|escaped|nocollision|attacked|deleted)
- **Reference3**: 触りに行く際のスクリプト。<br />
  必殺技中は当たり判定名。
- **Reference4**: シェル番号。
