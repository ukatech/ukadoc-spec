# OnTranslate

**カテゴリ:** Other events

An event for SHIORI to also provide MAKOTO's translation function.<br />
It is mainly issued in response to a script being returned to the baseware when a SHIORI Event for a GET command is received.<br />
The script returned to the baseware after SHIORI performs internal operations on the SHIORI Event that triggered OnTranslate is sent back to SHIORI again after the baseware performs operations such as expanding environment variables. SHIORI can then process this script again in some way and return it to the baseware as the final script.<br />
OnTranslate itself does not occur again.

- **Reference0**: Original script.
- **Reference1**: ※SSP only　For communicate, communicate.<br />
  For SSTP SEND, sstp-send.<br />
  For Owned SSTP, owned.<br />
  For non-local SSTP, remote.<br />
  If translation is disabled, notranslate.<br />
  For a script from a plugin, plugin-script<br />
  For an event response from a plugin, plugin-event<br />
  Applicable items are returned separated by commas. ※If none apply, this field is omitted.
- **Reference2**: ※SSP only　Event ID of the event that caused this script. Omitted if the script was not caused by an event.
- **Reference3**: ※SSP only　The above event's Reference, separated by byte value 1. Omitted if the script was not caused by an event.

**対応:** Materia / SSP / CROW / Ninix
