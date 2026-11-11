# OnSpectrePlugin.Surface

**カテゴリ:** plugin「Spectre」

在 Spectre 的對話中，要求目前正在被搭話的 ghost 切換 surface 時發生。<br />
注意，此事件並非由 plugin 本身直接發出，而是透過對話中的嵌入標籤從 ghost 端呼叫。<br />
包含的表情為[建議表情](../../../descript/shell-surfaces/surface-brace/caption_standarddef.md)，另加上少數英語圈 ghost 常用的表情。<br />
*ghost 的 shell 無法準確呈現的表情應予以忽略，不要回傳回應。* 因為 plugin 會將此資訊用於自身用途。

- **Reference0**: 要求的表情。值為以下其中之一。

  - normal …… 通常為 surface0
  - embarrassed …… 通常為 surface1
  - surprised …… 通常為 surface2
  - anxious …… 通常為 surface3
  - discouraged …… 通常為 surface4
  - smile …… 通常為 surface5
  - relieved …… 通常為 surface6。也稱為「contented」
  - angry …… 通常為 surface7
  - sweat …… 通常為 surface8。也稱為「sweat smile」或「cold smile」
  - indignant …… 通常為 surface9。也稱為「embarrassed anger」
  - thinking …… 常見於部分英語圈 ghost。也稱為「thoughtful」或「confused」
  - unamused …… 常見於部分英語圈 ghost。也稱為「bored」
