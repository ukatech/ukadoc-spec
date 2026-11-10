# `\b[ID番号]`

**カテゴリ:** Balloon, text command

Change the balloon for the current scope to the balloon with the specified ID number.<br />
Odd numbers are reserved for balloons displayed to the right of the character, so only 0 or even IDs can be used.<br />
`\b[-1]` hides the balloon.

As of SSP 2.6.34, writing `\b[ID1,--fallback=ID2,--fallback=ID3]` makes the balloon use ID2 if ID1 does not exist, and ID3 if ID2 does not exist.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\b[2]本体側のトークをバルーン2番に表示する。バルーンによって実装状況は異なり、バルーン2番が存在しない場合もある。SSP同梱バルーン「SSPデフォルト+」では、本体側バルーン2番は表示文字数の多い大きなバルーンとなるが、サイズの決まりはないため、これを使う際は推奨バルーンを指定する・専用バルーンを同梱するなどが必要。
```
