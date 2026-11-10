# OnOtherSurfaceChange

**カテゴリ:** surface事件

其他ghost（不包括自身）的surface（表情）发生变化时通知。<br />
为减少负载，此事件默认禁用。要使用此事件，必须事先通过 `\![set,othersurfacechange,true]` 启用。

- **Reference0**: ghost名
- **Reference1**: ghost的Sakura名
- **Reference2**: surface切换的窗口ID（Sakura=0）
- **Reference3**: 新surface ID
- **Reference4**: 旧surface ID
- **Reference5**: 新surface的尺寸（坐标：左、上、右、下）

**対応:** SSP / Ninix
