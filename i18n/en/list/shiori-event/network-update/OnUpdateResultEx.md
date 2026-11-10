# OnUpdateResultEx

**カテゴリ:** Network update event

Occurs when a network update is run and reports all update results together, including the bulk balloon and shell update feature.

- **Reference\***: The update results are included in the following format, in the order in which the updates were run (`\1` is byte value 1)

  (※1)\[`\1`\](※2)\[`\1`\](※3)\[`\1`\](※4)\[`\1`\](※5)<br />
  or<br />
  (※1)\[`\1`\](※2)\[`\1`\](※3)\[`\1`\](※4)

  - ※1……Name of the network update target
  - ※2……[Type of network update target](caption_updatetype.md)
  - ※3……"OK" on success, "NG" on failure
  - ※4……Number of updated files on success (0 if there are no update files=none); [reason for failure](caption_updateresultfailure.md) on failure.
  - ※5……If the update failed and the file that caused the failure is known, its name.

**対応:** SSP
