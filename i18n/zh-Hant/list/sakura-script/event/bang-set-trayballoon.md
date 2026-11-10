# `\![set,trayballoon,オプション,オプション,オプション...]`

**カテゴリ:** 事件命令

從系統匣圖示顯示balloon。<br />
點擊balloon將其關閉時，會觸發OnTrayBalloonClick。<br />
逾時或按下關閉按鈕將其關閉時，會觸發OnTrayBalloonTimeout。<br />
可指定的選項如下。

Windows 10以上版本中，若檔案關聯設定為「僅捷徑」以上（不包括 kiosk 模式和唯讀模式。變更設定會從下次啟動起套用），將改為顯示 toast 通知，而非balloon，且通知會保留在通知中心。此時不會在系統匣圖示旁顯示。若不符合條件或顯示失敗，則與以往相同，以balloon顯示。<br />
toast 通知在點擊時會觸發OnTrayBalloonClick；按下關閉按鈕將其關閉，或通知逾時並移至通知中心時，會觸發OnTrayBalloonTimeout。移至通知中心後再點擊不會觸發事件。\[2.9.14\]

- **--text=文字**: 顯示於balloon的字串，指定多個值時會分成多行。（必填）
- **--title=標題**: balloon的標題。
- **--icon=圖示設定名稱**: balloon中顯示的圖示設定。<br />
  toast 通知中的圖示會顯示在內文左側。\[2.9.14\]
- **info**: 資訊圖示
- **error**: 錯誤圖示
- **warning**: 警告圖示
- **none**: 無
- **--timeout=秒數**: balloon的顯示時間（單位＝秒）。只能指定10～30秒。Windows 7以上版本會忽略此設定。toast 通知也會忽略此設定。\[2.9.14\]

**対応:** SSP

## 記述例

```sakurascript
\![set,trayballoon,--text=何らかのエラーにより、処理が失敗しました,--title=エラーが発生しました,--icon=error]
```
