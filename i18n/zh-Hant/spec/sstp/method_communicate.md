# 方法：COMMUNICATE

透過 COMMUNICATE 方法，可以從外部向 ghost 傳入任意字串並使其產生反應。<br />
基本上與在 ghost 內部使用對話框產生的反應相同，但由於是 SSTP，ghost 端可能不會接受。

## 簡單的 COMMUNICATE(COMMUNICATE/1.1)

```
COMMUNICATE SSTP/1.1
Charset: UTF-8
Sender: User
Sentence: おはよう。
```

ghost 之間可以重複傳送及接收對話（SSTP 伺服器之間（≒ghost 之間））。<br />
透過 SHIORI/3.0 的回應 Reference0 傳送時，SSTP 的傳送時機會是在 Sakura Script 播放結束時。<br />
利用這項功能，可以組成讓同時啟動的 ghost 彼此交談的處理。

## ghost 間對話(COMMUNICATE/1.2)

```
COMMUNICATE SSTP/1.2
Charset: UTF-8
Sender: Emily
HWnd: 28236
Sentence: \0\s[5]ちゃっらーん！エミリでーす！\nボクのお腹にはまだ若干の余裕が…？\1\s[11]そんなこと言ってたらまた太るよ？
Surface: 5,11
Reference0: 芋ちょうだい
Reference1: たくさんちょうだい
Reference2: 今すぐちょうだい
```

## request 專用標頭

- **Reference\***: 對話的擴充資訊。在 SHIORI/3.0 中會存放於 Reference2 以後。SSTP Reference0 = SHIORI Reference2。
- **Surface**: 傳送來源 ghost 傳送對話時（≒指令碼執行結束時）的`\0`和`\1`表面編號。<br />
  會在 OnCommunicate 事件中作為 Surface 標頭傳遞。
- **Option**: *\[舊規格\]*指定 substitute 時，Sentence 的內容會由`\1`說出。 ※SSP 尚未實作
