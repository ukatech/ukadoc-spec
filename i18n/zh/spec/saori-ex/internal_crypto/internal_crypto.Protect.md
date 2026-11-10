# Protect

**カテゴリ:** internal_crypto

使用OS的数据保护功能（Windows DPAPI）封装数据。只有同一台电脑上的同一用户（如果是`--scope=machine`，则为同一台电脑上的所有用户）才能通过[Unprotect](internal_crypto.Unprotect.md)解封。<br />
此功能用于防止保存数据中的令牌等内容被复制到其他电脑或其他用户后仍可读取，并不用于隔离不同的ghost（使用同一用户运行的其他ghost或程序也能解封）。

- **Argument1**: data（默认格式为`text`）
- **选项**: `--data-in=` / `--scope=user`（默认） / `--scope=machine`（其他值会返回400 `invalid parameter`） / `--out=`（默认格式为`base64`） / `--charset=`

**如果将保存数据移到另一台电脑（例如共享SSP保存数据、通过云存储同步或手动复制），或重建Windows用户，将无法使用Unprotect**。脚本应将Unprotect失败视为需要“重新登录”等情况处理。

**対応:** SSP 2.9.13
