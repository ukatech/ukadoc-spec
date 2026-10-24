# メソッド：GIVE

*\[旧仕様\]* ゴーストに各種データを与え、処理したり反応させたりするためのメソッドです。<br />
相当昔の仕様であり、現在これを使用する意味はありません。NOTIFYやCOMMUNICATEを使用してください。

## requestサンプル

```
GIVE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Document: まず水や。それから粉やな。
```

```
GIVE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Song: 佐世保の時雨
```

## request固有ヘッダ

- **Document**: 文書（汎用的な文字列）<br />
  SHIORI/3.0ではユーザーコミュニケートと同じ扱いとなり、OnCommunicateイベントが発生する。
- **Song**: 歌の名前。<br />
  SHIORI/3.0ではOnMusicPlayイベントが発生し、Reference0がSongヘッダに指定された文字列となる。
