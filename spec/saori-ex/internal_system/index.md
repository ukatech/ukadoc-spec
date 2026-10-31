# internal_system

内蔵モジュールの一覧と、関数の呼び方。どの関数が使えるか、どんなオプションやアルゴリズム名が使えるかを、スクリプトから確かめるのに使う。<br />
一覧に出るのは名前が`internal_`で始まるモジュールだけである（[互換モジュール](../compat.md)は出ない）。<br />
`ListModules` / `ListFunctions`の結果は`Result`にカンマ区切りで、`Value0`以降に1つずつ入る。並び順に意味はない。

## 一覧

- [ListModules](internal_system.ListModules.md)
- [ListFunctions](internal_system.ListFunctions.md)
- [Describe](internal_system.Describe.md)
