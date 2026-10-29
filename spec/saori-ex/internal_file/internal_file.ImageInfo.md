# ImageInfo

**カテゴリ:** internal_file

画像ファイルの大きさを、**ファイルをロードせずに**（ヘッダだけを読んで）取得する。サーフェスなどを作らなくても、パスだけで読める。<br />
**環境によっては取得できない場合がある**。SSPはまずOSのプロパティハンドラ（エクスプローラーのファイルの詳細に出るのと同じ仕組み）で読み、取れなければ、SSP自身がファイルのヘッダだけを読んで取る（画像を展開しない）。ヘッダから取れるのは、PNG（APNG）/ JPEG / GIF / BMP / TIFF / WebP / ICO・CUR（最大のエントリ）/ PSD / XCF / PSP（バージョン4.0以降）/ QOI / PCX / TGA / PBM・PGM・PPM・PAM・PFM / XBM / XPM / MAG / PI。ORA / KRA / CLIP（中身を展開しないと分からない形式）は、OSのハンドラがなければ空になる。取れなかったことはエラーにならない。<br />
ヘッダから読むときの寸法は、TIFFは最初のページ、GIFは論理スクリーン、ICO・CURは最大のエントリ。EXIFの向き（回転）は反映しない。<br />
同期で呼ぶと、読み出しの間ゴーストが止まる点に注意。読み出しはファイルの置き場所（ネットワークドライブなど）によっては時間がかかるので、[`--async`](../async.md)の利用も検討する。

音声・動画のタグや長さは[MediaInfo](internal_file.MediaInfo.md)で読む。

- **Argument1**: ファイルのパス。相対パスはゴーストのフォルダ（ghost/master）が基準。区切りは`/`も`\`も書ける。ゴーストなしの呼び出しで相対パスを渡すと400（`ghost required`）。ファイルが無い（フォルダを含む）ときは400（`file not found`）。URLは受け付けない。
- **Argument2以降**: 欲しい値のキー。1個以上必須（1個もなければ400 `invalid parameter`）で、11個まで。キーは大文字小文字を区別しない。

キーは次のとおり。値は10進の整数の文字列。

- **width / height**: 画像の画素数（px）。

応答の`Result`は`image`（画像と判別できたとき）か空。画像と判別できなければ（音声・動画のファイルを含む）、`Value`はすべて空になる。<br />
`Value0`以降は`Argument2`以降に並べたキーと同じ順に対応する。取れなかった値・知らないキーは**空文字**（エラーにはならない。実装独自のキーは返さない）。読めない・未対応の形式でも、400にはならず、`Result`も`Value`もすべて空の200で返る。<br />
応答の文字コードは要求の`Charset`に従う。

## 記述例

```
Argument0: ImageInfo
Argument1: image/bg01.png
Argument2: width
Argument3: height

→ 200
　Result: image
　Value0: 640
　Value1: 480
```

**対応:** SSP 2.9.27
