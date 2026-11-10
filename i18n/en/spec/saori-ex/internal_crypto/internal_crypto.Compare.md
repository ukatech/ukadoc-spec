# Compare

**カテゴリ:** internal_crypto

Compare two byte sequences in the same amount of time regardless of their contents. Returns `1` if they are equal and `0` if they differ (also returns `0` if their lengths differ).<br />
Use this when you do not want the contents to be inferred from the comparison time, such as when checking a Webhook signature. When comparing hexadecimal signatures, use `--a-in=hex --b-in=hex` to ignore differences in letter case.

- **Argument1**: a (default format is `text`)
- **Argument2**: b (default format is `text`)
- **Options**: `--a-in=` / `--b-in=` / `--charset=`

**対応:** SSP 2.9.13
