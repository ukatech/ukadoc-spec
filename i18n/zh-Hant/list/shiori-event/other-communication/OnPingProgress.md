# OnPingProgress

**カテゴリ:** Other communication events

Occurs while ping is running with `\![execute,ping]`.

- **Reference0**: The exact string specified with --event
- **Reference1**: Source address \[`\1`\] total number sent \[`\1`\] number successful \[`\1`\] number failed \[`\1`\] are separated by byte value 1
- **Reference2**: "OK" or error information \[`\1`\] responding address \[`\1`\] RTT (round-trip time in ms) \[`\1`\] are separated by byte value 1<br />
  Starting at Reference2, information for each Ping sent is recorded. For Progress, the information is incomplete.<br />
  For error information, see the [Status header of the ICMP_ECHO_REPLY Structure](http://msdn.microsoft.com/en-us/library/aa366053%28v=vs.85%29.aspx).

**対応:** SSP
