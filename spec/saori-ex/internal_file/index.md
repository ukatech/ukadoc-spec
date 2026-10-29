# internal_file

ファイルそのものを対象にする処理。（ファイルの中身をバイト列として読むだけの処理は、`internal_crypto`の`Digest` / `HMAC`の`--data-in=file`のように、それぞれの関数が受け付ける。）

## 一覧

- [MediaInfo](internal_file.MediaInfo.md)
- [ImageInfo](internal_file.ImageInfo.md)
- [IsMediaLoadable](internal_file.IsMediaLoadable.md)
- [IsImageLoadable](internal_file.IsImageLoadable.md)
- [CompressArchive](internal_file.CompressArchive.md)
- [ExtractArchive](internal_file.ExtractArchive.md)
- [MediaInfoを実装するベースウェア向けの注記](internal_file_impl.md)
