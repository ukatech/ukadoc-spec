# OnSpectrePlugin.Surface

**カテゴリ:** plugin“Spectre”

在Spectre的对话中，要求当前对话对象ghost切换surface时发生。<br />
注意，此事件并非由plugin本身直接触发，而是通过对话中的嵌入标签从ghost侧调用。<br />
包含的表情是[推荐表情](../../../descript/shell-surfaces/surface-brace/caption_standarddef.md)，以及一些英语ghost中常用的额外表情。<br />
*对于ghost的shell无法准确表现的表情，应忽略且不返回响应。* 因为plugin会将此信息用于自身用途。

- **Reference0**: 请求的表情。取以下值之一。

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
  - thinking …… 在部分英语ghost中常用。也称为“thoughtful”或“confused”
  - unamused …… 在部分英语ghost中常用。也称为“bored”
