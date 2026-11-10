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
※The request ends with a blank line (two consecutive CR+LF sequences, including the preceding line's terminator).

- **Method**:

  - **GET**: A method that assumes that something will be returned in a Value response header.
  - **NOTIFY**: A method that assumes no value will be returned. The Value response header is ignored.<br />
    Mainly used when a mode constraint prevents the ghost from speaking, or for status notification events immediately after startup.<br />
    Note that the same ID (event name) may be used with both GET and NOTIFY.

- **Charset**: Character encoding. It is preferable to put this on the first line, or at least before any line containing characters outside the ASCII range.

- **Sender**: Event sender.

- **SenderType \[SSP 2.5.05～拡張\]**: Attributes of the event sender. The values are as follows. If there are multiple values, they are comma-separated.<br />
  For ID: OnTranslate, the attributes of the event being translated are inherited.

  - **internal**: An event from within the application.
  - **external**: An event from outside the application.
  - **sakuraapi**: An event triggered by the Sakura API.
  - **embed**: An event triggered by the `\![embed]` tag.
  - **raise**: An event triggered by the `\![raise]` tag.
  - **property**: An event triggered by the result of a property system reference command.
  - **plugin**: An event triggered by a plugin.
  - **sstp**: An event triggered by SSTP.
  - **communicate**: An event triggered by the Communicate specification.

- **SecurityLevel**: Security level when executing a script. One of the following.<br />
  For ID: OnTranslate, the attributes of the event being translated are inherited.<br />
  It is notified as early as possible, and appears at least before the ID header.

  - **local**: A notification from within the machine on which the application is running.
  - **external**: A notification from outside the machine on which the application is running.

  An external notification originates outside the machine on which the application is running, so handle it with security in mind.<br />
  This is a different concept from SenderType internal/external. An event originating outside the application may be considered safe and therefore classified as local, so SecurityLevel may be local even when SenderType is external.

- **SecurityOrigin \[SSP拡張\]**: A URL-like string indicating the sending server. It has the following formats. Its concept is the same as that of the [Origin HTTP header](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin).<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme is usually one of http, https, or sstp. hostname is the sending server's name or IP address. port is a port that can receive replies.<br />
  If information is unavailable, such as when a header is not specified in SSTP or there is no concept of a sender, the value is null.<br />
  See also SecurityOrigin in the SSTP specification.

- **Status \[SSP拡張\]**: The ghost's execution state. The values are as follows. If there are multiple values, they are comma-separated.

  - **talking**: Speaking
  - **choosing**: Displaying choices
  - **minimizing**: Being minimized
  - **induction**: In `\![enter,inductionmode]`
  - **passive**: In `\![enter,passivemode]`
  - **timecritical**: In a time-critical section (`\t`)
  - **nouserbreak**: In `\![enter,nouserbreak]`
  - **online**: Communicating over the network
  - **opening(type)**: An input box or similar is open.<br />
    If multiple types are open, they are listed separated by /.<br />
    "dialog" means a file picker, color picker, and similar dialogs.<br />
    Example: opening(communicate/input/teach/dialog)
  - **balloon(group of IDs)**: Balloons are displayed.<br />
    Listed in the format character ID=balloon ID.<br />
    If multiple balloons are open, they are listed separated by /.<br />
    For example, balloon(0=2/1=0) means that a large balloon is displayed for `\0` and a normal balloon for `\1`.

- **ID**: Event name or text resource identifier.

- **BaseID \[SSP拡張\]**: Compatible base event name.<br />
  For example, OnFirstBoot is compatible with OnBoot and is a variant of OnBoot, so OnBoot is set as the BaseID for OnFirstBoot.

- **Reference\***: Additional information associated with the event. A number follows Reference. There is no limit to the number of lines (as long as memory permits).

- **X-SSTP-PassThru-(arbitrary string) \[SSP 2.5.05～拡張\]**: Only when an event notification arrives via SSTP, headers in the SSTP request beginning with "X-SSTP-PassThru-" are passed through unchanged.<br />
  These are not added for other sources.
