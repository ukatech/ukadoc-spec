# Protect

**カテゴリ:** internal_crypto

データを、OSのデータ保護機能（WindowsのDPAPI）で包む。包んだものは、同じPCの同じユーザー（`--scope=machine`なら同じPCの全ユーザー）でしか[Unprotect](internal_crypto.Unprotect.md)できない。<br />
セーブデータに置くトークンなどを、ほかのPCやほかのユーザーにコピーされても読めないようにするためのもので、ゴースト同士を分けるものではない（同じユーザーで動くほかのゴーストやプログラムは戻せる）。

- **Argument1**: data（既定の形式は`text`）
- **オプション**: `--data-in=` / `--scope=user`（既定） / `--scope=machine` / `--out=`（既定は`base64`） / `--charset=`

**セーブデータを別のPCへ持っていった場合（SSPのセーブデータ共有、クラウドストレージでの同期、手でのコピーなど）や、Windowsのユーザーを作り直した場合は、Unprotectできなくなります。**スクリプトはUnprotectの失敗を「ログインし直してもらう」などとして扱ってください。

**対応:** SSP 2.9.13
