# `\![set,syncobject,同期オブジェクト名]`

**カテゴリ:** ウエイトコマンド

指定した名前つき同期オブジェクトをシグナル状態にする(活性化)。<br />
SemaphoreはReleaseSemaphoreで1加算、EventはSetEvent、WaitableTimerは即座にシグナル状態にする。<br />
所有していないMutexのsetは意味をなさないため無視される。

**対応:** SSP 2.8.28
