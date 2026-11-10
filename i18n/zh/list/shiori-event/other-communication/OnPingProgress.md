# OnPingProgress

**カテゴリ:** Other communication events

Triggered while ping is running via `\![execute,ping]`.

- **Reference0**: The exact string specified by --event
- **Reference1**: Source address \[`\1`\] total number of sends \[`\1`\] number of successes \[`\1`\] number of failures \[`\1`\] are separated by byte value 1
- **Reference2**: “OK” or error information \[`\1`\] responding address \[`\1`\] RTT (round-trip time in ms) \[`\1`\] are separated by byte value 1<br />
  From Reference2 onward, information for each sent Ping is recorded. For Progress, it is incomplete.<br />
  See [Status header of ICMP_ECHO_REPLY Structure](http://msdn.microsoft.com/en-us/library/aa366053%28v=vs.85%29.aspx) for error information.

**対応:** SSP
