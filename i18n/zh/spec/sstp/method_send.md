# Method: SEND

SEND is a method for sending Sakura Script or SHIORI events from an external application to a ghost and playing them back.<br />
SEND and NOTIFY are handled identically. There is no functional difference between them. The following specifications also apply to NOTIFY as-is.<br />
Both methods are available: specifying Sakura Script directly in the Script header, and sending an event in the Event header to obtain a script in the SHIORI response.<br />
Event and Script can be used together. If the SHIORI response to Event does not return a script, the script in the Script header is used as a fallback.<br />
If no target ghost is specified, the currently running ghost is targeted.

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

## Event + fallback script sample

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnCustomEvent
Reference0: data
Script: \h\s[0]イベント未対応時のスクリプト\e
```

By specifying multiple IfGhost headers and pairing them with the corresponding Script headers, you can specify a different script for each ghost.

## Sample routing by IfGhost

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

## Headers specific to the request

- **Sender**: This is a common header, but the special value `Sender: First` can be used with SEND/NOTIFY. When specified, the ghost from the first startup (sakura) is targeted.<br />
  If both Sender and User-Agent are unspecified, the result is 400 Bad Request.
- **Script**: The Sakura Script to play.<br />
  When used with the Event header, this is used as a fallback if the SHIORI response to Event does not return a script.
- **Entry**: Entry data. Passed to SHIORI.
- **Event**: SHIORI event name. In SHIORI/3.0, this is handled as the value of the ID header.
- **Reference\***: Event Reference headers. They are passed through to SHIORI after only minimal processing, such as character encoding conversion.
- **IfGhost**: When a ghost name is specified in the format `\0`側名,`\1`側名, the immediately following Script header is handled as specific to that ghost.<br />
  If a Script header exists that does not immediately follow IfGhost, it is used as the default Script when no IfGhost matches.<br />
  If omitted, the same Script header is played for all ghosts.<br />
  For detailed routing rules, see [Script routing by IfGhost](method_send.md#ifghostによるスクリプト振り分け).
- **Ghost**: Specifies the target ghost by its name (the name in descript.txt).
- **Option**: Specifies options for how Sakura Script executed via SSTP is handled.<br />
  Multiple options can be specified, separated by commas. In addition to common options (nodescript, notranslate, etc.), the following option flags can be used with SEND/NOTIFY.<br />
  nobreak : Queue the script without interrupting the currently playing script.<br />
  notify : Send the SHIORI event in notify mode (no response required). It is also forcibly handled as if the script had been [returned in a ValueNotify header](../shiori3/request.md). \[SSP 2.6.76\]

## Headers specific to the response

- **Script**: The script that was actually played. Line breaks are removed.
- **SHIORI custom headers**: Headers included in the SHIORI response are passed through.

## Script routing by IfGhost

By specifying multiple IfGhost headers and pairing them with the corresponding Script headers, you can specify a different script for each ghost.<br />
IfGhost and Script are paired in order of appearance. A Script written before the first IfGhost becomes the default script.

- **Name matching**: If IfGhost is in the format 「`\0`側名,`\1`側名」, both names must match.<br />
  If IfGhost contains only `\0`側名, selection is based only on whether the `\0`側名 matches.<br />
  If neither matches, the default script is used. However, if the ghost has the “Reject unspecified SSTP” setting enabled, the default script is not used either.
- **Handling as the default ghost**: The following names are treated as the default ghost (sakura), and their script also serves as the default script.<br />
  「さくら」「エミリ」「えみりぃ」
