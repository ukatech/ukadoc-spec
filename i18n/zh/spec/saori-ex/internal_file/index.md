# internal_file

对文件本身进行处理。（仅将文件内容作为字节串读取的处理，可由各个函数分别支持，例如`internal_crypto`的`Digest` / `HMAC`的`--data-in=file`。）

## 一覧

- [MediaInfo](internal_file.MediaInfo.md)
- [ImageInfo](internal_file.ImageInfo.md)
- [IsMediaLoadable](internal_file.IsMediaLoadable.md)
- [IsImageLoadable](internal_file.IsImageLoadable.md)
- [CompressArchive](internal_file.CompressArchive.md)
- [ExtractArchive](internal_file.ExtractArchive.md)
- [MediaInfo 的 baseware 实现说明](internal_file_impl.md)
