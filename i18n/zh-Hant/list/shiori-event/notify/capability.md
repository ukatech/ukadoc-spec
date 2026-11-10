# capability

**カテゴリ:** Notify event

通知 SHIORI 擴充功能的實作狀態。*\[NOTIFY\]*

- **Reference\***: 依實作等級，各項資訊會逐一傳送至 Reference。<br />
  請注意，通知時會將標頭名稱轉為小寫。例：SecurityLevel→securitylevel<br />
  另請參閱 [SHIORI/3.0仕様書](../../../spec/shiori3/index.md)。

  - **request.(ヘッダ名小文字)**: SHIORI 請求的支援狀態。例：request.status
  - **response.(ヘッダ名小文字)**: SHIORI 回應的支援狀態。例：response.marker

**対応:** SSP
