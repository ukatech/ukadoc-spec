# meta.artwork

**カテゴリ:** プロパティシステム \> サウンドプロパティ名

目标媒体专辑封面图像文件的路径。<br />
\[2.9.32\] 对于 ID3 图像、FLAC 的 PICTURE 块、Ogg（Vorbis / Opus）的 METADATA_BLOCK_PICTURE，SSP 会自行提取。有多张图像时优先使用封面（正面封面），没有封面时使用第一张。其他格式（如 MP4）则从 OS 获取。<br />
没有标签或无法获取时的行为请参见[此处](sound.meta.artwork.note.md)。

**対応:** SSP 2.8.73
