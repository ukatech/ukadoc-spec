# 互換モジュール

SSPはよく使われていた次のSAORI DLLの互換の機能を内蔵しています。ゴーストがこれらのDLLをloadすると、SSPはDLLを読まずに内蔵の機能に差し替えます（ファイル名で判定します）。<br />
\[SSP 2.9.13\] これらはDirect SSTPからも、DLL名から`.dll`を除いた名前（`Module: string`など）で呼べます。引数と戻り値は原作のSAORIのままです。

`houchi` `clipcopy` `textcopy` `saori_ip` `saori_cpuid` `mciaudio` `cpuusage` `httpc` `string` `hanayu` `osuwari`（`osuwari`は \[SSP 2.9.33\]）

- Direct SSTPには`load` / `unload`が無いので、ゴーストごとに状態を持つもの（`mciaudio` / `httpc` / `string` / `hanayu`）は、そのゴーストの最初の呼び出しで用意し、ゴーストの終了（SHIORIの再読み込みを含む）で捨てます。DLLとしてloadしたものとは状態を共有しません。
- ゴーストなしの呼び出しでは、ゴーストに依存する処理（`httpc`の取得・保存と`bg`、`hanayu`の`show`、`mciaudio`の`load` / `play` / `loop` / `stop`）は400（`ghost required`）になります。
- `houchi`はloadしたときに働くものなので、Direct SSTPから呼んでも何も起きません。
- Direct SSTPの要求はSSPの主スレッドで処理されるので、`httpc`の取得は`bg`を付けて行ってください（付けないと、取得の間SSPの画面が止まります）。

## osuwari \[SSP 2.9.33\]

ukiya氏の`Osuwari.dll`の互換です。ゴーストのウインドウを、前面のウインドウ・指定したウインドウ・画面の矩形に追尾させます（[`\![set,alignmenttodesktop,osuwari,…]`](../../list/sakura-script/surface/note-1.md#setalignmenttodesktoposuwariについて)と同じ処理で、オプションの意味もそちらに書いてあります）。引数は原作と同じ位置引数です。

- `START`: `Argument1`から順に、制御対象のHWND / 追尾対象（`ACTIVE` `FIX` `@タイトル` `#ハンドル`） / 原点（`TL` `TR` `BL` `BR`） / xのずれ / yのずれ / 更新間隔（ミリ秒。0は100） / (省略可)オプション（`XMOVE` `YMOVE` `NOCLIP` `BACK`をスペース区切り。`BACK`は対象のウインドウのすぐ奥に座ります。原作にはありません） / (省略可)座れないときの指定（`DESKTOP` `WORKAREA`と、`CENTER` `LEFT` `RIGHT` `TOP` `BOTTOM`をスペース区切り） / (省略可)見切れマージン（`左_上_右_下`）。
  - 7つめの引数以降を省略すると、前回の`START`の値を引き継ぎます。原作と同じ動作です。`\![set,alignmenttodesktop,osuwari,…]`のほうは、省略したオプションを毎回既定値にします（引き継ぎません）。
  - 制御対象のHWNDは、`OnHWND`イベント（`hwnd`）で通知される、**そのゴーストのキャラクターのウインドウ**だけを指定できます。他のウインドウは動かしません（見つからなければ500）。
- `STOP`: SAORIが設定したお座りを止め、アラインをゴースト・シェルの既定（`descript.txt`）へ戻します。`descript.txt`の既定がosuwariなら、osuwariに座り直します。`\![set,alignmenttodesktop,osuwari,…]`で設定したものは止めません。SAORIのアンロード（SHIORIの再読み込みを含む）でも止まります。
- 成功は204、引数が足りない・解釈できないときは400、制御対象のHWNDが見つからないときは500（`source window is not exist`）です。
- 原作との違いは次のとおりです。
  - ウインドウの矩形は、見た目の枠で測ります。
  - 基準とする画面は、対象のウインドウがあるモニタです（見切れは全モニタを合わせた領域で判定します）。
  - `DESKTOP`を指定したときに`side`が常に`TOP`になる原作の不具合はありません。
  - 最小化・非表示のウインドウには座りません。
  - シェルの`descript.txt`に`seriko.alignmenttodesktop,free`を書く必要はありません。
- 名前を変えたDLL（`osuwari0.dll`など）は互換の対象になりません。本物のDLLが読まれます。
