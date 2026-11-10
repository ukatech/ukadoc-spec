# OnOtherSurfaceChange

**カテゴリ:** surface 事件

（自己以外的）其他 ghost 的 surface（表情）變更時會收到通知。<br />
為避免增加負載，此事件預設為停用。若要使用此事件，必須事先透過 `\![set,othersurfacechange,true]` 啟用。

- **Reference0**: ghost 名稱
- **Reference1**: ghost 的 Sakura 名稱
- **Reference2**: surface 切換的視窗 ID（Sakura=0）
- **Reference3**: 新 surface ID
- **Reference4**: 舊 surface ID
- **Reference5**: 新 surface 的大小（座標：左、上、右、下）

**対応:** SSP / Ninix
