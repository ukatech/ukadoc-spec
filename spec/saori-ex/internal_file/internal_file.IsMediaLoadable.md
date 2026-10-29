# IsMediaLoadable

**カテゴリ:** internal_file

音声・動画ファイルを、SSPが扱えるかを調べる。ファイルをロードせずに、拡張子から判定する。<br />
判定は、音声・動画ファイルをSSPにドラッグ＆ドロップしたときに内蔵のメディアプレーヤで開けるかの判定と同じ部品（OSのDirectShow / Media Foundationが再生し得る拡張子の集合）を使う。ファイルの中身は調べないので、`read`でも実際に再生できるとは限らない。

- **Argument1**: ファイルのパス。相対パスはゴーストのフォルダ（ghost/master）が基準。区切りは`/`も`\`も書ける。ゴーストなしの呼び出しで相対パスを渡すと400（`ghost required`）。ファイルが無い（フォルダを含む）ときは400（`file not found`）。URLは受け付けない。

応答の`Result`は取り扱いのレベルで、次のどれか。

- **none**: 読めない。音声・動画ではない（画像を含む）、または未対応の形式。
- **read**: 読み取りのみ。再生できる見込みのある形式。
- **embed**: ゴーストに組み込める。**現状は返らない。**
- **write**: 書き込みも可能。**現状は返らない。**

[IsImageLoadable](internal_file.IsImageLoadable.md)と同じ4段階の語を使う。後のレベルは前のレベルを含む。`embed`・`write`は今後、返すようになることがあるので、`read`と等しいかではなく、`none`でないかで判断するのが無難。

## 記述例

```
Argument0: IsMediaLoadable
Argument1: sound/bgm01.mp3

→ 200
　Result: read
```

**対応:** SSP 2.9.27
