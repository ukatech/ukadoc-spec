# currentghost.sound(要素名).サウンドプロパティ名

**カテゴリ:** プロパティシステム

現在のゴーストが管理しているメディアのうち、要素名が一致する最も新しいものから情報を取得。<br />
要素名は`\![sound,play,～]`などで指定したファイル名/パス/URLそのもの。<br />
ドットを挟まず括弧を直接続けることに注意（`currentghost.sound(～)`であって`currentghost.sound.(～)`ではない）。<br />
サウンドプロパティ名は[後述](sound-property/sound.name.md)。書き込みが可能なものと、その際の注意点については[こちら](sound-property/notes_sound_propertyset.md)。

**対応:** SSP 2.8.72
