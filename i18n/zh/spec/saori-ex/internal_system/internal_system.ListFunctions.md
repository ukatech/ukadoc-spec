# ListFunctions

**カテゴリ:** internal_system

Returns a list of function names in the specified built-in module. Function names are returned in their canonical spelling (including case).<br />
A name that is not a built-in module (including compatibility modules) results in 400 (`unknown module`).

- **Argument1**: Module name (case-insensitive)

## 記述例

```
Argument0: ListFunctions
Argument1: internal_jwt

→ Result: Sign,Verify
→ Value0: Sign
→ Value1: Verify
```

**対応:** SSP 2.9.14
