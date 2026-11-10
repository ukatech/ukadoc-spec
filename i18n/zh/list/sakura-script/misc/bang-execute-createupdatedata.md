# `\![execute,createupdatedata,出力先ファイル]`

**カテゴリ:** 未分類命令

创建执行脚本的 ghost 自身的更新定义文件（updates2.dau/updates.txt）。<br />
输出目标文件：可省略。指定相对于 ghost 的 ghost/master 文件夹的路径，或绝对路径。\[2.8.98\]<br />
指定时，只创建该文件；如果已存在同名文件，则覆盖。文件名以 .dau 结尾时，按与 updates2.dau 相同的格式输出；否则按 updates.txt 的格式输出。<br />
此时，不会创建或删除通常输出位置（ghost 根目录和 ghost/master）中的 updates2.dau/updates.txt。如果输出目标位于 ghost 文件夹内，该文件本身不会包含在更新定义中。

**対応:** SSP 2.5.08
