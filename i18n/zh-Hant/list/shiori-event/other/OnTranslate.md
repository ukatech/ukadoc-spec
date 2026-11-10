# OnTranslate

**カテゴリ:** 其他事件

SHIORI用來兼任MAKOTO轉換功能的事件。<br />
主要在GET命令的SHIORI Event有腳本傳回baseware時，會依此發出事件。<br />
SHIORI會在內部處理OnTranslate來源的SHIORI Event，並將腳本傳回baseware；baseware展開環境變數等內容後，會再次將腳本傳送給SHIORI。SHIORI可以再次處理此腳本，並將最終腳本傳回baseware。<br />
此外，OnTranslate本身不會再次觸發。

- **Reference0**: 原始腳本。
- **Reference1**: ※僅限SSP　若為communicate，則為communicate。<br />
  若為SSTP SEND，則為sstp-send。<br />
  若為Owned SSTP，則為owned。<br />
  若為非本機SSTP，則為remote。<br />
  指定不進行轉換時，則為notranslate。<br />
  若為來自plugin的腳本，則為plugin-script<br />
  若為來自plugin的事件反應，則為plugin-event<br />
  符合的項目會以逗號分隔回傳。※若沒有符合項目，該項會省略。
- **Reference2**: ※僅限SSP　觸發此腳本的事件ID。若並非由事件觸發，該項會省略。
- **Reference3**: ※僅限SSP　上述事件的Reference，以位元組值1分隔。若並非由事件觸發，該項會省略。

**対応:** Materia / SSP / CROW / Ninix
