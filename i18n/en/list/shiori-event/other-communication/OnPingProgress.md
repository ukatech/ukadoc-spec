# OnPingProgress

**カテゴリ:** Other communication events

Occurs while a ping is in progress with `\![execute,ping]`.

- **Reference0**: Exact string specified with --event
- **Reference1**: Source address \[`\1`\] total number of transmissions \[`\1`\] number of successes \[`\1`\] number of failures \[`\1`\] are separated by byte value 1
- **Reference2**: "OK" or error information \[`\1`\] responding address \[`\1`\] RTT (round-trip time in ms) \[`\1`\] are separated by byte value 1<br />
  Starting with Reference2, information for each Ping sent is recorded. This is incomplete for Progress.<br />
  For error information, see the Status header in the [ICMP_ECHO_REPLY Structure](http://msdn.microsoft.com/en-us/library/aa366053%28v=vs.85%29.aspx).

**対応:** SSP
