# 同時安裝

## 概要

在 SSP 中，可以將 balloon 等內容隨附於 ghost 或 shell 的封存檔，並一起安裝。<br />
隨附內容以「\*.」開頭的項目指定，\* 部分填入隨附內容的種類。

\* 可填入以下 5 種：

- **balloon**：balloon
- **headline**：headline sensor
- **plugin**：plugin
- **calendar.skin**：行事曆外觀檔案
- **calendar.plugin**：行事曆排程感測器

請注意，與 [type](type.md) 的寫法不同，行事曆類型使用*點號分隔*（calendar.skin，而非 calendar skin）。

無論封存檔本身的 [type](type.md) 為何都能運作，但實際上用於 type 為 *ghost* 或 *shell* 的封存檔。

## 多個隨附項目的編號方式

隨附多個相同種類的項目時，將 \* 部分寫成 balloon0、balloon1、…，在種類後加上從 0 開始的編號並依序排列。（SSP 2.7.00 以後）

依照*無編號→0→1→2…*的順序搜尋，*遇到不存在的編號時即停止搜尋*。<br />
因此*不可跳號*。例如只寫 balloon0 和 balloon2 時，搜尋會在 balloon1 不存在時停止，因此不會讀取 balloon2。

無編號項目和 0 會視為不同項目。若同時寫入 balloon 和 balloon0，便會安裝 2 個 balloon。

[\*.directory](star-.directory.md)、[\*.source.directory](star-.source.directory.md)、[\*.refresh](star-.refresh.md)、[\*.refreshundeletemask](star-.refreshundeletemask.md) 均可針對各個編號分別指定。

另外，只有第一個會設定為與 ghost 或 shell *關聯的 balloon*。<br />
第二個以後的 balloon 只會安裝，不會成為該 ghost 的預設 balloon。

## 記述例

隨附 2 個 balloon 和 1 個 plugin 至 ghost 的情況

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
balloon0.directory,example_balloon
balloon0.source.directory,balloon_normal
balloon1.directory,example_balloon_ex
balloon1.source.directory,balloon_special
plugin0.directory,example_plugin
```
