# ListFunctions

**カテゴリ:** internal_system

指定した内蔵モジュールの関数名の一覧を返す。関数名は正規の綴り（大文字小文字）で返る。<br />
内蔵モジュールでない名前（互換モジュールを含む）は400（`unknown module`）。

- **Argument1**: モジュール名（大文字小文字は区別しない）

## 記述例

```
Argument0: ListFunctions
Argument1: internal_jwt

→ Result: Sign,Verify
→ Value0: Sign
→ Value1: Verify
```

**対応:** SSP 2.9.14
