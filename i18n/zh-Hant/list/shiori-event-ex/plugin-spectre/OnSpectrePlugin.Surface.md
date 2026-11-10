# OnSpectrePlugin.Surface

**カテゴリ:** plugin「Spectre」

Spectre 對話期間，要求目前對話中的 ghost 切換 surface 時發生。<br />
請注意，此事件並非由 plugin 本身直接發出，而是由 ghost 透過對話中的內嵌標籤呼叫。<br />
其中包含[建議表情](../../../descript/shell-surfaces/surface-brace/caption_standarddef.md)，並額外加入一些英語系 ghost 常用的表情。<br />
*若 ghost 的 shell 無法準確呈現指定表情，請忽略並不要回應。* plugin 會將此資訊用於自身用途。

- **Reference0**: 要求的表情。值為下列其中之一。

  - normal …… 通常是 surface0
  - embarrassed …… 通常是 surface1
  - surprised …… 通常是 surface2
  - anxious …… 通常是 surface3
  - discouraged …… 通常是 surface4
  - smile …… 通常是 surface5
  - relieved …… 通常是 surface6。也稱為「contented」
  - angry …… 通常是 surface7
  - sweat …… 通常是 surface8。也稱為「sweat smile」或「cold smile」
  - indignant …… 通常是 surface9。也稱為「embarrassed anger」
  - thinking …… 部分英語系 ghost 常用。也稱為「thoughtful」或「confused」
  - unamused …… 部分英語系 ghost 常用。也稱為「bored」
