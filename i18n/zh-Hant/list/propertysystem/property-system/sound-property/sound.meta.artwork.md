# meta.artwork

**カテゴリ:** 屬性系統 \> 音效屬性名稱

目標媒體的專輯封面圖片檔案路徑。<br />
\[2.9.32\] SSP 會自行讀取 ID3 圖片、FLAC 的 PICTURE 區塊、Ogg（Vorbis / Opus）的 METADATA_BLOCK_PICTURE。若有多張圖片，會優先使用封面（正面封面）；若沒有封面，則使用第一張圖片。其他格式（例如 MP4）則從 OS 取得。<br />
沒有標籤或無法取得時的行為請參閱[此處](sound.meta.artwork.note.md)。

**対応:** SSP 2.8.73
