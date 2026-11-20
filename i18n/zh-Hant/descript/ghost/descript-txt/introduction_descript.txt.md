# descript.txt（ghost 的）

## 概要

ghost 的基本設定檔。<br />
可設定 ghost 名稱、作者名稱、shiori 設定、balloon 基本位置資訊及圖示等各種資訊。

!!! note "可由 shell 的 descript.txt 覆寫的項目"
    與 shell 的 `descript.txt` 共通的項目（`sakura.name` / `kero.name`、owner draw 選單的圖片與顏色、balloon 與角色的位置、surface 位置資訊、滑鼠游標、`don't need ...`、`shiori.logo.*` 等）也可以寫在 ghost 的 `descript.txt` 中。<br />
    寫在 ghost 端的設定會成為整個 ghost 的預設值；若 shell 的 `descript.txt` 中有相同項目，則以 shell 端的設定為優先（覆寫 ghost 端的設定）。<br />
    這些項目列在 [Shell 設定](../../shell/descript-txt/index.md)，而非本頁。對應項目均註明「也可以寫在 ghost 端的 descript.txt 中」。

## 記述例 與基本寫法

```
charset,Shift_JIS
type,ghost
name,凡例さん
sakura.name,凡例さん
kero.name,斑糲岩
homeurl,http://ssp.shillest.net/ukadoc/manual/hogehoge/example/

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

shiori,satori.dll
```

type、name、sakuraname、keroname、craftman、craftmanw 為必填項目（使用 SSP 時，部分項目可省略）。

使用 Satori 等 dll 名稱不是「shiori.dll」的 SHIORI 時，請注意不要忘記在 shiori 中指定 dll 名稱。

homeurl 除了寫在 descript.txt 中，也可透過回覆 baseware 的 [SHIORI Resource](../../../list/shiori-resource/ghost/homeurl.md) 要求來設定（方法依 SHIORI 而異，故略過）。<br />
基本上指定其中一種即可；若兩者都指定，請特別注意網站搬遷時忘記修改其中一處等失誤。

另外，以 \\ 或 % 開頭的字串會被視為 Sakura Script 或環境變數標籤，基於安全風險而遭捨棄。若要將其作為一般字元使用，必須以 \\\\ 或 \\% 等方式跳脫。
