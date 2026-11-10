# OnTranslate

**カテゴリ:** 其他事件

SHIORI兼任MAKOTO的翻译功能时使用的事件。<br />
主要在对GET命令的SHIORI Event返回脚本给baseware时，根据情况发出。<br />
对于作为OnTranslate来源的SHIORI Event，SHIORI经过内部处理后返回给baseware的脚本，会在baseware展开环境变量等内容后再次发送给SHIORI。SHIORI可以再次处理该脚本，并将其作为最终脚本返回给baseware。<br />
另外，OnTranslate本身不会再次触发。

- **Reference0**: 原始脚本。
- **Reference1**: ※仅限SSP　通信交互时为communicate。<br />
  SSTP SEND时为sstp-send。<br />
  Owned SSTP时为owned。<br />
  非本地SSTP时为remote。<br />
  指定不进行翻译时为notranslate。<br />
  来自plugin的脚本时为plugin-script<br />
  来自plugin的事件响应时为plugin-event<br />
  符合多个条件时以逗号分隔返回。※没有符合项时会留空。
- **Reference2**: ※仅限SSP　此脚本触发的事件ID。若并非由事件触发，则留空。
- **Reference3**: ※仅限SSP　上述事件的Reference，以字节值1分隔。若并非由事件触发，则留空。

**対応:** Materia / SSP / CROW / Ninix
