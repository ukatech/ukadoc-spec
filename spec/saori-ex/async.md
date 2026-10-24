# 非同期の呼び出し

内蔵モジュール（名前が`internal_`で始まるもの）の関数は、オプション`--async=識別子`を付けると非同期で動きます。要求を受け付けると、応答はすぐに204で返り、結果はあとで呼び出し元のゴーストへイベントで届きます。<br />
ゴーストなしの呼び出しでは使えません（400 `ghost required`）。識別子が空なら400（`invalid parameter`）です。<br />
時間のかかる処理（大きなファイルのハッシュ、パスワードのハッシュ、鍵の導出、RSAの鍵ペアの生成など）には`--async`を使ってください。<br />
同時に動く非同期の呼び出しは、SSPではCPUの数ほど（2～4）までです。それを超えた分は、前のものが終わるまで順番を待ちます。

## 結果を届けるイベント

- **イベント名**: 識別子が`On`で始まれば、成功時はその名前、失敗時は「識別子＋`Failure`」。<br />
  そうでなければ、成功時は[OnInternalSaoriComplete](../../list/shiori-event/other/OnInternalSaoriComplete.md)、失敗時は[OnInternalSaoriFailure](../../list/shiori-event/other/OnInternalSaoriFailure.md)。
- **成功時のReference**: Reference0＝識別子、Reference1＝結果（同期の呼び出しの`Result`）、Reference2＝モジュール名、Reference3＝関数名、Reference4以降＝`Value0`以降。
- **失敗時のReference**: Reference0＝識別子、Reference1＝失敗理由（同期の呼び出しの`ErrorDescription`と同じ文字列）、Reference2＝モジュール名、Reference3＝関数名。

引数の数やオプションの名前の誤りは、受付の時点で400になります。引数の中身の誤り（読めない16進など）は、失敗のイベントで届きます。<br />
結果が届く前に呼び出し元のゴーストが終了した場合（SHIORIの再読み込みを含む）、結果は届きません。
