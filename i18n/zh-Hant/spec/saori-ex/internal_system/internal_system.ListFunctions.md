# ListFunctions

**カテゴリ:** internal_system

傳回指定內建模組的函式名稱清單。函式名稱會以標準拼法（大小寫）傳回。<br />
非內建模組的名稱（包括相容模組）會回傳 400（`unknown module`）。

- **Argument1**: 模組名稱（不區分大小寫）

## 記述例

```
Argument0: ListFunctions
Argument1: internal_jwt

→ Result: Sign,Verify
→ Value0: Sign
→ Value1: Verify
```

**対応:** SSP 2.9.14
