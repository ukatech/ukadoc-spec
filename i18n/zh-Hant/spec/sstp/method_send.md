# Method: SEND

SEND is a method for sending Sakura Script or SHIORI events from an external application to a ghost and playing them back.<br />
SEND and NOTIFY are handled identically. There is no functional difference between them. The following specifications also apply to NOTIFY as-is.<br />
Both methods are available: specifying Sakura Script directly in the Script header, or sending an event in the Event header and obtaining a script in the SHIORI response.<br />
Event and Script can be used together. If the SHIORI response to the Event does not return a script, the script in the Script header is used as a fallback.<br />
If the target ghost is not specified, the currently running ghost is the target.

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

By specifying the IfGhost header multiple times and pairing it with the corresponding Script header, different scripts can be specified for each ghost.

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

- **Sender**: A common header, but the special value `Sender: First` can be used with SEND/NOTIFY. When specified, the ghost (sakura) that starts up on the first launch is the target.<br />
  If both Sender and User-Agent are omitted, the response is 400 Bad Request.
- **Script**: The Sakura Script to play.<br />
  When used together with the Event header, this is used as a fallback if the SHIORI response to the Event does not return a script.
- **Entry**: Entry data. Passed to SHIORI.
- **Event**: SHIORI event name. In SHIORI/3.0, this is handled as a specification of the ID header.
- **Reference\***: Event Reference headers. SHIORI performs only minimal processing, such as character encoding conversion, and passes them through as-is.
- **IfGhost**: Specify the ghost name in the format `\0` side name,`\1` side name to treat the immediately following Script header as exclusive to a particular ghost.<br />
  If a Script header occurs that is not immediately after an IfGhost, it is used as the default Script for when no IfGhost matches.<br />
  If omitted, the same Script header is played for all ghosts.<br />
  For detailed routing rules, see [Script routing using IfGhost](method_send.md#ifghostによるスクリプト振り分け) below.
- **Ghost**: Specify the target ghost by its name (the name in descript.txt).
- **Option**: Specify options for how Sakura Script executed through SSTP is handled.<br />
  Multiple options can be specified, separated by commas. In addition to common options (nodescript, notranslate, etc.), the following option flags can be used with SEND/NOTIFY.<br />
  nobreak : Queue without interrupting the currently playing script.<br />
  notify : Send the SHIORI event in notify mode (no response required). It is also forcibly handled as if the script had been [returned in a ValueNotify header](../shiori3/request.md). \[SSP 2.6.76\]

## Response-specific headers

- **Script**: The script that was actually played. Line breaks are removed.
- **SHIORI custom headers**: Headers included in the SHIORI response are passed through.

## Script routing using IfGhost

By specifying the IfGhost header multiple times and pairing it with the corresponding Script header, different scripts can be specified for each ghost.<br />
IfGhost and Script are paired according to their order of appearance. A Script written before the first IfGhost becomes the default script.

- **Name matching**: If IfGhost is in the format "`\0` side name,`\1` side name", both names must match.<br />
  If IfGhost contains only "`\0` side name", it is selected when the `\0` side name matches.<br />
  If neither matches, the default script is used. However, the default script is also not used if the ghost is configured to "reject SSTP when unspecified".
- **Treating as the default ghost**: The following names are treated as the default ghost (sakura), and their script also functions as the default script.<br />
  "さくら", "エミリ", "えみりぃ"
