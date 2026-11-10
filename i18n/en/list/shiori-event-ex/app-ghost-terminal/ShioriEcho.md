# ShioriEcho

**カテゴリ:** Interactive executable for ghost development “Ghost Terminal”

Event that occurs after a command is entered

- **Reference0**: Command collected by the terminal
- **戻り値**: If \`ShioriEcho.GetResult\` is not defined, you can return any value supported by \`ShioriEcho.GetResult\` here. These return values are handled correctly by the terminal (however, if you do not define \`ShioriEcho.GetResult\` and return nothing, return value 3 proceeds to retrieve the next command).<br />
  If \`ShioriEcho.GetResult\` is defined, the return value here is ignored (\*\*however, Sakura Script is executed normally\*\*).
