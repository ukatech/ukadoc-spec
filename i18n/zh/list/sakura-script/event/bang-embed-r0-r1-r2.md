# `\![embed,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

A special tag that **“embeds”** the result of an event in this tag within the currently executing script.<br />
The options are used in the same way as for `\![raise]`, with the third and subsequent arguments stored in Reference0 and onward, in order.

When the `\![embed]` tag is encountered during execution, the specified event is called. If it returns a result, the entire `\![embed]` tag is replaced with the result string, and script execution resumes from the first character of the replacement string.<br />
(This feature provides a more general-purpose way to use the mechanism for calling SAORI “sync” during Satori execution.)

Originally, this was implemented for use with the property system as a mechanism to perform, “within a single script execution,” dynamic processing based on the result of the property system call, which itself does not return a result, by embedding a `\![embed]` tag immediately afterward. However, there is no particular restriction to this use; it can be used whenever you want to synchronize some processing with script execution.

**対応:** SSP / Ninix

## 記述例

```sakurascript
このトークの最後に、SHIORIイベント「OnEmbedTest」の実行結果が表示される。raiseと違いスクリプトが1つなので、スクリプト終了で効果が切れるさくらスクリプト(フォント変更など)が持続する。\![embed,OnEmbedTest]
```

```sakurascript
里々のテンプレートでこのスクリプトを実行した場合は、この文の後にランダムトークがくっつく。\![embed,OnTalk]
```
