# `\![wait,syncobject,同期オブジェクト名,オプション]`

**カテゴリ:** ウエイトコマンド

指定した名前つき同期オブジェクト(Windows上の場合はMutex,Semaphore,Event,WaitableTimer(2.8.28から))がシグナル状態になるまで待機する。<br />
Mutexは待機後解放、Semaphoreは待機後1解放、Event及びWaitableTimerは取得後特に何も操作しない。

以下のオプションを指定できる。

- 数値 もしくは --timeout=数値……タイムアウト時間。省略または0で(スクリプトブレークされるまで)無限待機、1以上を指定すると指定ミリ秒間待機。
- --reset=0 or 1……待機直後にmutexとsemaphoreをreleaseするかどうか。1でリリースする（デフォルト）、0でリリースしない。

**対応:** SSP
