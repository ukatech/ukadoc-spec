# 互換モジュール

SSPはよく使われていた次のSAORI DLLの互換の機能を内蔵しています。ゴーストがこれらのDLLをloadすると、SSPはDLLを読まずに内蔵の機能に差し替えます（ファイル名で判定します）。<br />
\[SSP 2.9.13\] これらはDirect SSTPからも、DLL名から`.dll`を除いた名前（`Module: string`など）で呼べます。引数と戻り値は原作のSAORIのままです。

`houchi` `clipcopy` `textcopy` `saori_ip` `saori_cpuid` `mciaudio` `cpuusage` `httpc` `string` `hanayu`

- Direct SSTPには`load` / `unload`が無いので、ゴーストごとに状態を持つもの（`mciaudio` / `httpc` / `string` / `hanayu`）は、そのゴーストの最初の呼び出しで用意し、ゴーストの終了（SHIORIの再読み込みを含む）で捨てます。DLLとしてloadしたものとは状態を共有しません。
- ゴーストなしの呼び出しでは、ゴーストに依存する処理（`httpc`の取得・保存と`bg`、`hanayu`の`show`、`mciaudio`の`load` / `play` / `loop` / `stop`）は400（`ghost required`）になります。
- `houchi`はloadしたときに働くものなので、Direct SSTPから呼んでも何も起きません。
- Direct SSTPの要求はSSPの主スレッドで処理されるので、`httpc`の取得は`bg`を付けて行ってください（付けないと、取得の間SSPの画面が止まります）。
