# HEADLINE/2.0

Last modified: 2013-08-07

Reference: [HEADLINE/1.1](http://usada.sakura.vg/contents/headlinesenser.html) (external site)

## Preface

HEADLINE/2.0 is a revision of the legacy specification (1.1). It is currently implemented only by SSP.

The main change is the addition of character encoding specification.

## Headline data

Two files are required: the configuration file "descript.txt" and a DLL file that exports the execute function.

## DLL

See the [DLL page](dll.md).

## request - response 1: get version

### request example

```
GET Version HEADLINE/2.0
Charset: UTF-8
Sender: SSP
```

### request header details

- **Charset**: Character encoding
- **Sender**: Event sender

### response example

```
HEADLINE/2.0 200 OK
Charset: UTF-8
Value: HeadlineModule 1.1
```

### response header details

- **Charset**: \[Optional\] Character encoding. If omitted, the caller's specified encoding is used.
- **Value**: \[Optional\] Version string

## request - response 2: get headlines

### request example

```
GET Headline HEADLINE/2.0
Charset: UTF-8
Sender: SSP
Option: url
Path: C:\SSP\temp\ad9326dc37cb86a9.html
```

### request header details

- **Charset**: Character encoding
- **Sender**: Event sender
- **Option**: \[Optional\] Options that can be parsed in the response. Listed as comma-separated values.<br />
  Currently, only url is supported. See the Headline header section in the response.
- **Path**: Full path of the file to parse for headlines.

### response example

```
HEADLINE/2.0 200 OK
Charset: UTF-8
Headline: ほげほげ1
Headline: ほげほげ2
Headline: ほげほげ3
Headline: ほげほげ4
Headline: ほげほげ5
```

### response header details

- **Charset**: \[Optional\] Character encoding. If omitted, the caller's specified encoding is used.
- **RequestCharset**: \[Optional\] The preferred character encoding for the next call. If omitted, Charset is used.
- **Headline**: Headline content.<br />
  URL extensions are supported if the Option header contains url when called, as in Option: url.<br />
  In that case, if the response is in the format content\[1\]URL, with byte value 1 as the separator, the URL is also notified to the ghost. If supported by the ghost, clicking an item may jump to its details, for example.<br />
  Note that the returned content is not a fragment of Sakura Script, and tags cannot be used. Return plain text only.

## descript.txt

See the [Headline settings page](../descript/headline/index.md).

## SHIORI Event

For details on all of these, see the [SHIORI Event page](../list/shiori-event/index.md).

- **[OnHeadlinesenseBegin](../list/shiori-event/headline-rss/OnHeadlinesenseBegin.md)**: When headline sensing begins.
- **[OnHeadlinesense.OnFind](../list/shiori-event/headline-rss/OnHeadlinesense.OnFind.md)**: When there is content to read aloud.
- **[OnHeadlinesenseComplete](../list/shiori-event/headline-rss/OnHeadlinesenseComplete.md)**: When headline sensing completes successfully.
- **[OnHeadlinesenseFailure](../list/shiori-event/headline-rss/OnHeadlinesenseFailure.md)**: When headline sensing fails.

## Notes

GET Headline is called twice. The first call is for the old file, and the second is for the new file. However, depending on the implementation, the order may be reversed from old to new, so do not write code that depends on the order.

If you want it to always be displayed, such as during debugging (so that it does not become "no update"), try writing alwaysdisplay,1 in descript.txt (be sure to remove it after debugging).
