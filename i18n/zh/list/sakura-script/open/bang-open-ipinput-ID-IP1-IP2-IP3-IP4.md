# `\![open,ipinput,ID,表示時間,IP1桁目,IP2桁目,IP3桁目,IP4桁目,オプション]`

**カテゴリ:** 打开命令

打开IP地址输入InputBox。<br />
在Windows上，由于输入框的限制，只能接受IPv4地址。<br />
可以按照--option=○○的格式指定[※选项](bang-close-textareabox-ID.note.md)。

<br />
其他行为与[inputbox](bang-open-inputbox-ID.md)相同。

**対応:** SSP

## 記述例

```sakurascript
\![open,ipinput,IP入力テスト,30000,192,168,0,1]
```

```sakurascript
\![open,ipinput,IP入力テスト,--timeout=30000,--text="192,168,0,1"]
```
