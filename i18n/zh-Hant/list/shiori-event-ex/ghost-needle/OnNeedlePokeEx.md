# OnNeedlePokeEx

**カテゴリ:** ghost「Needle」

當 Needle（透過重疊）「戳」其他 ghost 時觸發。此事件在 [OnNeedlePoke](OnNeedlePoke.md) 之前觸發，是 OnNeedlePoke 的多 scope 版本，可用於進階處理。

- **Reference0**: 所有被戳的 scope ID 組成的陣列，以逗號分隔。主要角色為 0，次要角色為 1，其他角色為 2 以後的數值。
- **Reference1**: Needle 目前使用的 shell 名稱。
- **Reference2**: 目前的 dressup 清單。這是二維陣列，各 dressup 以 0xFDEF 分隔，每個 dressup 的類別名稱與部件名稱以 0x01 分隔。（例："Color\[0x01\]Gray\[0xFDEF\]Bow\[0x01\]Pink"）
