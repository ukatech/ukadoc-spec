# 本頁的格式說明

本頁說明 SHIORI/3.0 及 3.1（SSP 擴充定義）所發出的各個 SHIORI Event ID。<br />
未列於此處的事件，可能會出現在 [SHIORI Resource](../shiori-resource/index.md) 或[外部 SHIORI Event](../shiori-event-ex/index.md)頁面。

若需要了解 SHIORI Event 本身，請參閱「[補充：什麼是 SHIORI Event](../../memo/shiori-event.md)」頁面。

## Reference 清單說明

具有 Reference 的 SHIORI Event 各自都有 Reference 清單。<br />
若 Reference 的編號部分標示為「\*」，表示 Reference 的數量不固定。<br />
也就是說，該 Reference 的*數量會依執行環境而異，因此編號不固定*，而且這些數量不固定的 Reference *內容格式都相同*。<br />
即使如此，Reference 仍遵循從 0 開始依序編號的原則。因此，若 Reference 清單中只有編號為 \* 的項目，就會有格式相同的 Reference 從 0 開始排列至不固定的編號（數量依環境而定）；若清單中列到 Reference2，下一行則是 Reference\*，格式相同的 Reference 就會從 3 開始排列至不固定的編號。

## \[NOTIFY\] 標示說明

說明文字中標示為 *\[NOTIFY\]* 的 SHIORI Event，通常會透過 NOTIFY 命令發出。<br />
未特別標示時，通常會透過 GET 命令發出。
