# Overview

This is the specification for update definition files used by the ghost update system (network update).<br />
Update definition files contain a list of the files that make up a ghost and their hash values. The baseware retrieves the file from the server, compares it with local files, and performs a differential update.

There are currently two valid formats. The legacy format, updates.dau (Version 1), has been deprecated and is omitted.

- **updates2.dau (Version 2)**: A binary-oriented format delimited by byte value 1.
- **updates.txt (Version 3)**: A text format delimited by byte value 1, with line prefixes.
