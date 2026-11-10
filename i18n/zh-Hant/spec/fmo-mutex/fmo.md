# FMO (File Mapping Object)

所有 baseware 在執行期間都會保留具名檔案對應物件（FMO）。<br />
讀取這個跨處理序共用記憶體，即可用相對低廉的成本取得執行中的 ghost。<br />
為避免讀取到寫入中的不完整資訊，會使用[FMO Mutex](fmo-mutex.md)進行互斥控制。請一併確認。

- **FMO 名稱與字元編碼**: Sakura：依作業系統而異，在日文作業系統上為 Shift JIS<br />
  SakuraUnicode：固定為 UTF-8 \[SSP 2.5.26 之後～\]
- **FMO 大小**: 最初的 4 個位元組（第 0～3 個位元組）表示已配置的 FMO 大小。<br />
  這不是已寫入資訊的長度，而是表示 FMO 本身配置大小的固定值。<br />
  目前的值為小端序 0x00010000，也就是固定為 64KB。<br />
  為確保與其他程式的相容性，目前未考慮變更大小。
- **資料本體**: 從第 4 個位元組開始是 FMO 的資料本體，格式如下。<br />
  (32 位元組的識別 ID).(鍵名)\[`\1`\]值\[`\r\n`\]<br />
  \[`\1`\]是位元組值 1，\[`\r\n`\]是 CR+LF（換行）。<br />
  以多行重複此格式。
- **資料結尾**: 資料結尾與 C 語言字串相同，為位元組值 0。<br />
  因此，資料本體可使用的最大大小為 65531 位元組（65536 - 4 - 1）。<br />
  如果需要寫入 FMO，請留意大小可能超出上限時，不要寫入不完整的資訊。<br />
  如果可能超出大小上限，最好不要寫入整組資料；即使無法做到，也請避免在一行中途結束。

## 資料本體範例

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

- **32 位元組的識別 ID**: 用來識別一組 ghost 的唯一識別 ID。至少必須選擇在 FMO 內不會與其他項目重複的字串。<br />
  常見做法是將某些唯一資訊組合後計算 MD5 雜湊，或組合 HWND（視窗控制代碼）。<br />
  Materia 的規格未規定長度，但為了相容性，應固定為 32 位元組。

- **鍵名與值**: 表示資訊種類的鍵與資訊本體。如下所示。

  - **path**: 執行中 baseware 根資料夾的完整路徑。
  - **hwnd**: 主要視窗的視窗控制代碼。以十進位表示。
  - **name**: 與 descript.txt 的 sakura.name 相同。
  - **keroname**: 與 descript.txt 的 kero.name 相同。
  - **sakura.surface**: `\0`側目前顯示的 surface ID。以十進位表示。
  - **kero.surface**: `\1`側目前顯示的 surface ID。以十進位表示。
  - **kerohwnd**: `\1`側視窗的視窗控制代碼。以十進位表示。\[僅限 SSP\]
  - **hwndlist**: 以逗號分隔列出目前使用的所有視窗控制代碼。以十進位表示。\[僅限 SSP\]
  - **ghostpath**: 執行中 ghost 的完整路徑。\[僅限 SSP\]
  - **fullname**: 執行中 ghost 的 descript.txt 中的 name 項目。\[SSP 2.5.58～\]
  - **modulestate**: 以逗號分隔的字串，表示執行中 ghost 所載入的模組狀態。\[SSP 2.5.79～\]<br />
    shiori:running 表示已載入 SHIORI（未載入時，字串本身不存在）<br />
    makoto-ghost:running 表示已載入 ghost 端的 MAKOTO<br />
    makoto-shell:running 表示已載入 shell 端的 MAKOTO<br />
    compatible:running 表示已切換至相容模式，並已載入 script.txt 等檔案<br />
    SSP 與各種模組之間的通訊發生異常時，會以 critical 取代 running<br />
    範例： ssp_fmo_header_00004468_00120da6.modulestate\[`\1`\]shiori:running,makoto-ghost:running\\r\\n
