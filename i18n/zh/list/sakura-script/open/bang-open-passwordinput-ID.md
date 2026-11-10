# `\![open,passwordinput,ID,表示時間,テキスト,オプション]`

**カテゴリ:** 打开命令

打开一个会隐藏输入字符的 InputBox。其他行为与[inputbox](bang-open-inputbox-ID.md)相同。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![open,passwordinput,パスワードテスト,-1,--option==noclose]入力が●で伏せ字になるInputBoxを開く。OKボタンを押しても、時間経過でも自動的に閉じない。閉じるボタンを押すと閉じる。
```

```sakurascript
\![open,passwordinput,パスワードテスト,--timeout=-1,--option==noclose] 上記と同じ(新オプション指定)
```
