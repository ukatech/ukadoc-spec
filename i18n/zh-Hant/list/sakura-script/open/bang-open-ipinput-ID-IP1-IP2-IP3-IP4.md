# `\![open,ipinput,ID,表示時間,IP1桁目,IP2桁目,IP3桁目,IP4桁目,オプション]`

**カテゴリ:** 開啟指令

開啟 IP 位址輸入用的 InputBox。<br />
在 Windows 上，由於輸入框的限制，只能接受 IPv4 位址。<br />
可使用 --option=○○ 的格式指定[※選項](bang-close-textareabox-ID.note.md)。

<br />
其他行為與[inputbox](bang-open-inputbox-ID.md)相同。

**対応:** SSP

## 記述例

```sakurascript
\![open,ipinput,IP入力テスト,30000,192,168,0,1]
```

```sakurascript
\![open,ipinput,IP入力テスト,--timeout=30000,--text="192,168,0,1"]
```
