# system.cpu.(キー)

**カテゴリ:** プロパティシステム

起動中の環境のCPUの情報。(キー)に入る文字列は以下の通り。

- **load**: 負荷率（単位％、整数、適宜分単位程度で移動平均を計算して均されているもの）
- **num**: OSが認識している全コア数
- **vendor**: ベンダー名。例：GenuineIntel
- **name**: 名前。例：11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- **clock**: クロック周波数
- **features**: 解釈可能な拡張命令のリスト(半角空白区切り)。例：MMX SSE SSE2 SSE3

**対応:** SSP 2.6.26
