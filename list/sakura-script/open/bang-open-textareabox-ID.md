# `\![open,textareabox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** オープンコマンド

複数行の入力ボックス(textareabox)を開く。<br />
決定時(OKボタンを押すか、Ctrl+Enter)にSHIORIイベント[OnTextAreaInput](../../shiori-event/inputbox/OnTextAreaInput.md)が発生する。Enterキーは改行になる。<br />
表示時間を過ぎた(タイムアウトした)場合と、閉じるボタンを押して閉じた場合は、[OnTextAreaInputCancel](../../shiori-event/inputbox/OnTextAreaInputCancel.md)が発生する。

<br />
入力内容の改行は、バイト値1の文字(`\1`)で区切って渡される。テキスト(初期表示する内容)も同じく`\1`で改行を表す。<br />
IDの扱い(「On」で始まる場合はID名のイベントが発生する)は[InputBoxのID](notes_inputbox-id.md)と同じ。<br />
表示時間・テキストの指定と[※オプション](notes_inputbox-option.md)は[inputbox](bang-open-inputbox-ID.md)と同じ。ただし次の点が異なる。<br />
・--limit=は改行を1文字として数える。<br />
・--placeholder=(空欄のときに薄く表示する案内文)も`\1`で改行を表す。<br />
・入力補完([inputbox.autocomplete](../../shiori-event/inputbox/inputbox.autocomplete.md))は使えない。<br />
・--balloon=を省略した場合はballoonc5を使う。balloonc5が無いバルーンでは、話しているキャラクターの現在のバルーン画像を背景にし、validrectの範囲を入力欄にする(文字の書体・大きさ・色もバルーン本文のもの)。縦書きのバルーンでも入力欄は横書きになる。

**対応:** SSP 2.9.10

## 記述例

```sakurascript
\![open,textareabox,感想,--timeout=300000] 複数行の入力ボックスを開く。5分でタイムアウトする。
```

```sakurascript
\![open,textareabox,OnDiaryInput,--limit=400] 決定時にOnDiaryInputが発生する。改行込みで400文字まで。
```

```sakurascript
\![open,textareabox,OnDiaryInput,--placeholder=今日の出来事(Ctrl+Enterで決定)] 空欄に案内文を薄く表示する。
```
