# Describe

**カテゴリ:** internal_system

Returns how to call a function in a built-in module (number of positional arguments, accepted options, and choices selected by name).<br />
Functions in built-in modules fail with 400 (`invalid parameter` or `unsupported algorithm`) if passed an unknown option or algorithm name. This is what happens when you use an option or algorithm added in a newer SSP with an older SSP. Checking in advance with this function lets you determine whether it is available without calling it. [ListFunctions](internal_system.ListFunctions.md) only tells you whether the function exists.

- **Argument1**: Module name (case-insensitive)
- **Argument2**: Function name (case-insensitive)

A name that is not a built-in module (including compatibility modules) results in 400 (`unknown module`); a function name that does not exist in that module results in 400 (`unknown function`). If either is missing, the result is 400 (`invalid parameter`).

The results are as follows.

- **Result**: Function name (canonical spelling).
- **Value0**: Maximum number of positional arguments. This is the number of arguments from `Argument1` onward that can appear before any options. For functions with a variable number of positional arguments (such as `MediaInfo` in `internal_file`), this is the upper limit.
- **Value1**: Number of required positional arguments.
- **Value2**: `1` if the number of positional arguments is variable, or `0` if it is fixed. For functions with a variable number of positional arguments, values from the second positional argument onward, starting with the first value that begins with `--`, are read as options ([common conventions](../internal.md#関数と引数)).
- **Value3**: Comma-separated names of the accepted options, without the `--` prefix. This includes `async`, which is accepted by every function. Options in the form `--データ名-in=` (such as `data-in` and `key-in`) are listed as-is.
- **Value4 and later**: If any arguments or options must be selected from a fixed set of choices, each has one value. The format is `name=choice|choice|…`; the name is `Argument1` and so on for a positional argument (using the same number as the request's `ArgumentN`), or an option such as `--digest`. Choices use the same spelling as in each function's description. Functions without a fixed set of choices have no Value4 or later.

Names in forms such as `--out=` and `--data-in=` ([common conventions](../internal.md#バイト列の入力の形式)), and the format names for [Format](../internal_time/internal_time.Format.md), are not included as choices.

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

From this result, you can determine whether `x25519` is available by splitting `Value4` at `=` and `|` and checking whether `x25519` is present.

**対応:** SSP 2.9.27
