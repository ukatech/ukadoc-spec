# 非同步呼叫

內建模組（名稱以`internal_`開頭）的函式加上選項`--async=識別子`後，便會以非同步方式執行。收到要求後會立即以204回應，結果則會在稍後以事件傳送給呼叫端的ghost。<br />
沒有ghost時無法呼叫（400 `ghost required`）。識別子為空時會回傳400（`invalid parameter`）。<br />
請在耗時較長的處理（大型檔案的雜湊、密碼雜湊、金鑰導出、RSA金鑰組生成等）中使用`--async`。<br />
在SSP中，同時執行的非同步呼叫數量最多為CPU數量（2～4）。超過的部分會等待前面的呼叫完成後再依序執行。

## 傳送結果的事件

- **事件名稱**: 如果識別子以`On`開頭（區分大小寫），成功時事件名稱就是該識別子，失敗時則為「識別子＋`Failure`」。如果使用既有事件名稱（例如`OnBoot`）作為識別子，結果會以該事件傳送，請避免這樣做。<br />
  否則，成功時會傳送[OnInternalSaoriComplete](../../list/shiori-event/other/OnInternalSaoriComplete.md)，失敗時會傳送[OnInternalSaoriFailure](../../list/shiori-event/other/OnInternalSaoriFailure.md)。
- **成功時的Reference**: Reference0＝識別子、Reference1＝結果（與同步呼叫的`Result`相同）、Reference2＝模組名稱、Reference3＝函式名稱、Reference4以後＝`Value0`以後。
- **失敗時的Reference**: Reference0＝識別子、Reference1＝失敗原因（與同步呼叫的`ErrorDescription`相同的字串）、Reference2＝模組名稱、Reference3＝函式名稱。

引數數量錯誤或選項名稱錯誤會在受理時回傳400。引數內容錯誤（例如無法讀取的十六進位值）則會透過失敗事件傳送。

## 結果送達的條件與順序

- 只要呼叫端的ghost尚未結束，就一定會收到結果。即使ghost處於時間關鍵狀態、被動模式或導引模式，也會收到結果（即使暫存至快取，只要SHIORI仍載入中，就會收到）。\[SSP 2.9.27\] 在此版本之前，處理在這些狀態期間結束時，結果可能不會送達。
- SHIORI正在處理其他request時，會等該request處理完畢後才送達。
- 如果呼叫端的ghost在結果送達前結束（包括重新載入SHIORI），結果就不會送達。
- 多個非同步呼叫的結果送達順序不一定與呼叫順序相同（會依處理完成順序送達；超過同時執行數量而等待的呼叫，則會依可用執行名額的順序開始）。需要順序時，請以識別子對應結果，或等前一個結果送達後再呼叫下一個。
