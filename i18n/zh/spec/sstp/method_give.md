# 方法：GIVE

*\[旧规格\]* 用于向 ghost 提供各种数据并进行处理或使其作出反应的方法。<br />
这是非常古老的规格，现在没有使用它的意义。请使用 NOTIFY 或 COMMUNICATE。

## request 示例

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

## request 专用头

- **Document**: 文档（通用字符串）<br />
  在 SHIORI/3.0 中按与用户沟通相同的方式处理，并触发 OnCommunicate 事件。
- **Song**: 歌曲名称。<br />
  在 SHIORI/3.0 中会触发 OnMusicPlay 事件，Reference0 的值为 Song 头中指定的字符串。
