# ネットワーク更新イベントの発生順序

SSPの通常のネットワーク更新（ゴースト更新）でのイベント発生順序は以下の通り。

1. OnUpdateProcessExec　※メニューなどからの実行時のみ。スクリプトを返した場合、以降の標準の更新処理は行われない。

2. OnUpdateBegin

3. OnUpdateReady　※更新ファイルがあった場合のみ。更新ファイルが無い場合は、以降のイベントは飛ばして OnUpdateComplete（Reference0 が none）が発生する。

4. 更新ファイル1つごとに、以下を繰り返す。

   1. OnUpdate.OnDownloadBegin
   2. OnUpdate.OnMD5CompareBegin
   3. OnUpdate.OnMD5CompareComplete または OnUpdate.OnMD5CompareFailure<br />
      MD5が一致しなかった場合は、同じファイルについて OnUpdate.OnDownloadBegin からやり直す。リトライ回数を超えても一致しなかった場合は、OnUpdateFailure（md5 miss）となり、以降のファイルは処理されない。

5. 全ファイルの取得後、更新ファイルの置き換えとSHIORI・シェルなどの再読み込みを行ってから、OnUpdateComplete が発生する。したがって、OnUpdateComplete は再読み込み後のゴーストが受け取る。

- 途中で失敗（中断を含む）した場合は、その時点で OnUpdateFailure が発生して終了する。同じ更新で OnUpdateFailure と OnUpdateComplete の両方が発生することはない。
- OnUpdateReady・各ファイルの処理の後・置き換え前には、それまでに発生したイベントのスクリプトの再生が終わるまで待ってから次へ進む。そのため、これらのイベントでスクリプトを返すと、その再生が終わるまで更新は次の段階に進まない。
- OnUpdateReady のスクリプトの再生が終わり、ファイルの取得を始める時点で早送りキー（SSPの設定「早送りキーを有効にする」で指定したキー。標準では Ctrl）が押されていた場合、その更新では全てのファイルについて OnUpdate.OnDownloadBegin・OnUpdate.OnMD5Compare\* が発生しない（ファイルの取得とMD5の照合そのものは行われる）。OnUpdateBegin・OnUpdateReady・OnUpdateComplete・OnUpdateFailure は通常通り発生する。
- 自動更新（更新理由が auto）の場合、OnUpdateBegin は更新ファイルの有無が確認できた時点、つまり OnUpdateReady の直前に発生する。更新ファイルが無い場合と、更新ファイルの確認前に失敗した場合は、OnUpdateBegin・OnUpdateComplete・OnUpdateFailure のいずれも発生しない。
- 更新チェックのみ（ゴーストエクスプローラなどからのチェック）の場合、OnUpdateBegin・OnUpdateReady・OnUpdate.OnDownloadBegin・OnUpdate.OnMD5Compare\*・OnUpdateComplete・OnUpdateFailure は発生せず、代わりに OnUpdateCheckComplete または OnUpdateCheckFailure が発生する。
- ゴースト以外（シェル・バルーンなど）の更新では、上記のイベント名が OnUpdateOther〜（OnUpdateOtherBegin、OnUpdateOther.OnDownloadBegin など）に置き換わる。発生順序は同じ。

ゴースト本体・シェル・バルーンをまとめて更新する場合は、ゴースト → シェル → バルーン（→ 推奨バルーン）の順に、それぞれ上記の一連のイベントが発生する。全ての更新が終わった後に、最後に一度だけ OnUpdateResultEx が発生する。OnUpdateResultEx がスクリプトを返さなかった場合に限り、続けて OnUpdateResult が発生する。更新チェックのみの場合は、それぞれ OnUpdateCheckResultEx・OnUpdateCheckResult となる。
