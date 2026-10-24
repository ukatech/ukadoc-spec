# OnWindowModeChange

**カテゴリ:** OS状態イベント

SSPのウインドウモードが切り替えられた際に発生。*\[起動時NOTIFY/他GET\]*<br />
ウインドウモードは、ゴーストをデスクトップ上ではなくSSPが用意したウインドウ(コンテナ)の中に表示するモード。コンテナの内側がゴーストにとっての画面になる。<br />
切り替えによってゴーストにとっての画面の大きさが変わるため、このイベントの後に[OnDisplayChange](OnDisplayChange.md)も発生する。<br />
現在のモードは[baseware.windowmode](../../propertysystem/property-system/baseware.windowmode.md)でも取得できる。

- **Reference0**: init (起動時通知) か update (起動後の切り替え)
- **Reference1**: 現在のモード。<br />
  normal：通常モード(ゴーストをデスクトップ上に表示する)<br />
  shared：ウインドウモード。全ゴーストで1枚のコンテナを共有する<br />
  perghost：ウインドウモード。ゴースト1体につき1枚のコンテナを使う
- **Reference2**: 直前のモード。値の種類はReference1と同じ。Reference0がinitの場合は空。

**対応:** SSP 2.8.93
