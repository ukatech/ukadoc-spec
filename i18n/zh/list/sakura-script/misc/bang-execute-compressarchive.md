# `\![execute,compressarchive,ファイル名,ディレクトリ名,オプション...]`

**カテゴリ:** 未分类命令

压缩ZIP文件。建议使用完整路径指定。使用相对路径时，会解释为相对于ghost/master/的路径。<br />
选项如下。

- --event=事件标识符……指定事件标识符后，会在继续执行Sakura Script的同时进行压缩，并在完成后触发事件。如果标识符以On开头，则触发该标识符对应的事件；否则触发OnCompressArchiveComplete或OnCompressArchiveFailure。省略时，脚本执行会暂停，直至处理完成。
- --password=密码……启用AES加密ZIP，并使用指定的密码。

有关处理完成后触发的事件的规范，请参阅[OnCompressArchiveComplete](../../shiori-event/other/OnCompressArchiveComplete.md)和[OnCompressArchiveFailure](../../shiori-event/other/OnCompressArchiveFailure.md)。<br />
目录名必须指定文件夹。\[SSP 2.9.33\] 如果指定的不是文件夹（例如文件路径），则会失败，不执行压缩（如果指定了`--event=`，失败事件（OnCompressArchiveFailure，或在标识符后附加`Failure`的事件）的`Reference1`会设为`invalid parameter`）。<br />
出于安全考虑，压缩目标仅限于SSP管理的文件夹（如ghost文件夹、balloon文件夹，以及通过“文件夹”设置指定的位置）下的路径。<br />
此外，此限制可能会视情况加强，因此最好将压缩目标限制在存放该ghost自身数据的文件夹下。

**対応:** SSP 选项指定仅支持2.7.23及更高版本

## 記述例

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4]Cドライブ直下にSSPがインストールされている場合、Emily/Phase4.5のフォルダをtest.zipに圧縮してghostフォルダに置く。処理が完了するまでスクリプトの実行は停止する。
```

```sakurascript
\![execute,compressarchive,C:/SSP/ghost/test.zip,C:/SSP/ghost/emily4,--event=OnCompressComplete]非同期で圧縮を実行し、完了時にOnCompressCompleteイベントが発生する。
```
