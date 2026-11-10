# Path Handling

- **URL encoding**: If all entries are percent-encoded, they are decoded before use. Otherwise, only the URL side is encoded.

- **Security checks**: Entries that meet any of the following conditions are treated as invalid.

  - No MD5.
  - Ends in `/` or `\` (directory entry).
  - Contains `..\` or `../` (to prevent directory traversal).
