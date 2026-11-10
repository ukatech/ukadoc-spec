# OnSpectrePlugin.Surface

**カテゴリ:** プラグイン「Spectre」

Spectreの会話中に、現在話しかけられているゴーストへサーフェスの切り替えを求めるときに発生する。<br />
このイベントはプラグイン自体から直接発生するのではなく、会話中の埋め込みタグを通じてゴースト側から呼び出される点に注意。<br />
含まれる表情は[推奨表情](../../../descript/shell-surfaces/surface-brace/caption_standarddef.md)に、英語圏のゴーストでよく使われる表情を少し加えたもの。<br />
*ゴーストのシェルで正確に表現できない表情は無視し、応答を返さないこと。* プラグインがこの情報を独自の目的に使うため。

- **Reference0**: 求められる表情。次のいずれかの値になる。

  - normal …… 通常はsurface0
  - embarrassed …… 通常はsurface1
  - surprised …… 通常はsurface2
  - anxious …… 通常はsurface3
  - discouraged …… 通常はsurface4
  - smile …… 通常はsurface5
  - relieved …… 通常はsurface6。「contented」とも呼ばれる
  - angry …… 通常はsurface7
  - sweat …… 通常はsurface8。「sweat smile」「cold smile」とも呼ばれる
  - indignant …… 通常はsurface9。「embarrassed anger」とも呼ばれる
  - thinking …… 一部の英語圏のゴーストでよく使われる。「thoughtful」「confused」とも呼ばれる
  - unamused …… 一部の英語圏のゴーストでよく使われる。「bored」とも呼ばれる
