# ShioriEcho.TabPress

**カテゴリ:** Interactive exe for ghost development "Ghost Terminal"

An event for completing a command with the Tab key.

- **Reference0**: Command collected by the terminal.
- **Reference1**: First character of the command at the cursor position when Tab is pressed (starting value is 0).
- **Reference2**: Number of consecutive Tab presses made by the user (starting value is 0).
- **Reference3**: First character of the command at the cursor position when Tab was first pressed in this series of tab completions (starting value is 0).
- **Return value (optional): X-SSTP-PassThru-Command**: Replace the command with this content.
- **Return value (optional): X-SSTP-PassThru-InsertIndex**: Move the cursor to this position (leave it unchanged if not provided).
- **Return value (optional): X-SSTP-PassThru-OldInsertIndex**: Update the subsequent \`Reference3\` to this content and keep it in effect until this series of tab completions ends (leave it unchanged if not provided).
