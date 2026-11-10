# Field details

These are the field definitions common to the `file,` lines in updates2.dau and updates.txt.

- **Required fields**:

  - **File path (position \[0\])**: Relative path to the file to be updated. Uses forward slashes (`/`) as separators.
  - **MD5 hash (position \[1\])**: MD5 hash of the file contents. A 32-character hexadecimal string.

- **Extension fields (position \[2\] and later)**: Written in `key=value` format. All are optional.

  - **size=number**: File size in bytes.
  - **date=string**: Date and time string in ISO 8601 format. Example: `2024-01-15T12:34:56`
  - **charset=string**: Charset name. Appended only to the end of the first entry in updates2.dau. Used only to determine the charset; ignored when loading the file as a definition file.
