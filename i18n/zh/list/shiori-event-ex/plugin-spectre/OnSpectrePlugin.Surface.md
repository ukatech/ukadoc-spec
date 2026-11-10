# OnSpectrePlugin.Surface

**カテゴリ:** 插件“Spectre”

Spectre对话期间，请求当前正在交谈的ghost切换surface时触发。<br />
请注意，此事件不是由插件本身直接触发，而是由ghost通过对话中的嵌入标签调用。<br />
其中包含的表情见[推荐表情](../../../descript/shell-surfaces/surface-brace/caption_standarddef.md)，并额外加入了一些英语圈ghost常用的表情。<br />
*如果ghost的shell无法准确呈现某种表情，请忽略该表情且不要返回响应。* 插件会将此信息用于自身的用途。

- **Reference0**: 请求的表情。值为以下之一。

  - normal …… 通常为surface0
  - embarrassed …… 通常为surface1
  - surprised …… 通常为surface2
  - anxious …… 通常为surface3
  - discouraged …… 通常为surface4
  - smile …… 通常为surface5
  - relieved …… 通常为surface6。也称为“contented”
  - angry …… 通常为surface7
  - sweat …… 通常为surface8。也称为“sweat smile”或“cold smile”
  - indignant …… 通常为surface9。也称为“embarrassed anger”
  - thinking …… 英语圈的部分ghost常用。也称为“thoughtful”或“confused”
  - unamused …… 英语圈的部分ghost常用。也称为“bored”
