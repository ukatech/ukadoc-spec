# Page format

This page explains the IDs of SHIORI Events issued in SHIORI/3.0 and 3.1 (SSP extension definitions).<br />
Events not listed here may be found on the [SHIORI Resource](../shiori-resource/index.md) or [External SHIORI Events](../shiori-event-ex/index.md) pages.

For an explanation of SHIORI Events themselves, refer to the page “[Note: What is a SHIORI Event?](../../memo/shiori-event.md).”

## About the Reference list

SHIORI Events that have References each have a list of their References.<br />
If the number part of a Reference is “\*”, it means the number of References is variable.<br />
In other words, the Reference number is *variable because the number of items depends on the runtime environment*, and all References with a variable number have *the same content format*.<br />
Even in this case, the rule that References are numbered sequentially starting from 0 still applies. For example, if the Reference list contains only entries numbered \*, References with the same format will be listed from 0 through a variable number (as many as the environment requires). If the list includes up to Reference2 and the next entry is Reference\*, References with the same format will be listed from 3 through a variable number.

## About the \[NOTIFY\] label

SHIORI Events marked *\[NOTIFY\]* in their description are normally issued with the NOTIFY command.<br />
If there is no such label, they are normally issued with the GET command.
