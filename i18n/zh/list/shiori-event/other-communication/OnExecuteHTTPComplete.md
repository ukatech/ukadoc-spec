# OnExecuteHTTPComplete

**カテゴリ:** Other communication events

Occurs when execute-http completes retrieval successfully.

- **Reference0**: One of post/get/head/put/delete
- **Reference1**: The string specified with the --sync or --async option.
- **Reference2**: The target URL.
- **Reference3**: If the --nofile option is present, the retrieved data. However, newline characters are replaced with byte value 1.<br />
  Otherwise, the full path of the retrieved file.
- **Reference4**: Retrieval result code (timeout|fileio|200|204|403|404), etc. See also [\[failure reasons\]](../network-update/caption_updateresultfailure.md).
- **Reference5**: Cookie string.
- **Reference6**: All response headers received. Separated by byte value 1 instead of newlines. \[2.6.40\]

**対応:** SSP / Ninix
