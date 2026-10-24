# OnMusicPlayEx

**カテゴリ:** その他イベント

Windows標準のメディアプレイヤーアプリなど、対応した音楽再生ソフトで再生中の曲情報をゴーストに通知する。<br />
このイベントに反応しない場合はOnMusicPlayにフォールバックする。<br />
ブラウザでの動画・音楽再生は全部OnVideoPlayEx扱いになるので注意。

- **Reference0**: 曲タイトル
- **Reference1**: アーティスト名
- **Reference2以降**: 拡張情報名\[バイト値1\]拡張情報の内容 [OnMusicPlayExの拡張情報リスト](caption_musicplayex_codes.md)

**対応:** SSP 2.7.55
