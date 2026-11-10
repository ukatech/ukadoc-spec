# OnTranslate

**カテゴリ:** Other events

An event that allows SHIORI to also handle MAKOTO's translation function.<br />
It is issued mainly in response to a script being returned to the baseware when SHIORI handles a GET command's SHIORI Event.<br />
The script returned to the baseware after SHIORI-internal processing of the SHIORI Event that triggered OnTranslate is sent back to SHIORI after the baseware expands environment variables and performs other processing. SHIORI can then process this script again and return it to the baseware as the final script.<br />
OnTranslate itself does not occur again.

- **Reference0**: Original script.
- **Reference1**: ※SSP only. For communicate, communicate.<br />
  For SSTP SEND, sstp-send.<br />
  For Owned SSTP, owned.<br />
  For non-local SSTP, remote.<br />
  If translation is disabled, notranslate.<br />
  For a script from a plugin, plugin-script<br />
  For an event response from a plugin, plugin-event<br />
  Applicable values are returned as a comma-separated list. ※If none apply, the entry is omitted.
- **Reference2**: ※SSP only. Event ID that caused this script. Omitted if the script was not caused by an event.
- **Reference3**: ※SSP only. The Reference of the event above, separated by byte value 1. Omitted if the script was not caused by an event.

**対応:** Materia / SSP / CROW / Ninix
