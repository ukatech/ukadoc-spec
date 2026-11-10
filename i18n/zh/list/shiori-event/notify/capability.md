# capability

**カテゴリ:** Notify事件

通知SHIORI扩展功能的实现状态。*\[NOTIFY\]*

- **Reference\***: 根据实现级别，以下各项会分别作为一个Reference发送。<br />
  请注意，通知中的标头名称会转换为小写。例如：SecurityLevel→securitylevel<br />
  另请参阅[SHIORI/3.0规格说明书](../../../spec/shiori3/index.md)。

  - **request.(标头名称小写)**: SHIORI请求的支持情况。例如：request.status
  - **response.(标头名称小写)**: SHIORI响应的支持情况。例如：response.marker

**対応:** SSP
