# About Sound Property Metadata (meta.～) \[2.8.73\]

Sound properties that begin with meta. retrieve tag information embedded in media files (such as ID3, Vorbis Comment, MP4 metadata atoms, and ASF attributes). All are read-only.

**If a tag does not exist or cannot be retrieved for some reason, the property itself is treated as nonexistent.** Note that, unlike [error](sound.error.md), which returns an empty string, referencing the property itself fails (the behavior is the same as when a nonexistent property name is specified). When handling media whose tags may or may not exist, write your scripts with this in mind.

Naturally, all meta. properties fail to be retrieved for formats that do not have tags.

\[2.9.32\] For tags in ID3 (v1 / v2.2 / v2.3 / v2.4) for MP3 and other formats, comments in FLAC, Ogg Vorbis, and Opus, and INFO in WAV and AVI (including WAV id3 chunks), SSP reads the tags itself without relying on the OS. This also allows it to read tags that the OS misreads, such as Shift_JIS or ISO-8859-1 tags interpreted using the OS's default character encoding, ID3v2 tags with unsynchronisation or extended headers, ID3v2.2, and WAV tags. Items SSP cannot read, as well as other formats (such as MP4 and WMA), are still retrieved from the OS as before.<br />
For tags with no specified character encoding (ID3v1, ISO-8859-1 in ID3v2, and INFO in WAV and AVI), SSP guesses the encoding in this order: UTF-8 → Shift_JIS → the OS's default character encoding. Since this is an estimate, especially on operating systems that are not Japanese, Western-language text and Japanese may be mistaken for one another.<br />
Retrieval is now performed per item: SSP reads the tags first, and only items it could not read are supplemented by the OS or media playback components. As a result, even if only some items are retrieved from a tag, the remaining items may be supplemented by the OS or media playback components (for example, in some environments, the artist value is used to supplement a tag that has no album artist).
