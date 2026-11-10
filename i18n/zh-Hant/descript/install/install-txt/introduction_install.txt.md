# install.txt

## 概要

也請參考[檔案結構「安裝」](../../../manual/install.md)頁面。

這是用於 ghost、balloon、shell 等伺か (Ukagaka)/SSP 內容封存檔（例如 .nar）的安裝設定檔。所有封存檔都可以解壓縮後手動安裝；但若有正確設定的 install.txt，便會啟用安裝程式功能，可透過拖放封存檔等簡單方式安裝。

## 記述例與基本寫法

ghost 的情況（balloon 和 plugin 也幾乎相同，只需更改 type 欄位）

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
```

追加 shell 的情況

```
charset,Shift_JIS
name,凡例さんアルティメットフォーム
type,shell
directory,ultimate
accept,凡例さん
```

ghost 的 supplement（追加檔案）的情況

```
charset,Shift_JIS
name,凡例さん猫化パッチ
type,supplement
accept,凡例さん
```

將 balloon 隨附於 ghost 的情況

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
balloon.directory,example_balloon
balloon.source.directory,balloon
```

※僅 SSP 適用：用於多項內容安裝套件的最上層<br />
（各隨附內容中的 install.txt 照常撰寫即可）

```
charset,Shift_JIS
name,凡例さんファミリー一括入居パッケージ
type,package
```

charset 必須指定在第 1 行（若為 Shift_JIS 則可省略）。

name 和 type 為必填。若 type 不是 supplement 或 package，directory 也為必填。<br />
其他項目則視需要指定。

追加 shell 或 supplement 可使用 accept 設定，以避免安裝到非預期的 ghost。<br />
尤其 supplement 有意外覆寫檔案並造成損壞的風險，因此幾乎是必填項目。<br />
請注意，accept 指定的是*本體端名稱*，而非 ghost 名稱。

在 SSP 中，若要將 balloon 或 plugin 隨附於 ghost 或 shell，請使用 \*.directory。<br />
詳情請參閱[「同時安裝」](introduction_install_multi.md)。

另外，name 主要用於透過 [安裝類 SHIORI Event](../../../list/shiori-event/install/OnInstallComplete.md) 的 Reference 傳送通知內容。<br />
有些 ghost 具備利用此資訊，在安裝完成後切換至該項目的功能；但若 descript.txt 中實際的 ghost 名稱與 install.txt 中的名稱不同，切換將無法正常運作，請留意。
