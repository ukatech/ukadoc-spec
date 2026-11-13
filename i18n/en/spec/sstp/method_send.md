# Method: SEND

SEND is a method for sending Sakura Script or SHIORI events from an external application to a ghost for playback.<br />
SEND and NOTIFY are handled identically. There is no functional difference between them. The following specifications also apply to NOTIFY.<br />
Both specifying Sakura Script directly in the Script header and sending an event in the Event header to obtain a script from the SHIORI response are supported.<br />
Event and Script can be used together. If the SHIORI response to the Event does not return a script, the script in the Script header is used as a fallback.<br />
If no target ghost is specified, the currently running ghost is targeted.

## Basic script playback example

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\w5\u\s[10]ご機嫌いかが？\e
```

## Event sending example

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnExternalEvent
Reference0: param1
Reference1: param2
```

## Event with fallback script example

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnCustomEvent
Reference0: data
Script: \h\s[0]イベント未対応時のスクリプト\e
```

By specifying multiple IfGhost headers and pairing them with corresponding Script headers, different scripts can be specified for each ghost.

## IfGhost routing example

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\e
IfGhost: まゆら
Script: \h\s[0]まゆらさん、こんにちは。\e
IfGhost: 花ちゃん,妹
Script: \h\s[0]花ちゃんと妹さん、こんにちは。\e
```

## Interruption suppression example

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]割り込まないで追加。\e
Option: nobreak
```

## Request-specific headers

- **Sender**: A common header, but `Sender: First` can be used as a special value for SEND/NOTIFY. When specified, it targets the ghost (sakura) from the first startup.<br />
  If neither Sender nor User-Agent is specified, a 400 Bad Request is returned.
- **Script**: The Sakura Script to play.<br />
  When used with the Event header, it is used as a fallback if the SHIORI response to the Event does not return a script.
- **Entry**: Entry data. It is passed to SHIORI.
- **Event**: The SHIORI event name. In SHIORI/3.0, it is treated as the ID header.
- **Reference\***: The event's Reference header. It is passed to SHIORI as is, after minimal processing such as character encoding conversion.
- **IfGhost**: When ghost names are specified in the format `\0` side name,`\1` side name, the immediately following Script header is treated as exclusive to that ghost.<br />
  A Script header that does not immediately follow an IfGhost header is used as the default script when no IfGhost matches.<br />
  \[SSP 2.9.35\] A ghost's [UUID](../../list/propertysystem/property-system/general-property/uuid.md) can also be specified instead of names (in UUID form, without a comma). This allows ghosts with the same names to be distinguished.<br />
  If omitted, the same Script header is played for every ghost.<br />
  For detailed routing rules, see [Script routing with IfGhost](method_send.md#ifghostによるスクリプト振り分け) below.
- **Ghost**: Specifies the target ghost by its ghost name (name in descript.txt).
- **Option**: Specifies options for how Sakura Script executed via SSTP is handled.<br />
  Multiple options can be specified, separated by commas. In addition to common options (nodescript, notranslate, etc.), the following option flags can be used with SEND/NOTIFY.<br />
  nobreak : Queues the script without interrupting the script currently playing.<br />
  notify : Sends the SHIORI event in notify mode (no response required). The script is also forcibly handled in the same way as when [returned in a ValueNotify header](../shiori3/request.md). \[SSP 2.6.76\]

## Response-specific headers

- **Script**: The script that was actually played. Line breaks are removed.
- **SHIORI custom headers**: Headers included in the SHIORI response are passed through.

## Script routing with IfGhost

By specifying multiple IfGhost headers and pairing them with corresponding Script headers, different scripts can be specified for each ghost.<br />
IfGhost and Script headers are paired in order of appearance. A Script specified before the first IfGhost becomes the default script.

- **Name matching**: If IfGhost is in the format "`\0` side name,`\1` side name", both names must match.<br />
  If IfGhost contains only the "`\0` side name", the script is selected based on a match of the `\0` side name alone.<br />
  \[SSP 2.9.35\] If IfGhost is in UUID form (22 base64 characters and `==`), the script is selected by matching the ghost's UUID rather than its names. If multiple ghosts with the same UUID are running, the displayed ghost takes priority.<br />
  If none match, the default script is used. However, if the ghost is configured to reject unspecified SSTP, the default script is not used either.
- **Default ghost handling**: The following names are treated as the default ghost (sakura), and their scripts also function as default scripts.<br />
  "さくら", "エミリ", "えみりぃ"
