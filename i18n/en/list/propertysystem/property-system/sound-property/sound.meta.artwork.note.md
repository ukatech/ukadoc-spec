# Metadata for Sound Properties (meta.～) \[2.8.73\]

Sound properties that begin with meta. retrieve tag information embedded in media files (ID3, Vorbis Comment, MP4 metadata atoms, ASF attributes, etc.). All are read-only.

**If tags are missing or cannot be retrieved for any reason, the property itself is treated as nonexistent.** Unlike [error](sound.error.md), which returns an empty string, referencing the property itself fails (the behavior is the same as specifying a nonexistent property name). When handling media that may or may not have tags, write scripts with this in mind.

Naturally, all meta. properties fail to be retrieved for formats that do not have tags.

\[2.9.32\] SSP reads tags for ID3 (v1 / v2.2 / v2.3 / v2.4) in MP3 and other formats, comments in FLAC・Ogg Vorbis・Opus, and INFO in WAV・AVI (including WAV id3 chunks) itself, without relying on the OS. This allows it to read tags that the OS may misread (such as Shift_JIS and ISO-8859-1 tags interpreted using the OS's default character encoding, ID3v2 tags with unsynchronisation or extended headers, ID3v2.2, and WAV tags). Items SSP cannot read, as well as other formats (such as MP4・WMA), continue to be retrieved from the OS.<br />
For tags with no specified character encoding (ID3v1, ID3v2 ISO-8859-1, and WAV・AVI INFO), SSP tries to determine the encoding in this order: UTF-8 → Shift_JIS → the OS's default character encoding. Since this is an estimate, especially on operating systems that are not Japanese, Western European and Japanese text may be mistaken for one another.<br />
Retrieval is now performed per item: SSP reads the tags first, and only items it cannot read are supplemented by the OS or media playback components. Therefore, even if only some items can be retrieved from a tag, the remaining items may be supplemented by the OS or media playback components (as a result, in some environments, the artist value may be used when the tags have no album artist).
