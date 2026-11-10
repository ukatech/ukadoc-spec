# OnVanished

**カテゴリ:** 消失事件

因前一个 ghost 消失而切换到自身时触发。<br />
在SSP中，如果此事件没有返回脚本（204），则会接着触发[OnBoot](../boot-close-change/OnBoot.md)。<br />
另请注意，在SSP中，同时运行的其他ghost消失时，如果OnOtherGhostVanished没有返回脚本，也会触发此事件。此时不会回退到OnBoot。

- **Reference0**: 已消失ghost的本体侧名称。
- **Reference1**: ※仅SSP　已消失ghost的OnVanishSelected事件脚本。
- **Reference2**: ※仅SSP　已消失ghost的名称。
- **Reference7**: ※仅SSP　*切换到的ghost的*shell名称。

**対応:** Materia / SSP / CROW / Ninix
