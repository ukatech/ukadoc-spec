# `\b[ID番号]`

**カテゴリ:** balloon, text command

Change the balloon for the current scope to the balloon with the specified ID.<br />
Odd-numbered IDs are reserved for balloons displayed to the right of a character, so only ID 0 or even-numbered IDs can be used.<br />
Hide the balloon with `\b[-1]`.

Starting with SSP 2.6.34, writing `\b[ID1,--fallback=ID2,--fallback=ID3]` makes the command use ID2 if ID1 is unavailable, and ID3 if ID2 is also unavailable.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\b[2]本体側のトークをバルーン2番に表示する。バルーンによって実装状況は異なり、バルーン2番が存在しない場合もある。SSP同梱バルーン「SSPデフォルト+」では、本体側バルーン2番は表示文字数の多い大きなバルーンとなるが、サイズの決まりはないため、これを使う際は推奨バルーンを指定する・専用バルーンを同梱するなどが必要。
```
