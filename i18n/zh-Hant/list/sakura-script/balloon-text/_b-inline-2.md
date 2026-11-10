# `\_b`\[檔案路徑,inline,[選項](note-1.md#_bファイルパスについて),選項...\]

**カテゴリ:** バルーン、テキストコマンド

將圖片貼入 balloon 文字行內，並視為一個字元。<br />
\[執行中 ghost 的資料夾\]/ghost/master 為基準資料夾。<br />
※可使用 base64 編碼或 exe/dll 資源作為圖片，而非檔名，[※請參閱下方](note-1.md#補足)。

可指定的選項請參閱[※下方](note-1.md#_bファイルパスについて)。

## 記述例

```sakurascript
本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.png\_b[test.png,inline,--option=use_self_alpha,--clipping=100 30 150 90]を、文字扱い、ファイルの透過情報付きpngとして、画像の横100～150pixel縦30～90pixelの範囲を表示する。
```

**対応:** SSP
