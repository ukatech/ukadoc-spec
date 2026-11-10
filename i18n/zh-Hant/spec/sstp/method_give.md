# 方法：GIVE

*\[舊規格\]* 這個方法可向 ghost 提供各種資料，讓它進行處理或做出反應。<br />
這是非常古老的規格，目前已沒有使用它的意義。請改用 NOTIFY 或 COMMUNICATE。

## request 範例

```
GIVE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Document: まず水や。それから粉やな。
```

```
GIVE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Song: 佐世保の時雨
```

## request 專用標頭

- **Document**：文件（一般用途的字串）<br />
  在 SHIORI/3.0 中會以與使用者 COMMUNICATE 相同的方式處理，並觸發 OnCommunicate 事件。
- **Song**：歌曲名稱。<br />
  在 SHIORI/3.0 中會觸發 OnMusicPlay 事件，Reference0 會設為 Song 標頭中指定的字串。
