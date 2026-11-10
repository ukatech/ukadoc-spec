# OnUserInputCancel

**カテゴリ:** 输入框事件

InputBox 关闭时触发。<br />
发生超时且此事件没有收到响应时，为确保兼容性，会发送 OnUserInput Reference1=timeout。

- **Reference0**: 输入事件的 ID。
- **Reference1**: 超时时为 timeout。关闭时为 close。
- **Reference2**: 输入内容的补充信息（仅 sliderinput 使用，最小值,最大值。其他情况为空）
- **Reference3～**: 通过 --reference= 指定的附加信息

**対応:** SSP / Ninix
