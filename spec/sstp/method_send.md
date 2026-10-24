# メソッド：SEND

SENDは、外部アプリケーションからゴーストにSakuraScriptやSHIORIイベントを送信し、再生させるためのメソッドである。<br />
SENDとNOTIFYは同一の処理として扱われる。両者に機能上の差異はない。以下の仕様はNOTIFYにもそのまま適用される。<br />
Scriptヘッダで直接SakuraScriptを指定する方法と、Eventヘッダでイベントを送信しSHIORI応答でスクリプトを得る方法の両方が使用できる。<br />
EventとScriptは併用可能で、Eventに対するSHIORI応答がスクリプトを返さなかった場合、Scriptヘッダのスクリプトにフォールバックする。<br />
対象ゴーストが未指定の場合、現在起動中のゴーストが対象となる。

## 基本的なスクリプト再生サンプル

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\w5\u\s[10]ご機嫌いかが？\e
```

## イベント送信サンプル

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnExternalEvent
Reference0: param1
Reference1: param2
```

## イベント＋フォールバックスクリプトサンプル

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnCustomEvent
Reference0: data
Script: \h\s[0]イベント未対応時のスクリプト\e
```

IfGhostヘッダを複数回記述し、対応するScriptヘッダと組み合わせることで、ゴーストごとに異なるスクリプトを指定できる。

## IfGhostによる振り分けサンプル

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\e
IfGhost: まゆら
Script: \h\s[0]まゆらさん、こんにちは。\e
IfGhost: 花ちゃん,妹
Script: \h\s[0]花ちゃんと妹さん、こんにちは。\e
```

## 割り込み抑制付きサンプル

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]割り込まないで追加。\e
Option: nobreak
```

## request固有ヘッダ

- **Sender**: 共通ヘッダだが、SEND/NOTIFYでの特殊値として`Sender: First`が使用できる。指定すると、初回起動時のゴースト（さくら）を対象にする。<br />
  SenderとUser-Agentの両方が未指定の場合、400 Bad Requestとなる。
- **Script**: 再生するSakuraScript。<br />
  Eventヘッダと併用した場合、Eventに対するSHIORI応答がスクリプトを返さなかった場合のフォールバックとして使用される。
- **Entry**: エントリデータ。SHIORIに渡される。
- **Event**: SHIORIイベント名。SHIORI/3.0ではIDヘッダの指定として取り扱われる。
- **Reference\***: イベントのReferenceヘッダ。SHIORIには文字コード変換等最低限の処理を行い、そのまま引き渡される。
- **IfGhost**: `\0`側名,`\1`側名 の書式でゴーストの名前を指定すると、直後に来たScriptヘッダを特定のゴースト専用として取り扱う。<br />
  IfGhostの直後ではないScriptヘッダが存在した場合は、IfGhostに該当しない場合のデフォルト処理用Scriptとなる。<br />
  省略した場合はどのゴーストに対しても同じScriptヘッダが再生される。<br />
  詳細な振り分けルールは後述の[IfGhostによるスクリプト振り分け](method_send.md#ifghostによるスクリプト振り分け)を参照。
- **Ghost**: ゴースト名（descript.txtのname）で対象ゴーストを指定する。
- **Option**: SSTPで実行されるSakuraScriptがどのように扱われるかのオプションを指定する。<br />
  カンマ区切りで複数指定可能。共通オプション(nodescript, notranslate等)に加え、SEND/NOTIFYで使用できるオプションフラグは以下の通り。<br />
  nobreak : 現在再生中のスクリプトを中断せずにキューイングする。<br />
  notify : SHIORIイベントをnotifyモード（応答不要）で送信する。また、スクリプトが[ValueNotifyヘッダで返された場合](../shiori3/request.md)と同じように強制的に扱われる。 \[SSP 2.6.76\]

## response固有ヘッダ

- **Script**: 実際に再生されたスクリプト。改行は除去される。
- **SHIORIカスタムヘッダ**: SHIORIの応答に含まれるヘッダが透過される。

## IfGhostによるスクリプト振り分け

IfGhostヘッダを複数回記述し、対応するScriptヘッダと組み合わせることで、ゴーストごとに異なるスクリプトを指定できる。<br />
IfGhostとScriptは出現順で対応付けられる。最初のIfGhostより前に記述されたScriptはデフォルトスクリプトとなる。

- **名前の照合**: IfGhostが「`\0`側名,`\1`側名」形式の場合、両方の名前が一致する必要がある。<br />
  IfGhostが「`\0`側名」のみの場合、`\0`側名の一致だけで選択される。<br />
  いずれにも一致しない場合、デフォルトスクリプトが使用される。ただし、ゴースト側が「未指定SSTP拒否」設定の場合はデフォルトスクリプトも使用されない。
- **デフォルトゴースト扱い**: 以下の名前はデフォルトゴースト（さくら）として扱われ、そのスクリプトはデフォルトスクリプトとしても機能する。<br />
  「さくら」「エミリ」「えみりぃ」
