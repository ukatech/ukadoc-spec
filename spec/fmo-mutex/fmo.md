# FMO (File Mapping Object)

すべてのベースウェアは起動中に名前つきファイルマッピングオブジェクト(FMO)を保持しています。<br />
このプロセス間共有メモリを読み取ることで、起動中のゴーストを比較的低コストで取得できます。<br />
書き込み中の不完全な情報の読み取りを避けるため、排他制御は[FMO用Mutex](fmo-mutex.md)で行っています。あわせて確認してください。

- **FMOの名前と文字コード**: Sakura : OS依存、日本語OS上はShift JIS<br />
  SakuraUnicode : UTF-8固定 \[SSP 2.5.26以降～\]
- **FMOのサイズ**: 最初の4バイト(0～3バイト目)は確保されているFMOのサイズを示します。<br />
  これは書き込まれている情報の長さではなく、あくまでもFMO自体の確保サイズを示す固定値です。<br />
  値は現在のところリトルエンディアンで0x00010000、つまり64KB固定になります。<br />
  他プログラムとの互換性確保のため、現在のところサイズ変更は考慮されていません。
- **データ本体**: 4バイト目以降はFMOのデータ本体になります。これは以下のフォーマットになります。<br />
  (32バイトの識別ID).(キー名)\[`\1`\]値\[`\r\n`\]<br />
  \[`\1`\]はバイト値1、\[`\r\n`\]はCR+LF(改行)になります。<br />
  このフォーマットを複数行繰り返す形になります。
- **データ終端**: データ終端はC言語文字列と同じバイト値0になります。<br />
  ゆえに、データ本体で使用可能な最大サイズは65531バイト(65536 - 4 - 1)になります。<br />
  FMOに書き込む必要がある場合、サイズの限界を超えそうな場合は、不完全な情報の書き込みにならないよう留意してください。<br />
  サイズを超えそうな場合は1組分のデータを丸々書き込まないようにするのが望ましく、それが無理な場合でも1行の途中で終わらないようにしてください。

## データ本体の例

```
ssp_fmo_header_00004468_000f0dea.path[\1]D:\ssp\
ssp_fmo_header_00004468_000f0dea.hwnd[\1]986602
ssp_fmo_header_00004468_000f0dea.name[\1]ラーシェ
ssp_fmo_header_00004468_000f0dea.keroname[\1]ティセ
ssp_fmo_header_00004468_000f0dea.sakura.surface[\1]0
ssp_fmo_header_00004468_000f0dea.kero.surface[\1]10
ssp_fmo_header_00004468_000f0dea.kerohwnd[\1]1052114
ssp_fmo_header_00004468_000f0dea.hwndlist[\1]986602,1052114
ssp_fmo_header_00004468_000f0dea.ghostpath[\1]D:\ssp\ghost\DE10_3001\
ssp_fmo_header_00004468_00120da6.path[\1]D:\ssp\
ssp_fmo_header_00004468_00120da6.hwnd[\1]1183142
ssp_fmo_header_00004468_00120da6.name[\1]Emily
ssp_fmo_header_00004468_00120da6.keroname[\1]Teddy
ssp_fmo_header_00004468_00120da6.sakura.surface[\1]20
ssp_fmo_header_00004468_00120da6.kero.surface[\1]10
ssp_fmo_header_00004468_00120da6.kerohwnd[\1]1117626
ssp_fmo_header_00004468_00120da6.hwndlist[\1]1183142,1117626,921002,2035340,658950
ssp_fmo_header_00004468_00120da6.ghostpath[\1]D:\ssp\ghost\emily4\
```

- **32バイトの識別ID**: ゴースト1組分を示すユニークな識別IDです。少なくともFMO内では他と重複しない文字列を選ぶ必要があります。<br />
  何かユニークな情報を組み合わせてMD5ハッシュを取ったり、HWND(ウインドウハンドル)を組み合わせたりしている場合が多いです。<br />
  Materiaでの規格上は長さは規定されていませんが、互換性のため32バイト固定長とすべきです。

- **キー名・値**: 情報の種類を示すキーと情報本体です。以下の通りです。

  - **path**: 起動しているベースウェアのルートフォルダのフルパス。
  - **hwnd**: メインとなるウインドウのウインドウハンドル。10進表記。
  - **name**: descript.txtのsakura.nameと同じもの。
  - **keroname**: descript.txtのkero.nameと同じもの。
  - **sakura.surface**: `\0`側で現在表示しているサーフィスID。10進表記。
  - **kero.surface**: `\1`側で現在表示しているサーフィスID。10進表記。
  - **kerohwnd**: `\1`側ウインドウのウインドウハンドル。10進表記。\[SSPのみ\]
  - **hwndlist**: 現在使用しているウインドウハンドルをすべてカンマ区切りで列挙。10進表記。\[SSPのみ\]
  - **ghostpath**: 起動中ゴーストのフルパス。\[SSPのみ\]
  - **fullname**: 起動中ゴーストのdescript.txtのnameエントリ。\[SSP 2.5.58～\]
  - **modulestate**: 起動中のゴーストに読み込まれているモジュール群の状態を示すカンマ区切りの文字列。\[SSP 2.5.79～\]<br />
    shiori:running SHIORIがロードされている(ロードされていない場合は文字列自体が存在しない)<br />
    makoto-ghost:running ゴースト側のMAKOTOがロードされている<br />
    makoto-shell:running シェル側のMAKOTOがロードされている<br />
    compatible:running 互換モードに切り替わりscript.txtなどがロードされている<br />
    SSPと各種モジュール群の間の通信に異常がある場合は、runningの代わりにcriticalが入る<br />
    例： ssp_fmo_header_00004468_00120da6.modulestate\[`\1`\]shiori:running,makoto-ghost:running\\r\\n
