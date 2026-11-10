# OnSpectrePlugin.Possession

**カテゴリ:** Plugin "Spectre"

Triggered 15 seconds after Spectre displays a conversation through this ghost.<br />
Note that this event is not triggered directly by the plugin itself, but is called by the ghost through a timerraise tag placed at the end of the conversation.

- **Reference0**: The character's current "mood", based on the current conversation pool. It takes one of the following values:
  - dissociated …… A deeply sad and incoherent mood
  - miserable …… A sad or angry mood
  - cheerful …… A happy or relaxed mood
- **Reference1**: Whether the script played was a "spooky text" script. A "spooky text" script has special text effects that evoke a sense of unease, for example. 1 if so, 0 otherwise.<br />
  Currently, "spooky text" scripts are played only in scenes where Reference0 is "dissociated".
