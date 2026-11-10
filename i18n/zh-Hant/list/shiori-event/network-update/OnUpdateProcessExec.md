# OnUpdateProcessExec

**カテゴリ:** 網路更新事件

從選單等處下達執行更新的指示時觸發。<br />
對此事件回傳任何 script，即可自訂更新處理。<br />
忽略此事件時，會自動進入標準更新處理。

- **Reference0**: manual : 從選單執行更新操作。<br />
  auto : 執行預先設定的定期自動更新處理。<br />
  testonly : 執行開發用調色盤中的 Update Full Check。

**対応:** SSP 2.6.23
