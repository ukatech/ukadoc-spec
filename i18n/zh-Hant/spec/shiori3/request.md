# request

## Sample

```
GET SHIORI/3.0
Charset: UTF-8
Sender: SSP
SenderType: internal,raise
SecurityLevel: local
Status: choosing,balloon(0=0)
ID: OnFirstBoot
BaseID: OnBoot
Reference0: 1
```

※The line ending is CR+LF.<br />
※The final line is a blank line (equivalent to (CR+LF)x2 including the preceding line ending).

- **Method**:

  - **GET**: A method intended to return some value in a response Value header.
  - **NOTIFY**: A method intended to return no value. The response Value header is ignored.<br />
    Mainly used when the ghost cannot "speak" due to a mode restriction, or for status notification events immediately after startup.<br />
    Note that both GET and NOTIFY may be used with the same ID (event name).

- **Charset**: Character encoding. It is preferable to place this on the first line, or at least before any line containing characters outside the ASCII range.

- **Sender**: Event sender.

- **SenderType \[SSP 2.5.05～拡張\]**: Attributes of the event sender, as listed below. If there are multiple attributes, they are comma-separated.<br />
  For ID: OnTranslate, the attributes of the source event are inherited.

  - **internal**: An event from inside the application.
  - **external**: An event from outside the application.
  - **sakuraapi**: An event triggered by the Sakura API.
  - **embed**: An event triggered by the `\![embed]` tag.
  - **raise**: An event triggered by the `\![raise]` tag.
  - **property**: An event triggered by the result of a property system query.
  - **plugin**: An event triggered by a plugin.
  - **sstp**: An event triggered by SSTP.
  - **communicate**: An event triggered by the communicate specification.

- **SecurityLevel**: The security level when executing a script. One of the following.<br />
  For ID: OnTranslate, the attributes of the source event are inherited.<br />
  This is notified as early as possible in the request, and appears at least before the ID header.

  - **local**: A notification from within the machine running the application.
  - **external**: A notification from outside the machine running the application.

  An external notification originates outside the machine running the application, so it requires careful security handling.<br />
  This is a separate concept from SenderType internal/external. An event originating outside the application may still be considered safe and classified as local, so SecurityLevel may be local even when SenderType is external.

- **SecurityOrigin \[SSP拡張\]**: A URL-like string indicating the source server. It has one of the following formats. The concept is the same as that of the [Origin HTTP header](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin).<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme is usually one of http, https, or sstp. hostname is the source server name or IP address. port is a port that can accept replies.<br />
  This is null when information is unavailable, such as when no header is specified in SSTP or when there is no concept of a sender in the first place.<br />
  Also refer to SecurityOrigin in the SSTP specification.

- **Status \[SSP拡張\]**: The ghost's execution status. The following values are used. If there are multiple values, they are comma-separated.

  - **talking**: In the middle of speaking
  - **choosing**: Displaying choices
  - **minimizing**: Minimized
  - **induction**: In `\![enter,inductionmode]`
  - **passive**: In `\![enter,passivemode]`
  - **timecritical**: In a time-critical section (`\t`)
  - **nouserbreak**: In `\![enter,nouserbreak]`
  - **online**: Network communication in progress
  - **opening(種類)**: An input box or similar is open.<br />
    If multiple types are open, they are listed separated by /. <br />
    "dialog" refers to file selection, a color picker, and similar dialogs.<br />
    Example: opening(communicate/input/teach/dialog)
  - **balloon(ID群)**: A balloon is displayed.<br />
    Listed in the format character ID=balloon ID.<br />
    If multiple balloons are open, they are listed separated by /. <br />
    For example, balloon(0=2/1=0) means that `\0` is displaying the larger balloon and `\1` is displaying the normal balloon.

- **ID**: An event name or a text resource identifier.

- **BaseID \[SSP拡張\]**: The compatible base event name.<br />
  Example: OnFirstBoot is compatible with OnBoot and is a variant of OnBoot, so its BaseID is OnBoot.

- **Reference\***: Additional information associated with the event. A number follows Reference. There is no limit to the number of lines (as long as memory allows).

- **X-SSTP-PassThru-(任意の文字列) \[SSP 2.5.05～拡張\]**: Only when an event notification arrives via SSTP, any SSTP request header beginning with "X-SSTP-PassThru-" is forwarded as-is.<br />
  It is not added for non-SSTP events.
