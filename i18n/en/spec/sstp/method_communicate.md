# Method: COMMUNICATE

The COMMUNICATE method lets you provide a ghost with an arbitrary string from outside and make it respond.<br />
This is basically the same as a response to text entered in the ghost's internal communicate box, but because this is SSTP, the ghost may not accept it.

## Simple COMMUNICATE (COMMUNICATE/1.1)

```
COMMUNICATE SSTP/1.1
Charset: UTF-8
Sender: User
Sentence: おはよう。
```

Communicate messages can be sent and received repeatedly between SSTP servers (≈ ghosts).<br />
When sending through Reference0 in a SHIORI/3.0 response, the SSTP message is sent after Sakura Script playback has finished.<br />
This makes it possible to set up behavior that makes ghosts running at the same time appear to be conversing.

## Inter-ghost communicate (COMMUNICATE/1.2)

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

## Request-specific headers

- **Reference\***: Additional information for the communicate message. In SHIORI/3.0, it is stored in Reference2 and later. SSTP Reference0 = SHIORI Reference2.
- **Surface**: The surface numbers for `\0` and `\1` at the time the sending ghost sends the communicate message (≈ when script execution ends).<br />
  Passed as the Surface header in the OnCommunicate event.
- **Option**: *\[Legacy specification\]* If substitute is specified, `\1` speaks the contents of Sentence. ※Not implemented in SSP
