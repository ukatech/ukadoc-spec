# Overview

This is the specification for update definition files used by the ghost update system (network update).<br />
Update definition files record a list of files that make up a ghost and their hash values. The baseware retrieves this file from the server, compares it with local files, and performs a differential update.

The following two formats are currently valid. The old-format updates.dau (Version 1) is deprecated and omitted.

- **updates2.dau (Version 2)**: A binary-oriented format using byte value 1 as a delimiter.
- **updates.txt (Version 3)**: A text format using byte value 1 as a delimiter and with line prefixes.
