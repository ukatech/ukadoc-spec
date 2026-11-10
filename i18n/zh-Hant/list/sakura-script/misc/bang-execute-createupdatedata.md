# `\![execute,createupdatedata,出力先ファイル]`

**カテゴリ:** 未分類指令

建立執行此腳本的 ghost 自身的更新定義檔（updates2.dau/updates.txt）。<br />
輸出目的地檔案：可省略。以相對於 ghost 的 ghost/master 資料夾的路徑或絕對路徑指定。\[2.8.98\]<br />
若有指定，只會在該檔案建立一個檔案；若已有同名檔案則會覆寫。檔名以 .dau 結尾時，會以與 updates2.dau 相同的格式輸出；否則會以 updates.txt 的格式輸出。<br />
此時不會建立或刪除通常的輸出目的地（ghost 根目錄與 ghost/master）中的 updates2.dau/updates.txt。若輸出目的地位於 ghost 資料夾內，該檔案本身不會包含在更新定義中。

**対応:** SSP 2.5.08
