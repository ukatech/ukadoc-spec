# 補足

## サーフェスの位置情報

- **top**: 上部に貼り付き表示。
- **bottom**: 下部に貼り付き表示。
- **free**: 自由移動。

## バルーンの位置情報

- **none**: 自動調整、shellのY座標が画面中央より左なら右、右なら左に表示。
- **left**: 常に左に表示。
- **right**: 常に右に表示。

## メニュー画像の位置指定

寄せる方向のいずれか+繰り返し(タイリング)指定 という形式で指定する。<br />
例：lefttop<br />
例：leftbottom+repeat-x+repeat-y

- **lefttop**: \[background/foreground\]左上端に寄せる。
- **centertop**: \[background/foreground\]上端中央に寄せる。 \[SSP\]
- **righttop**: \[background/foreground\]右上端に寄せる。
- **leftbottom**: \[background/foreground\]左下端に寄せる。 \[SSP\]
- **centerbottom**: \[background/foreground\]下端中央に寄せる。 \[SSP\]
- **rightbottom**: \[background/foreground\]右下端に寄せる。 \[SSP\]

- **top**: \[sidebar\]上端に寄せる。
- **bottom**: \[sidebar\]下端に寄せる。

- **+repeat-x**: \[background/foreground\]横方向に繰り返して（タイリングして）画像を表示する。 \[SSP 2.5.39\]
- **+repeat-y**: \[background/foreground/sidebar\]縦方向に繰り返して（タイリングして）画像を表示する。 \[SSP 2.5.39\]

## アイコン枠色の明度調整について

sakura(kero/char\*).icon.frame.color.(r/g/b)で指定した色は、そのままバックログ(発言履歴)ウィンドウの枠色として使われるわけではない。<br />
ダークモード/ライトモードなど、ウィンドウのUI配色に合わせて明度を上げ下げする演算が加えられた上で表示される。<br />
そのため、指定はできるだけ混じりけのない原色に近い値が望ましい。(例：赤にしたい場合はRGB＝255,0,0など)
