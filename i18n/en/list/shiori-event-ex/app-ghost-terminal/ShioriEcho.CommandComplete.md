# ShioriEcho.CommandComplete

**カテゴリ:** Interactive exe for ghost development "Ghost Terminal"

Event triggered when the user presses \`→\` at the right end of the command line

- **Reference0**: Command collected by the terminal
- **Reference1**: First character of the command at the cursor position when \`→\` is pressed (starting value is 0).
- **Return value (optional): X-SSTP-PassThru-Command**: Replace the command with this content.<br />
  The ghost can use this event to autocomplete commands.
- **Return value (optional): X-SSTP-PassThru-InsertIndex**: Move the cursor to this position (leave it unchanged if not provided).
