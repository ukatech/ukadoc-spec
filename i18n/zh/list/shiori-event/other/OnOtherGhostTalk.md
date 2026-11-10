# OnOtherGhostTalk

**カテゴリ:** Other events

Occurs when another ghost speaks. Enable it with `\![set,otherghosttalk,true]`.

- **Reference0**: Ghost name.
- **Reference1**: Name of the ghost on the baseware side.
- **Reference2**: If the talk was interrupted, break.<br />
  For communication, communicate.<br />
  For SSTP SEND, sstp-send.<br />
  For Owned SSTP, owned.<br />
  For non-local SSTP, remote.<br />
  If translation is disabled, notranslate<br />
  For scripts from plugins, plugin-script<br />
  For event reactions from plugins, plugin-event<br />
  Applicable values are returned as comma-separated entries.
- **Reference3**: Event ID for the other ghost's talk.
- **Reference4**: Script containing what the other ghost said.
- **Reference5**: Reference passed to the other ghost, separated by byte value 1.

**対応:** SSP / Ninix
