# ListFunctions

**カテゴリ:** internal_system

返回指定内置模块的函数名列表。返回的函数名采用规范拼写（大小写）。<br />
名称不是内置模块的模块（包括兼容模块）会返回 400（`unknown module`）。

- **Argument1**: 模块名（不区分大小写）

## 記述例

```
Argument0: ListFunctions
Argument1: internal_jwt

→ Result: Sign,Verify
→ Value0: Sign
→ Value1: Verify
```

**対応:** SSP 2.9.14
