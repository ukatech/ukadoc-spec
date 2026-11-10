# `\![open,ipinput,ID,表示時間,IP1桁目,IP2桁目,IP3桁目,IP4桁目,オプション]`

**カテゴリ:** Open commands

Opens an IP address input box.<br />
On Windows, only IPv4 addresses can be accepted due to input box limitations.<br />
Options can be specified in the form --option=○○; see [※Options](bang-close-textareabox-ID.note.md).

<br />
Other behavior is the same as for [inputbox](bang-open-inputbox-ID.md).

**対応:** SSP

## 記述例

```sakurascript
\![open,ipinput,IP入力テスト,30000,192,168,0,1]
```

```sakurascript
\![open,ipinput,IP入力テスト,--timeout=30000,--text="192,168,0,1"]
```
