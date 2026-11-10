# Describe

**カテゴリ:** internal_system

返回调用内置模块函数的方法（位置参数的数量、接受的选项、按名称选择的候选项）。<br />
内置模块函数收到未知选项或未知算法名称时，会以 400（`invalid parameter`或`unsupported algorithm`）失败。在较旧的 SSP 中使用新增选项或算法时，就会出现这种情况。事先通过此函数查询，即可在不调用函数的情况下判断是否可用。[ListFunctions](internal_system.ListFunctions.md)只会回答函数是否存在。

- **Argument1**: 模块名（不区分大小写）
- **Argument2**: 函数名（不区分大小写）

名称不是内置模块的名称（包括兼容模块）时返回 400（`unknown module`）；函数名不属于该模块时返回 400（`unknown function`）。任一参数缺失时返回 400（`invalid parameter`）。

结果如下。

- **Result**: 函数名（规范拼写）。
- **Value0**: 位置参数的最大数量。即从`Argument1`开始、可置于选项之前的参数数量。位置参数数量可变的函数（例如`internal_file`的`MediaInfo`）中，此值为上限。
- **Value1**: 必需的位置参数数量。
- **Value2**: 位置参数数量可变时为`1`，固定时为`0`。对于可变参数函数，从第二个位置参数开始，遇到第一个以`--`开头的值后，其后的内容会作为选项读取（[通用规则](../internal.md#関数と引数)）。
- **Value3**: 以逗号分隔列出的可接受选项名称。不加`--`。包括所有函数都接受的`async`。形如`--数据名-in=`的选项（例如`data-in`、`key-in`）也会原样列出。
- **Value4以降**: 如果参数或选项需要从固定候选项中选择，则每项对应一个值。格式为`名称=候选项|候选项|…`，名称为位置参数时是`Argument1`等（与请求中的`ArgumentN`编号相同），选项时是`--digest`等。候选项的拼写与各函数说明中列出的名称相同。对于可选名称不固定的函数，不会返回Value4及后续值。

形如`--out=`或`--data-in=`的名称（[通用规则](../internal.md#バイト列の入力の形式)）以及[Format](../internal_time/internal_time.Format.md)的格式名称不包含在候选项中。

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

根据此结果，可以通过用`=`和`|`拆分`Value4`，检查其中是否包含`x25519`，来判断`x25519`是否可用。

**対応:** SSP 2.9.27
