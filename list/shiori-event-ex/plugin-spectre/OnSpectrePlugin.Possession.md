# OnSpectrePlugin.Possession

**カテゴリ:** プラグイン「Spectre」

Spectreがこのゴーストを通じて会話を表示してから15秒後に発生する。<br />
このイベントはプラグイン自体から直接発生するのではなく、会話の末尾に置いたtimerraiseタグを通じてゴースト側から呼び出される点に注意。

- **Reference0**: 現在の会話プールに基づく、キャラクターの現在の「ムード」。次のいずれかの値になる。
  - dissociated …… ひどく悲しく、支離滅裂なムード
  - miserable …… 悲しい、または怒りのムード
  - cheerful …… 幸せな、またはリラックスしたムード
- **Reference1**: 再生されたスクリプトが「spooky text」スクリプトだったかどうか。「spooky text」スクリプトとは、不安感を呼び起こす特殊な文字効果を持つスクリプトなどのこと。該当すれば1、しなければ0。<br />
  「spooky text」スクリプトは、現在のところReference0が「dissociated」の場面でのみ再生される。
