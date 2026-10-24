# `\![reset,syncobject,同期オブジェクト名]`

**カテゴリ:** ウエイトコマンド

指定した名前つき同期オブジェクトを非シグナル状態にする(非活性化)。<br />
EventはResetEvent、WaitableTimerはCancelWaitableTimerで非シグナル状態にする。<br />
Semaphore及びMutexに対するresetは意味をなさないため無視される。

**対応:** SSP 2.8.28
