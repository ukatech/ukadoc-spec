# `\![open,textareabox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** 開啟命令

開啟多行輸入框（textareabox）。<br />
確定時（按下 OK 按鈕或 Ctrl+Enter）會觸發 SHIORI 事件[OnTextAreaInput](../../shiori-event/inputbox/OnTextAreaInput.md)。Enter 鍵會換行。<br />
超過顯示時間（逾時）或按下關閉按鈕關閉時，會觸發[OnTextAreaInputCancel](../../shiori-event/inputbox/OnTextAreaInputCancel.md)。

<br />
輸入內容中的換行會以位元組值 1 的字元（`\1`）分隔並傳遞。文字（初始顯示的內容）也同樣以 `\1` 表示換行。<br />
ID 的處理方式（若以「On」開頭，則會觸發名稱相同的事件）與[InputBox 的 ID](bang-close-textareabox-ID.note-2.md)相同。<br />
顯示時間、文字的指定方式及[※選項](bang-close-textareabox-ID.note.md)皆與[inputbox](bang-open-inputbox-ID.md)相同，但有以下差異。<br />
・--limit= 會將換行計為 1 個字元。<br />
・--placeholder=（欄位空白時以淡色顯示的提示文字）也以 `\1` 表示換行。<br />
・無法使用輸入補完功能（[inputbox.autocomplete](../../shiori-event/inputbox/inputbox.autocomplete.md)）。<br />
・省略 --balloon= 時會使用 balloonc5。若 balloon 中沒有 balloonc5，則會以交談中角色目前使用的 balloon 圖片為背景，並將 validrect 範圍設為輸入欄位（文字字型、大小與顏色也會沿用 balloon 本文的設定）。即使是直書 balloon，輸入欄位仍會以橫書方式顯示。

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
