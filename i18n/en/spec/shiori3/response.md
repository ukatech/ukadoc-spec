# response

## Sample

```
SHIORI/3.0 200 OK
Charset: UTF-8
Sender: AYA
Value: \1\s[10]\0\s[0]\e
```

※The line ending is CR+LF.<br />
※The response must end with a blank line (two consecutive CR+LF line endings).

- **Status code**: As with HTTP, codes in the 200 range indicate success, while all others indicate some kind of failure (error).<br />
  The codes primarily used at present are as follows.

  - **200**: 200 OK<br />
    Success, with a return value (Value).
  - **204**: 204 No Content<br />
    Success, with no return value.
  - **311**: 311 Not Enough<br />
    For ID: OnTeach (the SHIORI/2-series TEACH method), indicates that additional information is required.<br />
    Reopen the input box and ask the user, then add a Reference containing the input string after input is complete.
  - **312**: 312 Advice<br />
    For ID: OnTeach (the SHIORI/2-series TEACH method), indicates that the most recently entered string cannot be interpreted and should be discarded.<br />
    Discard the last Reference, reopen the input box and ask the user, then add a Reference containing the input string after input is complete.
  - **400**: 400 Bad Request<br />
    The request string could not be interpreted.
  - **500**: 500 Internal Server Error<br />
    An error occurred inside SHIORI, and it could not return a response.

- **Charset**: Character encoding. It is preferable to place this on the first line, or at least before any line containing characters outside the ASCII range.

- **Sender**: The sender. Usually the name of the SHIORI.

- **Value**: The script to speak.

- **ValueNotify \[SSP extension 2.5.35\]**: *\[Experimental feature\]*<br />
  An extension for executing Sakura Script even when the request method is NOTIFY.<br />
  When Sakura Script is returned in this header, it is executed immediately. For GET, it is executed before the script in the Value header.<br />
  The tags that can be executed are extremely limited; all other tags and text are ignored.<br />
  <del>Ignored when the method is not NOTIFY or when the Value header is already present.</del> Restriction removed in 2.6.76<br />
  The tags that can currently be executed are as follows:

  - `\![sound]`
  - `\![set,trayicon]`
  - `\![set,trayballoon]`
  - `\![raise]`
  - `\![raiseother]`
  - `\![raiseplugin]`
  - `\![timerraiseother]`
  - `\![timerraiseplugin]`
  - `\![notify]`
  - `\![notifyother]`
  - `\![notifyplugin]`
  - `\![get,property]` +2.6.82
  - `\![set,property]` +2.6.82

- **SecurityLevel \[SSP extension\]**: One of the following.

  - **local**: A security level equivalent to a script from within the running machine.
  - **external**: A security level equivalent to a script from outside the running machine.

  The SecurityLevel of the script to speak. When external, some scripts cannot be executed due to security features.

- **Marker \[SSP extension\]**: The string to display in the balloon marker (additional information below the balloon).

- **ErrorLevel \[SSP extension\]**: The level of an error that occurred inside SHIORI. One of the following. To represent multiple errors, separate them with byte value 1.

  - **info**: Information. Not an error.
  - **notice**: Notice. Descriptions that should be corrected, although they are not necessarily errors.
  - **warning**: Warning. There are errors such as incorrect descriptions; processing has not stopped, but they should be addressed.
  - **error**: Ordinary error. Processing has stopped due to an issue such as an incorrect description and cannot be resumed.
  - **critical**: Critical error. More severe than error; it should be addressed immediately.

  If this header is present, the user is notified that some kind of error has occurred.<br />
  The notification level can be changed by the user. Usually, it is error or higher.<br />
  In SSP, the error is recorded in the error log, and an error icon appears in the notification area.

- **ErrorDescription \[SSP extension\]**: Detailed information about an error that occurred inside SHIORI. Valid only when ErrorLevel is present.<br />
  To represent multiple errors, separate them with byte value 1.<br />
  The number of elements in ErrorLevel and ErrorDescription must be the same.

- **BalloonOffset \[SSP extension\]**: Balloon offset values (X,Y).

- **Reference0**: If you want to send a Communicate, the name of the ghost's `\0` side.

- **Reference1 onward**: Additional information for Communicate.<br />
  Response Reference1 = SSTP Communicate Reference0 = recipient's OnCommunicate Reference2<br />
  Note that these are offset as shown above for compatibility reasons.

- **Age \[SSP extension\]**: The generation number of the Communicate. The first is zero. It increases by 1 each time the exchange continues.<br />
  Although this is an SSP extension, in practice it is SHIORI/2.x compatibility processing.

- **MarkerSend \[SSP extension\]**: The balloon marker string to display “on the other side” during Communicate.<br />
  Sent as the SSTP Marker header.

- **X-SSTP-PassThru-(any string) \[SSP 2.5.03～ extension\]**: Only in a response to an event notification from SSTP, this header is added unchanged to the SSTP response.<br />
  Ignored for anything other than SSTP.<br />
  Multiple headers can be specified, but if you want to return multiple headers, change the header names.<br />
  (Old header name: X-SSTP-Return- is deprecated)
