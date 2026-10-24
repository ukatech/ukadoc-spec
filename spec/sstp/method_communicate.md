# メソッド：COMMUNICATE

COMMUNICATEメソッドで、ゴーストに外部から任意の文字列を与えて、反応させることができます。<br />
基本的にゴースト内部でのコミュニケートボックスを使った反応と同じになりますが、SSTPなのでゴースト側で受理されない場合があります。

## 単純なCOMMUNICATE(COMMUNICATE/1.1)

```
COMMUNICATE SSTP/1.1
Charset: UTF-8
Sender: User
Sentence: おはよう。
```

コミュニケートはSSTPサーバ同士（≒ゴースト同士）で送受信を繰り返すことができます。<br />
SHIORI/3.0のレスポンスReference0での送信の場合は、SSTP送信タイミングはSakuraScriptを再生し終わった時となります。<br />
これを用いて、同時起動しているゴースト同士が会話しているような処理を組むことが可能となります。

## ゴースト間コミュニケート(COMMUNICATE/1.2)

```
COMMUNICATE SSTP/1.2
Charset: UTF-8
Sender: Emily
HWnd: 28236
Sentence: \0\s[5]ちゃっらーん！エミリでーす！\nボクのお腹にはまだ若干の余裕が…？\1\s[11]そんなこと言ってたらまた太るよ？
Surface: 5,11
Reference0: 芋ちょうだい
Reference1: たくさんちょうだい
Reference2: 今すぐちょうだい
```

## request固有ヘッダ

- **Reference\***: コミュニケートの拡張情報。SHIORI/3.0ではReference2以降に格納される。SSTP Reference0 = SHIORI Reference2。
- **Surface**: 送信元ゴーストのコミュニケート送信時点（≒スクリプト実行終了時点）での`\0`と`\1`のサーフィス番号。<br />
  OnCommunicateイベントでSurfaceヘッダとして渡される。
- **Option**: *\[旧仕様\]*substituteを指定すると、Sentenceの内容を`\1`が喋る。 ※SSP未実装
