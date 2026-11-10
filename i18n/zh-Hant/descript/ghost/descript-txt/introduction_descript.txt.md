# descript.txt（ghost 的）

## 概要

ghost 的基本設定檔。<br />
可設定 ghost 名稱、作者名稱、SHIORI 設定、balloon 基本位置資訊、圖示等各種資訊。

## 記述例與基本寫法

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

type、name、sakuraname、keroname、craftman、craftmanw 為必填（SSP 中有些項目可省略）。

若使用名稱不是「shiori.dll」的 DLL（例如 Satori）作為 SHIORI，請記得在 shiori 中指定 DLL 名稱。

homeurl 除了寫在 descript.txt 中，也可以透過回應 baseware 的 [SHIORI Resource](../../../list/shiori-resource/ghost/homeurl.md) 請求來設定（方法取決於 SHIORI，因此略）。<br />
原則上指定其中一處即可；若兩處都指定，請注意網站搬遷時可能忘記修改其中一處。

另外，以 \\ 或 % 開頭的字串會被視為 Sakura Script 或環境變數標籤，基於安全性風險會被丟棄。若要將這些字元作為一般文字使用，必須以 \\\\ 或 \\% 等方式跳脫。
