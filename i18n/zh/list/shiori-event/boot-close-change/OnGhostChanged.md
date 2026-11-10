# OnGhostChanged

**カテゴリ:** 启动、关闭和切换事件

从其他 ghost 切换到本 ghost 时触发。<br />
在 SSP 中，如果对此事件没有返回脚本（204），则接着触发 [OnBoot](OnBoot.md)。

- **Reference0**: 前一个 ghost 的主角色名称。
- **Reference1**: 前一个 ghost 切换时的脚本。
- **Reference2**: 前一个 ghost 的名称。 \[仅限 SSP\]
- **Reference3**: 前一个 ghost 的路径（文件位置）。 \[仅限 SSP\]
- **Reference7**: *切换后的 ghost 的* shell 名称。 \[仅限 SSP\]

**対応:** Materia / SSP / CROW / Ninix
