# OnSpectrePlugin.Possession

**カテゴリ:** プラグイン「Spectre」

Occurs 15 seconds after Spectre displays a dialogue through this ghost.<br />
Note that this event does not come directly from the plugin itself, but rather is called from the ghost side by a timerraise tag placed at the end of dialogues.

- **Reference0**: The current "mood" of the character, based on the current dialogue pool. May be one of the following values:
  - dissociated …… A very sad and incoherent mood
  - miserable …… A sad or angry mood
  - cheerful …… A happy or relaxed mood
- **Reference1**: Whether the script that was played was a "spooky text" script, e.g., a script with special text effects to evoke a feeling of unease. 1 if true, 0 if false.<br />
  Note that "spooky text" scripts are currently only played in situations where Reference0 is "dissociated".
