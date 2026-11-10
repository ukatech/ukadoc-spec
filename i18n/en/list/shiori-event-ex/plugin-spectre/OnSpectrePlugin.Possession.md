# OnSpectrePlugin.Possession

**カテゴリ:** Plugin “Spectre”

Occurs 15 seconds after Spectre displays a conversation through this ghost.<br />
Note that this event is not raised directly by the plugin itself; it is called by the ghost through a timerraise tag placed at the end of the conversation.

- **Reference0**: The character’s current “mood,” based on the current conversation pool. One of the following values:
  - dissociated …… A deeply sad and incoherent mood
  - miserable …… A sad or angry mood
  - cheerful …… A happy or relaxed mood
- **Reference1**: Whether the script played was a “spooky text” script. A “spooky text” script uses special text effects that can evoke unease, for example. The value is 1 if it was, or 0 if it was not.<br />
  Currently, “spooky text” scripts are played only when Reference0 is “dissociated.”
