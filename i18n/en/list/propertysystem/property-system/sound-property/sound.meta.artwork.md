# meta.artwork

**カテゴリ:** Property System \> Sound Property Names

The file path of the target media's album artwork image.<br />
\[2.9.32\] SSP reads ID3 images, FLAC PICTURE blocks, and Ogg (Vorbis / Opus) METADATA_BLOCK_PICTURE itself. If there are multiple images, the front cover takes priority; if there is no front cover, the first image is used. Other formats (such as MP4) are retrieved from the OS.<br />
See [here](sound.meta.artwork.note.md) for behavior when tags are missing or cannot be retrieved.

**対応:** SSP 2.8.73
