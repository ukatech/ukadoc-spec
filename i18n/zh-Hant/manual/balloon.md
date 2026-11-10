# balloon

balloon 資料夾中的檔案如下。

```filetree
+-(myballoon)
　　+-descript.txt
　　+-readme.txt
　　+-balloons*.png
　　+-balloons*.pna （MATERIA不可）
　　+-balloons*s.txt
　　+-balloonk*.png
　　+-balloonk*.pna （MATERIA不可）
　　+-balloonk*s.txt
　　+-balloonp*def*.png  (SSP 2.5.51～)
　　+-balloonp*def*.pna  (SSP 2.5.51～)
　　+-balloonp*def*s.txt
　　+-balloonc*.png
　　+-balloonc*.pna  (SSP 2.5.37～)
　　+-balloonc*s.txt  (SSP 2.5.37～)
　　+-online*.png
　　+-sstp.png
　　+-arrow0.png
　　+-arrow1.png
　　+-arrows0.png  (SSP 2.4.78～)
　　+-arrows1.png  (SSP 2.4.78～)
　　+-arrowk0.png  (SSP 2.4.78～)
　　+-arrowk1.png  (SSP 2.4.78～)
　　+-arrowp*def0.png  (SSP 2.5.51～)
　　+-arrowp*def1.png  (SSP 2.5.51～)
　　+-thumbnail.png
　　+-ok_down.png/ok_up.png （SSPのみ）
　　+-cancel_down.png/cancel_up.png （SSPのみ）
　　+-mode_down.png/mode_up.png （SSPのみ）
　　+-sstp_new.png （SSPのみ）
　　+-sstp_newk.png  (SSP 2.5.51～)
　　+-sstp_newp*def.png  (SSP 2.5.51～)
　　+-marker.png （SSPのみ）
　　+-markers.png  (SSP 2.4.78～)
　　+-markerk.png  (SSP 2.4.78～)
　　+-markerp*def.png  (SSP 2.5.51～)
　　+-clickwait.png  (SSP 2.5.54～)
　　+-clickwaits.png  (SSP 2.5.54～)
　　+-clickwaitk.png  (SSP 2.5.54～)
　　+-clickwaitp*def.png  (SSP 2.5.54～)
```

- **[descript.txt](../descript/balloon/index.md)**: 用來識別 balloon 的檔案。

  相較於 ghost 或 shell 的 descript.txt，其中記載的項目較多。

  詳細資訊請參閱[連結](../descript/balloon/index.md)。

- **[balloons\*s.txt/balloonk\*s.txt/balloonc\*s.txt](../descript/balloon/balloonsoption/index.md)**: 用來設定各 balloon 個別選項的檔案。

  若為對應 ID 的 surface（balloons1.png 對應 balloons1s.txt）建立此檔案，便會覆寫 descript.txt 中的設定，並套用於該 surface。

  可用於變更特定 ID 的 surface 設定等情況。

  ※請注意檔名中的 s（不是 balloons\*.txt，而是 balloons\**s*.txt）

  現在也可用於輸入框。請以 balloonc\*s.txt 指定。

  詳細資訊請參閱[連結](../descript/balloon/balloonsoption/index.md)。

- **readme.txt**: balloon 作者用來記載發佈來源等資訊的檔案。

  可省略，但準備此檔案後，可在安裝時或從 baseware 的選單等處參閱。

- **balloons\*.png**: 本體側的對話框。

  \*代表 balloon 的 surface ID 數字。

  偶數 ID 是朝左的 balloon，奇數 ID 是朝右的 balloon，兩者成對。

  一般而言會採用以下配置，但也可以自由設定。也可以新增 4-5、6-7 等成對 ID，或只使用 0-1。

  - balloons0.png　以及　balloons1.png　……　一般對話框（左・右）
  - balloons2.png　以及　balloons3.png　……　縱長對話框（左・右）

- **balloons\*.pna**: MATERIA 不支援。

  將灰階（黑：透明←→不透明：白）的 png 圖片副檔名改為 pna。

  若準備與對應 ID 的 png（balloons0.png 對應 balloons0.pna）相符的 pna，即可將其用作透明度設定。

  SSP 也可以透過[設定](../descript/balloon/descript-txt/use_self_alpha.md)使用 png 本身的 alpha 通道。

  此檔案可省略。

- **balloonk\*.png**: 搭檔側（或第三人及之後角色）的對話框。

  基本上與 balloons\*.png 相同，但通常高度較小。

  此檔案可省略。省略時會使用本體側對應 ID 的圖片。

- **balloonk\*.pna**: balloons\*.pna 的 balloonk\*.png 版本。說明請參閱前述的 balloons\*.pna。

- **balloonp\*def\*.png**: 第三人及之後角色的對話框。對應於 `\p[2]` 的 balloon 為 balloonp2def0.png / balloonp2def1.png。

  此檔案可省略。省略時會使用 balloonk；若沒有 balloonk，則使用 balloons。

- **balloonp\*def\*.pna**: balloons\*.pna 的 balloonp\*def\*.png 版本。說明請參閱前述的 balloons\*.pna。

- **balloonc\*.png**: balloon 的輸入視窗。

  \*會是 0 到 3（SSP 為 4）的數字，各編號檔案對應如下。

  - balloonc0.png　……　Send 方塊
  - balloonc1.png　……　Communicate 方塊
  - balloonc2.png　……　Teach 方塊
  - balloonc3.png　……　Input 方塊
  - balloonc4.png　……　Address Bar 方塊（僅限 SSP）
  - balloonc5.png　……　多行輸入（Textarea）方塊（SSP 2.9.10 以後。若不存在，則使用 balloon 本體的圖片）

- **balloonc\*.pna**: balloons\*.pna 的輸入框版本。

- **online\*.png**: 接收網路資訊時顯示的圖片。

  依序循環播放動畫。

- **arrow\*.png**: 用於捲動文字的圖片。

  0 朝上，1 朝下。

  SSP 可以定義本體和搭檔專用的圖片。詳見後述。

- **sstp.png**:

  - 接收 SSTP 時，顯示傳送者資訊等內容
  - 執行 `\![*]` 標籤時（SSP 中 %\* 也相同）

  會顯示此圖片。SSP 可以分別設定專用圖片。詳見後述。

- **thumbnail.png**: 在選單樹中選取 balloon 時顯示的縮圖。

  可使用的圖片格式為 png 或 jpg。

  將 png 改名為 pnr 後，圖片左上角的 1 個像素（座標 0,0）會以相同顏色設為透明。

  此檔案可省略。

以下僅限 SSP。全部皆可省略。

- **ok_down.png/ok_up.png**: 輸入框類型的 OK 按鈕圖片。

- **cancel_down.png/cancel_up.png**: 輸入框類型的取消按鈕圖片。

- **mode_down.png/mode_up.png**: 模式切換按鈕圖片。

- **sstp_new.png / sstp_newk.png / sstp_newp\*def.png**: 接收 SSTP 時，顯示傳送者資訊等內容所使用的圖片（與 sstp.png 不同，僅供此用途使用）。

- **marker.png / markers.png / markerk.png / markerp\*def.png**: 以 `\![*]` 標籤（SSP 中 %\* 也相同）顯示的圖片（與 sstp.png 不同，僅供此用途使用）。

  markers 用於本體側（為相容舊版，建議以 marker 代替），markerk 用於搭檔側，markerp2def 以後則用於 `\p[2]` 以後的角色。

- **arrows\*.png / arrowk\*.png / arrowp\*def.png**: 用於捲動文字的圖片。僅限 SSP 2.4.78 以後版本。

  0 朝上，1 朝下。

  arrows 用於本體側（為相容舊版，建議以 arrow 代替），arrowk 用於搭檔側，arrowp2def 以後則用於 `\p[2]` 以後的角色。

- **clickwait.png / clickwaits\*.png / clickwaitk\*.png / clickwaitp\*def.png**: 用於表示等待點擊（`\x`）的圖片。僅限 SSP 2.5.54 以後版本。

  clickwaits 用於本體側，clickwaitk 用於搭檔側，clickwaitp2def 以後則用於 `\p[2]` 以後的角色。
