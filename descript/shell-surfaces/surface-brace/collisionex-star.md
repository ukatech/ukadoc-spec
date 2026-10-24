# collisionex\*,ID,タイプ,座標1,座標2...

**カテゴリ:** surfaceブレス

不定形当たり判定。<br />
\*の部分（collisionID）は、同じsurface内で重複しない通し番号。<br />
タイプは以下の通り。

- **rect**: 長方形。座標は始点XYと終点XYの4つ。<br />
  例：collisionex0,Head,rect,100,100,200,300
- **ellipse**: 楕円。座標は楕円を囲む長方形、始点XYと終点XYの4つ。<br />
  例：collisionex0,Head,ellipse,100,100,200,300
- **circle**: 真円。中心点のXYの値、半径の順で記述する。<br />
  例：collisionex0,Head,circle,100,200,20
- **polygon**: 多角形。座標は各頂点、交差可。<br />
  例：collisionex0,Head,polygon,100,100,200,300,50,200
- **region**: \[SSP 2.5.19～\]指定した画像ファイルの指定色の領域を当たり判定として扱う。<br />
  大量に(100～)使用すると全体的に動作が重くなるので注意。<br />
  「領域反転」をtrueにすると「指定色でない領域」の意味になる。省略可能。<br />
  指定フォーマット：ファイル名,R,G,B,領域反転(falseかtrue)<br />
  例1: collisionex0,Head,region,atari.png,255,0,0<br />
  例2: collisionex1,Head,region,atari.png,0,255,0,true

**既定値:** 挙動なし

**対応:** SSP
