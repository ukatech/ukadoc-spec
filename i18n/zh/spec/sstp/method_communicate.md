# Method: COMMUNICATE

The COMMUNICATE method lets you give a ghost an arbitrary string from outside and make it react.<br />
Basically, this works the same as a reaction using the communicate box inside a ghost, but because it is SSTP, the ghost may not accept it.

## Simple COMMUNICATE (COMMUNICATE/1.1)

```
COMMUNICATE SSTP/1.1
Charset: UTF-8
Sender: User
Sentence: おはよう。
```

Ghosts can repeatedly send and receive communicate messages between SSTP servers (≒ ghosts).<br />
When sending via Reference0 in a SHIORI/3.0 response, the SSTP send timing is after Sakura Script playback has finished.<br />
This can be used to make ghosts running at the same time appear to be having a conversation.

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

- **Reference\***: Extended information for communicate. In SHIORI/3.0, this is stored in Reference2 and later. SSTP Reference0 = SHIORI Reference2.
- **Surface**: The surface numbers for `\0` and `\1` at the time the sending ghost sends the communicate message (≒ when script execution ends).<br />
  Passed as the Surface header in the OnCommunicate event.
- **Option**: *\[Legacy specification\]* If substitute is specified, `\1` speaks the contents of Sentence. ※Not implemented in SSP
