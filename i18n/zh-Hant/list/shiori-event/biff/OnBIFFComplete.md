# OnBIFFComplete

**カテゴリ:** 郵件檢查事件

郵件檢查成功時觸發。

- **Reference0**: 佇列中的郵件數量，以１為起始索引。
- **Reference1**: 佇列中的郵件位元組數。
- **Reference2**: 要檢查的郵件伺服器名稱。
- **Reference3**: 新收到的郵件差異。
- **Reference4**: 所有郵件的 TopResult。POP 通訊的所有標頭清單。以位元組值2分隔每封郵件，以位元組值1分隔各標頭（通常使用 Reference7 的資訊即可）。
- **Reference5**: ListResult。郵件伺服器上的 ID。內容相當於 POP 指令「LIST」的結果。
- **Reference6**: UidlResult。用來區分郵件的 ID。內容相當於 POP 指令「UIDL」的結果。
- **Reference7**: 以位元組值1分隔的寄件者與標題。

**対応:** Materia / SSP / CROW
