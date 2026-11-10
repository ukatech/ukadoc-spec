# 方法：COMMUNICATE

使用 COMMUNICATE 方法，可以从外部向 ghost 发送任意字符串并使其作出反应。<br />
基本上，这与 ghost 内部使用沟通框进行交互时的反应相同，但由于这是 SSTP，ghost 可能不会接受该请求。

## 简单的 COMMUNICATE（COMMUNICATE/1.1）

```
COMMUNICATE SSTP/1.1
Charset: UTF-8
Sender: User
Sentence: おはよう。
```

沟通可以在 SSTP 服务器之间（≈ghost 之间）反复收发。<br />
通过 SHIORI/3.0 响应中的 Reference0 发送时，SSTP 会在 Sakura Script 播放结束时发送。<br />
利用这一功能，可以实现同时启动的 ghost 之间仿佛正在对话的效果。

## ghost 之间的沟通（COMMUNICATE/1.2）

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

## request 专用头

- **Reference\***: 沟通的扩展信息。在 SHIORI/3.0 中存储在 Reference2 及之后的字段中。SSTP Reference0 = SHIORI Reference2。
- **Surface**: 发送方 ghost 在发送沟通时（≈脚本执行结束时）`\0`和`\1`的 surface 编号。<br />
  在 OnCommunicate 事件中作为 Surface 头传递。
- **Option**: *\[旧规格\]*指定 substitute 时，由 `\1`说出 Sentence 的内容。※SSP 尚未实现
