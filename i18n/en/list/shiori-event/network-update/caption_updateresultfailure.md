# Network update failure reasons

- **timeout**: A timeout occurred.
- **too slow**: *Not emitted by SSP, which reports timeout instead.* The connection is extremely slow.
- **md5 miss**: The MD5 did not match.
- **artificial**: The update was interrupted by user action.
- **404 etc.**: Failed with that status code.
- **fileio**: ※SSP only. Writing to the update target failed because there was insufficient space.
- **readonly**: ※SSP only. Writing to the update target failed because of a read-only flag. This occurs when a file or folder has a read-only flag.
- **virusdetect**: ※SSP only. A virus may have been detected in the data. \[2.5.15\]
- **toomanyredirect**: ※SSP only. Processing was aborted because there were too many redirects. \[2.5.15\]
- **executing**: ※SSP only. A duplicate launch was prevented because an update was already running. \[2.5.26\]
- **parse**: ※SSP only. The data was downloaded, but parsing it failed. This occurs with rss-get/rss-post and ical-get/ical-post.
- **downloading**: ※SSP only. A duplicate download was prevented because a download from the same URL was already in progress. This occurs with execute-http/rss/ical. \[2.8.90\]
- **paramerror**: ※SSP only. The update could not be run because the update execution tag was configured incorrectly. \[2.5.26\]
