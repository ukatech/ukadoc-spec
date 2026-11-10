# ShioriEcho.GetResult

**カテゴリ:** Interactive exe for ghost development "Ghost Terminal"

Value result event query

Replyable header 1:

- **Return value: X-SSTP-PassThru-Result**: Display the content and proceed to retrieve the next command.
- **Return value (optional): X-SSTP-PassThru-Type**: Additional information: value type

Replyable header 2:

- **Return value: X-SSTP-PassThru-Special**: Display the content and proceed to retrieve the next command.<br />
  This return value is simply escaped:<br />
  \- \``\n`\` is converted to a line break.<br />
  \- \``\t`\` is converted to a tab.<br />
  \- \`\\\\\` is converted to \`\\\`.

Replyable header 3: Empty

Wait 1 second and retry ShioriEcho.GetResult.

Other

- **Return value: X-SSTP-PassThru-Status**: This return value can be combined with the return values above<br />
  If it is \`End\`, the terminal exits.<br />
  If it is \`Continue\`, the terminal displays nothing and proceeds to retrieve the next command.
