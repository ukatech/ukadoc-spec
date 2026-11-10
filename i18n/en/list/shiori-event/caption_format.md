# Page Format

This page describes each SHIORI Event ID issued in SHIORI/3.0 and 3.1 (SSP extended definitions).<br />
Events not listed here may be described on the [SHIORI Resource](../shiori-resource/index.md) or [External SHIORI Events](../shiori-event-ex/index.md) pages.

For an explanation of SHIORI Events themselves, see the page “[Notes: What is a SHIORI Event?](../../memo/shiori-event.md).”

## About the Reference List

For SHIORI Events that have References, a list of their References is provided.<br />
If the number portion of a Reference is “\*”, it means the number of References is variable.<br />
In other words, the Reference number is *variable because the number of items depends on the operating environment*, and all such variable References have *the same content format*.<br />
Even in this case, the rule that References are numbered sequentially starting at 0 still applies. For example, if the Reference list contains only entries numbered \*, References in the same format are listed from 0 through a variable number (depending on the environment); if the list includes up to Reference2 and the next line is Reference\*, References in the same format are listed from 3 through a variable number.

## About the \[NOTIFY\] Label

A SHIORI Event marked *\[NOTIFY\]* in its description is normally issued with the NOTIFY command.<br />
If no such label is present, it is normally issued with the GET command.
