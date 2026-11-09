# InputBoxのID

決定時、[OnUserInput](../../shiori-event/inputbox/OnUserInput.md)が発生するが、IDに「On」から始まる文字列を指定した場合、代わりにID名のイベントが発生する。<br />
OnUserInputではReference0に指定したID、Reference1に入力内容が入るが、ID名のイベントの場合、Reference0に入力内容が入る。<br />

例<br />
`\![open,inputbox,インプットテスト,10000,テスト入力]`で入力を決定した場合。

- 「OnUserInput」が発生
- Reference0は「インプットテスト」
- Reference1は入力内容
- Reference2は入力内容補足(sliderinputのみ、最小,最大。ほかは空欄)
- Reference3以降は--reference=で指定した追加情報

`\!`\[open,inputbox,*On*インプットテスト,10000,テスト入力\]で入力を決定した場合。

- 「Onインプットテスト」が発生
- Reference0は入力内容
- Reference1は入力内容補足(sliderinputのみ、最小,最大。ほかは空欄)
- Reference2以降は--reference=で指定した追加情報

IDにかかわらず、閉じるボタンを押した時とタイムアウト時は[OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)が発生する。
