# OnSpectrePlugin.Surface

**カテゴリ:** プラグイン「Spectre」

Occurs during Spectre's dialogues to call for surface changes from the ghost that is currently being spoken to.<br />
Note that this event does not come directly from the plugin itself, but rather is called from the ghost side by embed tags within the dialogues.<br />
The expressions included are the [recommended expressions](../../../descript/shell-surfaces/surface-brace/caption_standarddef.md), plus a few extra that are common in English ghosts.<br />
*Expressions which the ghost's shell cannot produce accurately should be ignored and not return a response*, as the plugin will use this information for its own purposes.

- **Reference0**: The expression being called for. May be one of the following values:

  - normal …… usually surface0
  - embarrassed …… usually surface1
  - surprised …… usually surface2
  - anxious …… usually surface3
  - discouraged …… usually surface4
  - smile …… usually surface5
  - relieved …… usually surface6, also known as "contented"
  - angry …… usually surface7
  - sweat …… usually surface8, also known as "sweat smile" or "cold smile"
  - indignant …… usually surface9, also known as "embarrassed anger"
  - thinking …… common in some English ghosts, also known as "thoughtful" or "confused"
  - unamused …… common in some English ghosts, also known as "bored"
