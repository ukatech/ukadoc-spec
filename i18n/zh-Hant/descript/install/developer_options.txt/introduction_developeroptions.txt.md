# developer_options.txt

## 概要

也請參考[檔案結構「網路更新」](../../../manual/update.md)與[檔案結構「安裝」](../../../manual/install.md)。

這是用來在 SSP 建立封存檔或網路更新資訊檔時，為目標檔案設定選項的檔案。<br />
SSP 有一項功能，可將 ghost 等套件的資料夾拖放到 SSP，以建立封存檔（.nar）或 update 檔案（updates2.dau）；執行此功能時會參照本檔案。<br />
因此，原則上若使用其他工具，例如「そだて」或「ghost 配布自動化系統」建立這些檔案，*就完全無關*，請留意。<br />
但也有例外，例如「さとりすと」等工具實作了讀取並使用 developer_options.txt 的功能。

## 記述例

```
ghost/master/savedata.txt,noupdate
shell/old/,nonar
ghost/master/profile/,nonar,noupdate
```

## 注意事項

請注意，設定必須對每個目標（檔案或資料夾）*各自寫在一行*。例如，若寫成以下內容，*只會套用後面（下方）的設定，nonar 選項會失效*。

```
ghost/master/profile/,nonar
ghost/master/profile/,noupdate
```

若要指定兩個選項，正確的寫法如前所述：

```
ghost/master/profile/,nonar,noupdate
```

即為此寫法。
