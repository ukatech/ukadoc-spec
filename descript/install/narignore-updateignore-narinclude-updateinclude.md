# .narignore / .updateignore / .narinclude / .updateinclude

## .narignore / .updateignore

developer_options.txtの記法より柔軟性をもたせるため、.gitignoreの記法をそのまま使えるようにしたものが、.narignore/.updateignoreである。

記法は [.gitignoreのマニュアル](https://git-scm.com/docs/gitignore/ja) を確認するか、LLM(テキスト生成AI)にやりたいことを質問して生成してもらうとよい。

ただし.gitignoreと異なり、サブディレクトリに置いても機能しない。ゴーストのルートディレクトリ直下に置いた場合のみ有効である。

伺か限定の特殊機能として、include:指定がある。たとえば<br />
include:.narignore<br />
と書くと、.narignoreファイルの内容をまるごとこの行の位置に挿入したかのように処理する。

include:に指定する相対パスは、ゴーストのルートディレクトリを基準とするのではなく、その行が書かれているファイル自身があるディレクトリを基準に解決される。読み込んだ先のファイルの中でさらにinclude:を書くこともでき、その場合の基準ディレクトリは「今読み込んだファイルのあるディレクトリ」へとその都度更新される(親から子、子から孫へと基準が移動していく)。

この再帰読み込みには上限があり、最大3階層まで辿れる。それを超える深さのinclude:は読み込みを拒否される。パスの区切り文字は / と \\ のどちらで書いてもよい。

例えばゴーストのルートディレクトリ直下の.narincludeにinclude:sub/extra.txtと書くと、sub/extra.txtを読み込む。そのextra.txt内でさらにinclude:foo.txtと書いた場合は、ゴーストのルートディレクトリではなく、extra.txtが置かれているsub/ディレクトリを基準に、sub/foo.txtを読み込む。

## .narinclude / .updateinclude

.narignore/.updateignoreのホワイトリスト版。ここに書いたものだけが更新ファイル/NARに格納される。<br />
サブディレクトリの扱いがgitignoreと異なり、たとえばshell/masterとだけ書いてshell/は書かなくても、親ディレクトリをきちんと含んで処理する。

また.narignore/.updateignoreと同様、.gitignoreと異なりサブディレクトリに置いても機能しない。ゴーストのルートディレクトリ直下に置いた場合のみ有効である。
