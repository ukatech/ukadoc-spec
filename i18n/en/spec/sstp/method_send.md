# Method: SEND

SEND is a method for sending Sakura Script or SHIORI events from an external application to a ghost and having them played.<br />
SEND and NOTIFY are treated as the same operation. They have no functional differences. The following specifications also apply to NOTIFY as is.<br />
Both the method of specifying Sakura Script directly in the Script header and the method of sending an event in the Event header and obtaining a script in the SHIORI response can be used.<br />
Event and Script can be used together. If the SHIORI response to Event does not return a script, the script in the Script header is used as a fallback.<br />
If the target ghost is not specified, the currently running ghost is targeted.

## Basic script playback sample

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\w5\u\s[10]ご機嫌いかが？\e
```

## Event sending sample

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnExternalEvent
Reference0: param1
Reference1: param2
```

## Event and fallback script sample

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnCustomEvent
Reference0: data
Script: \h\s[0]イベント未対応時のスクリプト\e
```

By specifying the IfGhost header multiple times and pairing each with the corresponding Script header, different scripts can be specified for each ghost.

## Routing sample using IfGhost

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

## Sample with interruption suppression

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]割り込まないで追加。\e
Option: nobreak
```

## Request-specific headers

- **Sender**: A common header, but `Sender: First` can be used as a special value in SEND/NOTIFY. When specified, the ghost that starts on the first launch (sakura) is targeted.<br />
  If both Sender and User-Agent are unspecified, the response is 400 Bad Request.
- **Script**: The Sakura Script to play.<br />
  When used together with the Event header, this is used as a fallback if the SHIORI response to Event does not return a script.
- **Entry**: Entry data. It is passed to SHIORI.
- **Event**: The SHIORI event name. In SHIORI/3.0, it is treated as the value of the ID header.
- **Reference\***: The event's Reference headers. They are passed through to SHIORI as is, after only minimal processing such as character encoding conversion.
- **IfGhost**: Specifies a ghost name in the format `\0` side name,`\1` side name. The Script header immediately following it is treated as intended for a specific ghost.<br />
  If a Script header appears that is not immediately after IfGhost, it becomes the default Script used when IfGhost does not match.<br />
  If omitted, the same Script header is played for all ghosts.<br />
  For details on the routing rules, see [Routing scripts using IfGhost](method_send.md#ifghostによるスクリプト振り分け).
- **Ghost**: Specifies the target ghost by name (the name in descript.txt).
- **Option**: Specifies how the Sakura Script executed by SSTP is handled.<br />
  Multiple options can be specified, separated by commas. In addition to common options (nodescript, notranslate, etc.), the following option flags can be used with SEND/NOTIFY.<br />
  nobreak : Queue the script without interrupting the currently playing script.<br />
  notify : Send the SHIORI event in notify mode (no response required). Also, it is forcibly handled in the same way as when a script is [returned in a ValueNotify header](../shiori3/request.md). \[SSP 2.6.76\]

## Response-specific headers

- **Script**: The script that was actually played. Line breaks are removed.
- **SHIORI custom headers**: Headers included in the SHIORI response are passed through.

## Script routing using IfGhost

By specifying the IfGhost header multiple times and pairing each with the corresponding Script header, different scripts can be specified for each ghost.<br />
IfGhost and Script are paired in the order they appear. A Script written before the first IfGhost becomes the default script.

- **Name matching**: If IfGhost is in the format “`\0` side name,`\1` side name”, both names must match.<br />
  If IfGhost contains only “`\0` side name”, it is selected when only the `\0` side name matches.<br />
  If neither matches, the default script is used. However, the default script is not used if the ghost is configured to “reject unspecified SSTP”.
- **Treating as the default ghost**: The following names are treated as the default ghost (sakura), and their script also functions as the default script.<br />
  “さくら”, “エミリ”, “えみりぃ”
