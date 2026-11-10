# OnPingComplete

**カテゴリ:** Other communication events

Occurs when the specified number of pings initiated by `\![execute,ping]` have completed.

- **Reference0**: The exact string specified by --event
- **Reference1**: Source address \[`\1`\] total number of sends \[`\1`\] number of successes \[`\1`\] number of failures \[`\1`\] are byte value 1
- **Reference2**: “OK” or error information \[`\1`\] reply address \[`\1`\] RTT (time taken for the round trip, in ms) \[`\1`\] are byte value 1<br />
  From Reference2 onward, information for each sent Ping is recorded. In the case of Progress, the information is incomplete.<br />
  For error information, see the [Status header of the ICMP_ECHO_REPLY Structure](http://msdn.microsoft.com/en-us/library/aa366053%28v=vs.85%29.aspx).

**対応:** SSP
