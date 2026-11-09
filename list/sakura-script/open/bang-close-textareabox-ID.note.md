# InputBoxオプション

○○の形で指定。すべて指定がなくても動く。

- **--option=(noclose|noclear)**: noclose:入力後、inputboxを閉じないで表示し続ける。<br />
  noclear:入力後、入力内容を初期化せずにそのまま表示し続ける。<br />
  nocloseと同時に指定する(例：`\![inputbox,入力内容,,,--option=noclose,--option=noclear]`)。<br />
  noclearは文字を入力しないinputbox(sliderinput,dateinput,timeinput,ipinput)では意味を持たない。
- **--text=デフォルト表示**: 最初から表示すべき文字列。<br />
  sliderinputでは初期値,最小,最大/dateinputでは年,月,日/timeinputでは時,分,秒
- **--placeholder=案内文 \[2.9.10\]**: 入力欄が空のときだけ薄く表示し、何を入力すればよいかを示す文字列(HTMLのplaceholderに相当)。文字を入力すると消え、空に戻すと再び表示される。<br />
  --text=と違い入力内容には含まれず、--limit=の文字数にも数えない。<br />
  文字色はバルーンの[communicatebox.placeholder.color](../../../descript/balloon/descript-txt/communicatebox.placeholder.color.r.md)で指定できる。指定が無ければ入力欄の文字色を背景色へ寄せ、さらに彩度を落とした色になる。<br />
  inputbox・passwordinput・textareaboxで有効(passwordinputでも伏せ字にせずそのまま表示する)。textareaboxでは`\1`で改行を表す。
- **--timeout=タイムアウトミリ秒**: 入力ボックスを自動的に閉じるまでの時間。ゼロ以下を指定すると閉じない。
- **--balloon=ID**: balloonc?.png/txtの?のところに入るIDを指定すると、そのIDに対応した画像を利用する。<br />
  指定がない場合は入力ボックスごとに標準で決まっているIDになる。 (SSP 2.6.23)
- **--limit=文字入力制限長さ**: 入力ボックスに入れられる文字数を制限する。
- **--reference=追加情報**: OnUserInputのReference3、またはOnではじまる指定イベントのReference2以降に指定した追加情報を追加する。
