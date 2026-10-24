# OnExecuteHTTPFailure

**カテゴリ:** その他通信イベント

execute-httpで取得エラーした際に発生。ReferenceはCompleteと同じ。

\[2.8.90\] 同じURLの取得がすでに進行中の場合、後から出したリクエストは実行されずこのイベント(Reference4=downloading)が発生する。それ以前はタグが黙って無視されていた。

**対応:** SSP / Ninix
