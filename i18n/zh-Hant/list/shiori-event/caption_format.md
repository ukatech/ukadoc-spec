# Formatting conventions for this page

This page describes each SHIORI Event ID issued in SHIORI/3.0 and 3.1 (SSP extension definitions).<br />
Events not listed here may be covered on the [SHIORI Resource](../shiori-resource/index.md) or [External SHIORI Events](../shiori-event-ex/index.md) pages.

For an explanation of SHIORI Events themselves, see the “[Note: What is a SHIORI Event?](../../memo/shiori-event.md)” page.

## Reference list

SHIORI Events that have References each have a list of their References.<br />
If the number portion of a Reference is “\*”, it indicates an indeterminate number of References.<br />
In other words, the number of those References is *indeterminate because it varies depending on the operating environment*, and all such References have *the same content format*.<br />
The rule that References are numbered sequentially starting from 0 still applies. For example, if the Reference list contains only an entry numbered \*, References from 0 through an indeterminate number will appear in the same format (in a quantity determined by the environment). If the list contains entries through Reference2 and the next line is Reference\*, References from 3 through an indeterminate number will appear in the same format.

## \[NOTIFY\] notation

SHIORI Events marked *\[NOTIFY\]* in the description are normally issued with the NOTIFY command.<br />
If there is no notation, they are normally issued with the GET command.
