# capability

**カテゴリ:** Notify event

Notifies the SHIORI extension implementation status.*\[NOTIFY\]*

- **Reference\***: Depending on the implementation level, each of the following is sent as a separate Reference.<br />
  Note that header names are sent in lowercase. Example: SecurityLevel→securitylevel<br />
  See also the [SHIORI/3.0 specification](../../../spec/shiori3/index.md).

  - **request.(lowercase header name)**: SHIORI request support status. Example: request.status
  - **response.(lowercase header name)**: SHIORI response support status. Example: response.marker

**対応:** SSP
