# capability

**カテゴリ:** Notifyイベント

SHIORI拡張実装状態を通知。*\[NOTIFY\]*

- **Reference\***: 実装レベルに応じて下記がReferenceに1つずつ送られる。<br />
  ヘッダ名を小文字に直したものが通知される点に注意。例：SecurityLevel→securitylevel<br />
  [SHIORI/3.0仕様書](../../../spec/shiori3/index.md)も参照。

  - **request.(ヘッダ名小文字)**: SHIORIリクエストの対応状況。例：request.status
  - **response.(ヘッダ名小文字)**: SHIORIレスポンスの対応状況。例：response.marker

**対応:** SSP
