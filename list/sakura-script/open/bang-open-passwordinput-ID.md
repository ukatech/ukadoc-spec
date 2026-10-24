# `\![open,passwordinput,ID,表示時間,テキスト,オプション]`

**カテゴリ:** オープンコマンド

文字を隠すInputBoxを開く。その他の動作は[inputbox](bang-open-inputbox-ID.md)と同じ。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![open,passwordinput,パスワードテスト,-1,--option==noclose]入力が●で伏せ字になるInputBoxを開く。OKボタンを押しても、時間経過でも自動的に閉じない。閉じるボタンを押すと閉じる。
```

```sakurascript
\![open,passwordinput,パスワードテスト,--timeout=-1,--option==noclose] 上記と同じ(新オプション指定)
```
