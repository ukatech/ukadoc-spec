# OnOtherGhostTalk

**カテゴリ:** PLUGIN Event

Occurs when a ghost talks.<br />
Can be configured with [otherghosttalk in descript.txt.](../../../descript/plugin/descript-txt/otherghosttalk.md)

- **Reference0**: Ghost name.
- **Reference1**: Name of the ghost's baseware.
- **Reference2**: break if the talk was interrupted.<br />
  communicate for a communicate event.<br />
  sstp-send for an SSTP SEND event.<br />
  owned for Owned SSTP.<br />
  remote for non-local SSTP.<br />
  notranslate if translation is disabled<br />
  plugin-script for a script from a plugin<br />
  plugin-event for an event response from a plugin<br />
  Returns applicable values separated by commas.
- **Reference3**: Event ID of the ghost's talk.
- **Reference4**: Script of what the ghost said.
- **Reference5**: Reference passed to the ghost, separated by byte value 1.

**対応:** SSP
