# DLL共通仕様

## DLL共通仕様

本仕様は、SHIORI、SAORI、その他の伺かシステムで使用されるDLLモジュールの共通インターフェースを定義するものである。

## メモリ管理

引数／戻り値の受け渡しは全て Windows の Global Memory を使用して行う。具体的には以下の手順で処理を行う：

- ベースウェアは GlobalAlloc() に GMEM_FIXED フラグを指定してメモリを確保し、データを書き込む
- モジュールは受け取った HGLOBAL を (char\*) にキャストして直接データにアクセスする
- モジュールは len パラメータを参照してデータ長を取得し、必要なデータを読み込む
- モジュールは GlobalFree() でメモリを解放する
- 処理結果を返す場合、モジュールは新たに GlobalAlloc() で GMEM_FIXED 指定のメモリを確保する
- モジュールは確保したメモリに結果を書き込み、len に新しいデータ長を設定する
- ベースウェアは返却されたメモリハンドルを使用後に GlobalFree() で解放する

注意点：

- GMEM_FIXED フラグ使用時は GlobalLock()/GlobalUnlock() が不要である
- HGLOBAL を (char\*) にキャストすることで直接メモリアクセスが可能である
- 渡されたメモリはNULL終端が保証されていないため、必ずlenパラメータを参照してアクセス範囲を制限する
- 戻り値用のメモリは、ベースウェアの実装に依存せず堅牢な動作を保証するため、lenより1バイト多く確保してゼロ終端することが望ましい

## request関数

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

全てのリクエストは request という唯一の関数で行われる。request関数は伺かモジュールの主要なインターフェースであり、ベースウェアからの全ての要求を処理する。

リクエストデータの形式はHTTPやSSTPのヘッダ形式を参考に設計されており、以下の規則に従う：

- 全ての行はCR+LF（0x0D, 0x0A）で区切られる
- 1行目にはコマンド名とプロトコルバージョンを記載する
- 2行目以降は「ヘッダ名: 値」の形式で任意の数のヘッダが続く
- ヘッダ部の終端はCR+LFを2つ連続して配置（空行の追加）することで示す
- 文字エンコーディングはヘッダで指定された方式（一般的にはUTF-8かデフォルトのOEM codepage）に従う

## ライフサイクル関数

DLLロード時およびアンロード時に以下の関数がコールされる。

### loadu関数

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

モジュールの初期化を行う関数。<br />
第1引数のグローバルメモリにはモジュールのディレクトリパスが*UTF-8エンコーディング*で格納される。

SSP 2.6.92 (2025/1/16) より実装された。それより前はloadのみの実装である。

処理内容の例：

- 渡されたパスをカレントディレクトリとして、必要なデータファイルを読み込む
- モジュールの動作に必要なリソースを初期化する
- 必要に応じてログファイルやデータベースの初期化を行う

注意点：

- 文字列データが不要な場合でも、渡されたグローバルメモリは必ず解放する
- 初期化に成功した場合は TRUE を、失敗した場合は FALSE を返却する
- 本関数はベースウェアによって優先的に使用される

#### load関数

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

loadu関数の従来版。<br />
第1引数のモジュールディレクトリパスがデフォルトのOEM codepage（日本語環境ではCP932）でエンコードされている以外は、loadu関数と同じ仕様。

注意点：

- loadu関数が実装されていない場合のフォールバック先として使用される
- 互換性確保のため、loadとloaduの両方を実装し、loaduで初期化済の時にloadも呼ばれた場合は無視するのが望ましい
- Unicode対応のためには、受け取ったパスを適切にワイド文字列に変換する必要がある

#### unload関数

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

モジュールの終了処理を行う関数。モジュールのアンロード時にベースウェアから呼び出される。

実装すべき処理：

- CreateFile 等で開いたファイルハンドルを解放する
- CreateMutex 等で作成した同期オブジェクトを解放する
- CreateThread 等で作成したスレッドの終了を待機し、後処理を行う
- その他、モジュールが確保した全てのシステムリソースを解放する

戻り値は現在は使用されていないが、将来の拡張性を考慮して TRUE を返却することが望ましい。

## マルチインスタンス用関数（任意）

`load` / `request` / `unload` は、1 つの DLL につき 1 つのインスタンスしか持てない。1 つのプロセスで同じ DLL から複数のインスタンスを作りたいベースウェアのために、インスタンスを id で区別する次の関数を、**任意で**実装できる。実装しなくてもモジュールとして成立し、これらを呼ばないベースウェアでも従来どおり動く。

```
extern "C" __declspec(dllexport) long __cdecl multi_loadu(HGLOBAL h, long len);
extern "C" __declspec(dllexport) long __cdecl multi_load(HGLOBAL h, long len);
extern "C" __declspec(dllexport) BOOL __cdecl multi_unload(long id);
extern "C" __declspec(dllexport) HGLOBAL __cdecl multi_request(long id, HGLOBAL h, long *len);
```

- **multi_loadu / multi_load**: `loadu` / `load` と同じ引数で、新しいインスタンスを作る。モジュールのディレクトリパスの文字コードも `loadu`（UTF-8）と `load`（デフォルトの OEM codepage）のとおり。戻り値はそのインスタンスを指す id（1 以上の整数）で、失敗したときは `-1` を返すことが望ましい。ベースウェアは 0 以下の戻り値を失敗として扱う。メモリの解放も `loadu` / `load` と同じく、モジュールが行う
- **multi_unload**: id で指したインスタンスを終了する。戻り値は成功で TRUE、存在しない id では FALSE
- **multi_request**: id で指したインスタンスへ `request` と同じ形式のリクエストを渡す。存在しない id では NULL を返す

注意点：

- id の 0 は従来の `load` / `request` / `unload` が扱うインスタンスに割り当てられている。`multi_load*` が 0 を返してはならない
- 従来の関数とマルチインスタンス用の関数は、同じ DLL に両方実装できる。両者のインスタンスは別のものとして扱う
- YAYA の `multi_load*` は辞書の読み込みに失敗しても id を返す（`load` が常に TRUE を返すのと同じで、失敗の確認には `CI_check_failed` を使う）
- SSP はこれらの関数を使用しない（SSP 以外のベースウェア向けの仕様である）

## YAYA 固有の関数

次の関数は YAYA（`yaya.dll`）が独自に実装している。デバッグ用のチェックツールとの連携に使うもので、SHIORI の仕様には含まれない。他のモジュールが実装する必要はなく、ベースウェアも呼ばなくてよい。

!!! note "注"
    仕様は YAYA の都合で変わることがある。`multi_` 付きの関数は前節のマルチインスタンス用関数と同様に、id で指したインスタンスに対して動く。

### CI_check_failed関数

```
extern "C" __declspec(dllexport) BOOL __cdecl CI_check_failed(void);
extern "C" __declspec(dllexport) BOOL __cdecl multi_CI_check_failed(long id);
```

辞書の読み込みに失敗して、動作を抑止している状態、または緊急モードになっているときに TRUE を返す。存在しない id（`multi_` 版）や、`load` 前は FALSE を返す。

### Set_loghandler関数

```
extern "C" __declspec(dllexport) void __cdecl Set_loghandler(void (*loghandler)(const wchar_t *str, int mode, int id));
extern "C" __declspec(dllexport) void __cdecl multi_Set_loghandler(long id, void (*loghandler)(const wchar_t *str, int mode, int id));
```

YAYA のログを受け取るコールバック関数を登録する。登録するとログの出力が有効になる。`multi_` 版は `multi_load*` で作ったあとのインスタンスにだけ登録でき、存在しない id では何もしない。

コールバックの引数は次のとおり。

- **str**: ログの文字列（UTF-16）。`mode` が制御用の値のときは空文字列
- **mode**: ログの種別または制御の値
- **id**: ログのメッセージ番号（インスタンスの id ではない）

`mode` の値は次のとおり。

- **0**: 情報
- **1**: 致命的なエラー
- **2**: エラー
- **3**: 警告
- **4**: 注記
- **6**: ログの終了
- **16 / 17 / 32**: 以降のログのマルチバイト文字の文字コードの通知。16 が Shift_JIS、17 が UTF-8、32 が OS のデフォルト。ログの最初に 1 回呼ばれる

コールバックは `load` / `request` / `unload` を呼んだスレッドで呼ばれる。

### logsend関数

```
extern "C" __declspec(dllexport) BOOL __cdecl logsend(long hwnd);
```

Windows の DLL 版だけが持つ。ログを `WM_COPYDATA` で受け取るウィンドウのハンドル（HWND）を渡す。常に TRUE を返す。`Set_loghandler` でコールバックを登録しているときは、そちらが優先される。

`WM_COPYDATA` の `dwData` には `Set_loghandler` の `mode` と同じ値、`lpData` にはログの文字列（UTF-16、NUL 終端）が入る。
