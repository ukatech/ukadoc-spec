# `\![embed,イベント名,r0,r1,r2...]`

**カテゴリ:** Event command

A special tag that **“embeds”** an event's result in this tag within the currently executing script.<br />
The options are used in the same way as for `\![raise]`; the third and subsequent arguments are stored in Reference0 onward, in order.

When the `\![embed]` tag is encountered during execution, the specified event is called. If it returns a result, the entire `\![embed]` tag is replaced with the result string, and script execution resumes from the first character of the replacement string.<br />
(This feature provides a broader, more general-purpose mechanism for synchronous SAORI calls during Satori execution.)

This was initially implemented for use with the property system as a way to call the property system, which does not itself return a result, and then use the result in the immediately following `\![embed]` tag to dynamically change processing, all “within a single script execution.” However, there is no such restriction in particular; this feature can be used whenever you want to perform some processing in sync with script execution.

**対応:** SSP / Ninix

## 記述例

```sakurascript
このトークの最後に、SHIORIイベント「OnEmbedTest」の実行結果が表示される。raiseと違いスクリプトが1つなので、スクリプト終了で効果が切れるさくらスクリプト(フォント変更など)が持続する。\![embed,OnEmbedTest]
```

```sakurascript
里々のテンプレートでこのスクリプトを実行した場合は、この文の後にランダムトークがくっつく。\![embed,OnTalk]
```
