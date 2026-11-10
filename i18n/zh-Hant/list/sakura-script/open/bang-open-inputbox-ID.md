# `\![open,inputbox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** 開啟指令

開啟 InputBox。<br />
按下確定（OK 按鈕）時會觸發 SHIORI 事件[OnUserInput](../../shiori-event/inputbox/OnUserInput.md)。<br />
超過顯示時間（逾時）或按下關閉按鈕關閉時，會觸發[OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)。<br />
若未回應 OnUserInputCancel，且因顯示時間到期而逾時，為確保相容性，會以「timeout」作為輸入文字觸發 OnUserInput。<br />
此外，過去在輸入期間會禁止所有其他操作，但 SSP 不會如此限制。

<br />
ID 會存入按下確定時觸發的 OnUserInput；若 ID 以「On」開頭，則會觸發同名事件。請參照[※ID](bang-close-textareabox-ID.note-2.md)。<br />
顯示時間以毫秒指定。省略或指定 0 以下的數值時，顯示時間不受限制。<br />
文字是 box 展開後預先顯示的文字（CROW 不支援），可省略。<br />
僅 SSP 可使用 --option=○○ 的格式指定[※選項](bang-close-textareabox-ID.note.md)，可省略。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\![open,inputbox,インプットテスト,10000,テスト入力]「テスト入力」と初期入力されたInputBoxを開く。OKボタンを押すか、10秒経過で自動的に閉じる。
```

```sakurascript
\![open,inputbox,インプットテスト,--timeout=10000,--text=テスト入力] 上記と同じ(新オプション指定)
```

```sakurascript
\![open,inputbox,OnNameInput,--placeholder=あなたの名前] 空欄に「あなたの名前」と薄く表示されたInputBoxを開く。[2.9.10]
```
