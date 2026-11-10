# ShioriEcho.Begin

**カテゴリ:** Interactive exe for ghost development "Ghost Terminal"

ghost_terminal event triggered when this ghost starts

- **Reference0**: Terminal version
- **Reference1**: Terminal session type<br />
  If the terminal starts with \`-s\`, the value is \`SakuraScript\`.<br />
  If the terminal starts with \`-c\`, the value is \`Command\`.<br />
  If the terminal starts in common mode, the value is \`Common\`.
- **Return value: X-SSTP-PassThru-Tittle (optional)**: Set the terminal title
- **Return value: X-SSTP-PassThru-Icon (optional)**: Set the terminal icon
- **Return value: X-SSTP-PassThru-SmallIcon (optional)**: Set the terminal's small icon<br />
  If not set, it matches \`X-SSTP-PassThru-Icon\`
- **Return value: X-SSTP-PassThru-CustomLoginInfo (optional)**: If set, the terminal does not display the default login information, and this<br />
  This return value is simply escaped:<br />
  \- \``\n`\` is converted to a line break.<br />
  \- \``\t`\` is converted to a tab.<br />
  \- \`\\\\\` is converted to \`\\\`.
