# system.os.(キー)

**カテゴリ:** プロパティシステム

起動中のOSの情報。(キー)に入る文字列は以下の通り。

- **type**: OSの種類。Windows,MacOS,Darwin,Linux,Android,FreeBSD,ReactOSなど。Web上ランタイムなら"Web"。(歴史的経緯で値はTitleCase)
- **arch**: OSのアーキテクチャ。x86,x64,arm,arm64,ia64,risc-v,ppc,mips,loongarchなど。確定できない・アーキテクチャ非依存なら"unknown"
- **name**: OSの名前。例：Windows 11 22H2
- **version**: OSのカーネルバージョン。例：10.0。OSの呼称と食い違う場合がある点に注意。例：Windows 10も11も10.0になる。
- **build**: OSのビルド番号。例：22621
- **parenttype**: 何らかの互換OS/互換レイヤーで動作している場合はその種類。無い場合は空文字列。今のところ Wine か ReactOS 。
- **parentname**: 互換OS/互換レイヤーのホスト側（親側）OSの名前。無い場合は空文字列。例：Linux 5.19.0-23-generic
- **locale**: OSのUIロケール名。言語コードと国・地域コードを「-」で連結したもの。例：ja-JP （SSP 2.8.17 以降）
- **locale.language**: OSのUI言語コード(ISO 639)。例：ja （SSP 2.8.17 以降）
- **locale.country**: OSのUI国・地域コード(ISO 3166)。例：JP （SSP 2.8.17 以降）
- **timezone.offset**: 現在のタイムゾーンのUTCからのオフセット（分単位）。UTCに対して進んでいる地域では負の値になる。例：日本標準時なら-540 （SSP 2.8.17 以降）
- **dst**: 現在、夏時間（サマータイム）が適用されている場合は1、それ以外は0。 （SSP 2.8.17 以降）
- **uptime**: OS起動からの経過時間（秒）。 （SSP 2.8.17 以降）
- **unixtime**: 現在時刻のUNIX時間（1970-01-01 00:00:00 UTCからの経過秒数）。 （SSP 2.8.17 以降）
- **idletime**: 最後のユーザー入力（キーボード・マウス操作）からの経過時間（秒）。 （SSP 2.8.17 以降）

**対応:** SSP 2.6.26/27
