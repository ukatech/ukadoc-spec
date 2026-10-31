# Describe

**カテゴリ:** internal_system

内蔵モジュールの関数の呼び方（位置引数の数・受け付けるオプション・名前で選ぶ候補）を返す。<br />
内蔵モジュールの関数は、知らないオプションや、知らないアルゴリズム名を渡されると、400（`invalid parameter`や`unsupported algorithm`）で失敗する。新しいSSPで増えたオプションやアルゴリズムを、古いSSPで使うとこうなる。この関数で先に調べておけば、使えるかどうかを、呼ばずに判断できる。[ListFunctions](internal_system.ListFunctions.md)が答えるのは、関数があるかどうかだけである。

- **Argument1**: モジュール名（大文字小文字は区別しない）
- **Argument2**: 関数名（大文字小文字は区別しない）

内蔵モジュールでない名前（互換モジュールを含む）は400（`unknown module`）、そのモジュールに無い関数名は400（`unknown function`）。どちらかが足りなければ400（`invalid parameter`）。

結果は次のとおり。

- **Result**: 関数名（正規の綴り）。
- **Value0**: 位置引数の最大数。`Argument1`以降のうち、オプションより前に置ける数である。位置引数が可変個の関数（`internal_file`の`MediaInfo`など）では、その上限。
- **Value1**: 必須の位置引数の数。
- **Value2**: 位置引数が可変個なら`1`、決まった数なら`0`。可変個の関数は、2番目以降の位置で最初に`--`で始まる値から後ろを、オプションとして読む（[共通規約](../internal.md#関数と引数)）。
- **Value3**: 受け付けるオプションの名前を、カンマ区切りで並べたもの。`--`は付けない。どの関数も受け付ける`async`を含む。`--データ名-in=`の形のオプション（`data-in`、`key-in`など）も、そのまま並ぶ。
- **Value4以降**: 決まった候補から選ぶ引数とオプションが、あれば1つずつ。`名前=候補|候補|…`の形で、名前は位置引数なら`Argument1`など（要求の`ArgumentN`と同じ番号）、オプションなら`--digest`など。候補は、各関数の説明に書かれている名前と同じ綴りである。選べる名前が決まっていない関数には、無い。

`--out=`や`--data-in=`などの形式の名前（[共通規約](../internal.md#バイト列の入力の形式)）と、[Format](../internal_time/internal_time.Format.md)の書式の名前は、候補に含まない。

## 記述例

```
Argument0: Describe
Argument1: internal_crypto
Argument2: KeyAgreement

→ Result: KeyAgreement
→ Value0: 3
→ Value1: 3
→ Value2: 0
→ Value3: key-in,peer-in,out,async
→ Value4: Argument1=secp256k1|x25519|p256
```

この結果から、`x25519`が使えるかどうかは、`Value4`を`=`と`|`で分けて、`x25519`があるかどうかで判断できる。

**対応:** SSP 2.9.27
