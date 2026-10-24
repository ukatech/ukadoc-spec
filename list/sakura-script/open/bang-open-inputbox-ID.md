# `\![open,inputbox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** オープンコマンド

InputBoxを開く。<br />
決定時(OKボタンを押す)にSHIORIイベント、[OnUserInput](../../shiori-event/inputbox/OnUserInput.md)が発生する。<br />
表示時間を過ぎた(タイムアウトした)場合と、閉じるボタンを押して閉じた場合は、[OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)が発生する。<br />
OnUserInputCancelに応答がない場合、かつ表示時間からタイムアウトした場合は、互換性確保のため、"timeout"を入力テキストとしたOnUserInputが発生する。<br />
なお入力中は他の一切の操作を受け付けない制御がされていたが、SSPではそうならない。

<br />
IDは決定時に発生するOnUserInputに格納されるが、IDが「On」で始まる場合、ID名のイベントが発生する。[※ID](notes_inputbox-id.md)参照。<br />
表示時間はミリ秒で指定。省略するか、0以下の数を指定すると、表示時間無制限。<br />
テキストはbox展開直後にあらかじめ表示するテキスト(CROW不可)、省略可。<br />
SSPのみ、--option=○○の形で[※オプション](notes_inputbox-option.md)指定可能。省略可。

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
