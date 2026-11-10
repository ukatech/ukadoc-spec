# .narignore / .updateignore / .narinclude / .updateinclude

## .narignore / .updateignore

為了比 developer_options.txt 的語法更具彈性，.narignore/.updateignore 可直接使用 .gitignore 的語法。

請參閱 [.gitignore 的手冊](https://git-scm.com/docs/gitignore/ja)，或向 LLM（文字生成 AI）描述需求並請它產生內容。

但與 .gitignore 不同，即使放在子目錄中也不會生效。只有放在 ghost 根目錄下時才有效。

這是伺か限定的特殊功能，可使用 include: 指定內容。例如，<br />
include:.narignore<br />
如此書寫時，會將 .narignore 檔案的全部內容視同插入此行的位置來處理。

include: 指定的相對路徑並非以 ghost 根目錄為基準，而是以寫有該行的檔案所在目錄為基準解析。也可以在讀入的檔案中進一步使用 include:；此時基準目錄會依序更新為「目前讀入的檔案所在目錄」（基準會從父檔案移至子檔案，再移至孫檔案）。

遞迴讀取有深度上限，最多可追蹤 3 層。超過此深度的 include: 會遭拒絕讀取。路徑分隔符號可使用 / 或 \\。

例如，在 ghost 根目錄下的 .narinclude 中寫入 include:sub/extra.txt，就會讀取 sub/extra.txt。如果再於該 extra.txt 中寫入 include:foo.txt，則會以 extra.txt 所在的 sub/ 目錄為基準，而非 ghost 根目錄，讀取 sub/foo.txt。

**対応:** SSP

## .narinclude / .updateinclude

這是 .narignore/.updateignore 的白名單版本。只有在此處列出的項目會納入更新檔案/NAR。<br />
子目錄的處理方式與 gitignore 不同；例如，只寫 shell/master 而不寫 shell/，也會正確納入父目錄。

此外，與 .narignore/.updateignore 相同，這也與 .gitignore 不同，即使放在子目錄中也不會生效。只有放在 ghost 根目錄下時才有效。

**対応:** SSP
