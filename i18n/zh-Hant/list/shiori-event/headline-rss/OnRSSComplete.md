# OnRSSComplete

**カテゴリ:** 頭條／RSS 感知事件

headline sensor 正常結束時觸發。若未回應此事件，則會產生適合顯示的指令碼，並呼叫 headline 完成相關事件。

- **Reference0**: 沒有更新時：no update　[※結束原因](caption_headlinesenseresult.md)<br />
  沒有更新時，只有 Reference0，且內容僅為字串 "no update"<br />
  有更新時：RSS 發布網站名稱。
- **Reference1**: 僅有更新時：RSS 來源 URL（指向發布網站，而非 feed 本身）
- **Reference2～**: 僅有更新時：標題 \[`\1`\] URL \[`\1`\] 更新日期時間（格式以逗號分隔：年、月、日、時、分、秒）\[`\1`\] 作者名稱 \[`\1`\] 內容或摘要<br />
  有更新時，Reference0、1、2～會依 RSS 項目數量依序出現<br />
  \[`\1`\] 為 byte 值 1

**対応:** SSP 作者名稱、內容 2.4.10～
