# metainfo

**カテゴリ:** 屬性系統 \> 通用屬性名稱

目標的 descript.txt 中記載的 [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) 值（metainfo 資料夾的 URL）。原樣回傳記載的字串。<br />
由於此值從 descript.txt 讀取，載入 ghost、balloon 清單時即可取得（並非延遲讀取）。<br />
若 descript.txt 中未記載，則取得失敗。即使只記載了 `githubrepo`，作為 `metainfo` 取得時仍會失敗。

**対応:** SSP 2.9.35
