# ShioriEcho

**カテゴリ:** ゴースト開発用の対話型exe「ゴースト・ターミナル」

コマンドが入力された後のイベント

- **Reference0**: 端末で収集したコマンド
- **戻り値**: もし\`ShioriEcho.GetResult\`を定義していない場合、ここで\`ShioriEcho.GetResult\`でサポートされている任意の返値を返すことができます。これらの返値は、ターミナルによって正しく処理されます（ただし、戻り値3は、\`ShioriEcho.GetResult\`を定義せずに何も返さない場合、次のコマンド取得に入ります）。<br />
  \`ShioriEcho.GetResult\`を定義している場合、ここでの返値は無視されます（\*\*ただし、sakura scriptは正常に実行される\*\*）。
