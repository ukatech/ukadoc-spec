# response

## Sample

```
SHIORI/3.0 200 OK
Charset: UTF-8
Sender: AYA
Value: \1\s[10]\0\s[0]\e
```

※The line ending is CR+LF.<br />
※The response must end with a blank line (two consecutive CR+LF sequences, including the line ending of the preceding line).

- **Status code**: As with HTTP, codes in the 200 range indicate success; other codes indicate some kind of failure (error).<br />
  The following codes are currently used most often.

  - **200**: 200 OK<br />
    Success, with a return value (Value).
  - **204**: 204 No Content<br />
    Success, with no return value.
  - **311**: 311 Not Enough<br />
    For ID: OnTeach (the TEACH method in SHIORI/2.x), indicates that more information is required.<br />
    Reopen the input box to ask the user, then add a Reference containing the input string after input is complete.
  - **312**: 312 Advice<br />
    For ID: OnTeach (the TEACH method in SHIORI/2.x), indicates that the most recently entered string cannot be interpreted and should be discarded.<br />
    Discard the last Reference, reopen the input box to ask the user, then add a Reference containing the input string after input is complete.
  - **400**: 400 Bad Request<br />
    The request string could not be interpreted.
  - **500**: 500 Internal Server Error<br />
    An error of some kind occurred inside SHIORI, and it could not return a response.

- **Charset**: Character encoding. It is preferable to place this on the first line, or at least before any line containing characters outside the ASCII range.

- **Sender**: The sender. Usually the name of SHIORI.

- **Value**: The script to speak.

- **ValueNotify \[SSP extension 2.5.35\]**: *\[Experimental feature\]*<br />
  An extension for executing Sakura Script even when the request method is NOTIFY.<br />
  When Sakura Script is returned in this header, it executes immediately. For GET, it executes before the script in the Value header.<br />
  The tags that can be executed are extremely limited; all other tags and strings are ignored.<br />
  <del>Ignored if the method is not NOTIFY or if a Value header already exists.</del> Restriction removed in 2.6.76<br />
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

  - **local**: A security level equivalent to a script originating from the running device.
  - **external**: A security level equivalent to a script originating outside the running device.

  The SecurityLevel of the script to speak. When set to external, some scripts cannot be executed due to security features.

- **Marker \[SSP extension\]**: The string to display in the balloon marker (additional information below the balloon).

- **ErrorLevel \[SSP extension\]**: The level of an error that occurred inside SHIORI. One of the following. To represent multiple errors, separate them with byte value 1.

  - **info**: Information. Not an error.
  - **notice**: Notice. Descriptions that should be fixed, although they are not quite errors.
  - **warning**: Warning. There are issues such as writing errors; processing has not stopped, but it is better to address them.
  - **error**: A regular error. Processing has stopped due to issues such as writing errors and cannot be resumed.
  - **critical**: A critical error. More severe than error, and should be addressed immediately.

  When this header is present, the user is notified that an error of some kind has occurred.<br />
  The levels to be notified can be configured by the user. Normally, error and above.<br />
  In SSP, the error is recorded in the error log, and an error icon appears in the notification area.

- **ErrorDescription \[SSP extension\]**: Details of an error that occurred inside SHIORI. Valid only when ErrorLevel is present.<br />
  To represent multiple errors, separate them with byte value 1.<br />
  The number of elements in ErrorLevel and ErrorDescription must be the same.

- **BalloonOffset \[SSP extension\]**: Balloon offset values (X,Y).

- **Reference0**: When sending a Communicate, the name of the ghost's `\0` side.

- **Reference1～**: Additional information for Communicate.<br />
  Response Reference1 = SSTP Communicate Reference0 = recipient's OnCommunicate Reference2<br />
  Note that these are offset as shown above for compatibility reasons.

- **Age \[SSP extension\]**: The generation number of a Communicate. The first is zero. Increases by 1 with each exchange.<br />
  This is an SSP extension, but in practice it is SHIORI/2.x compatibility processing.

- **MarkerSend \[SSP extension\]**: The balloon marker string to display “on the other party's side” during a Communicate.<br />
  Sent as the SSTP Marker header.

- **X-SSTP-PassThru-(任意の文字列) \[SSP 2.5.03～ extension\]**: Only in responses to event notifications from SSTP, this header is added unchanged to the SSTP response.<br />
  Ignored when not using SSTP.<br />
  Multiple headers can be specified, but use different header names if you want to return multiple headers.<br />
  (Old header name: X-SSTP-Return- is scheduled for deprecation)
