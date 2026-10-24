# ShioriEcho.Begin

**カテゴリ:** ゴースト開発用の対話型exe「ゴースト・ターミナル」

このゴーストが起動したときのghost_terminalイベント

- **Reference0**: ターミナルバージョン
- **Reference1**: 端末のセッションタイプ<br />
  端末が \`-s\` で始まる場合は \`SakuraScript\` となる。<br />
  端末が \`-c\` で始まる場合は \`Command\` となる。<br />
  端末が共通で起動する場合は \`Common\` となる。
- **戻り値：X-SSTP-PassThru-Tittle（オプション）**: 端末のタイトルを設定する
- **戻り値：X-SSTP-PassThru-Icon（オプション）**: 端末のアイコンを設定する
- **戻り値：X-SSTP-PassThru-SmallIcon（オプション）**: 端末の小さいアイコンを設定する<br />
  設定されていない場合、\`X-SSTP-PassThru-Icon\`と一致する
- **戻り値：X-SSTP-PassThru-CustomLoginInfo（オプション）**: 設定された場合、端末はデフォルトのログイン情報を表示せず、この<br />
  この戻り値は、単純にエスケープされます：<br />
  \- \``\n`\` は改行に変換されます。<br />
  \- \``\t`\` はタブに変換されます。<br />
  \- \`\\\\\` は \`\\\` に変換される。
