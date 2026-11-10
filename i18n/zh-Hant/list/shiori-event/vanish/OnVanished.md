# OnVanished

**カテゴリ:** 消滅事件

前一個 ghost 消失後切換為自己時觸發。<br />
在SSP中，若此事件未傳回腳本（204），接著會觸發[OnBoot](../boot-close-change/OnBoot.md)。<br />
另請注意，在SSP中，同時啟動的其他 ghost 消失時，若OnOtherGhostVanished未傳回腳本，也會觸發此事件。此情況不會回退至OnBoot。

- **Reference0**: 消失的 ghost 本體名稱。
- **Reference1**: ※僅限SSP　消失的 ghost 的OnVanishSelected事件腳本。
- **Reference2**: ※僅限SSP　消失的 ghost 名稱。
- **Reference7**: ※僅限SSP　*切換後的 ghost 的*shell 名稱。

**対応:** Materia / SSP / CROW / Ninix
