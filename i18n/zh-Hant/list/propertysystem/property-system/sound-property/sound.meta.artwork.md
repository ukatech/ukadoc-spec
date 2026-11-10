# meta.artwork

**カテゴリ:** Property System \> Sound Property Names

Image file path of the target media's album artwork.<br />
\[2.9.32\] SSP retrieves ID3 images, FLAC PICTURE blocks, and Ogg (Vorbis / Opus) METADATA_BLOCK_PICTURE itself. If there are multiple images, it prioritizes the cover (front cover); if there is no cover, it uses the first image. Other formats (such as MP4) are retrieved from the OS.<br />
See [here](sound.meta.artwork.note.md) for behavior when there are no tags or retrieval fails.

**対応:** SSP 2.8.73
