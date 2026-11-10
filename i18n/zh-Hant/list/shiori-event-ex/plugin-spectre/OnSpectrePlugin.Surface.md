# OnSpectrePlugin.Surface

**カテゴリ:** Plugin "Spectre"

Triggered during a Spectre conversation when a request is made to change the surface of the ghost currently being addressed.<br />
Note that this event is not triggered directly by the plugin itself, but is called by the ghost through an embedded tag in the conversation.<br />
The expressions included are those in [recommended expressions](../../../descript/shell-surfaces/surface-brace/caption_standarddef.md), with a few additions commonly used by English-speaking ghosts.<br />
*Ignore any expressions the ghost's shell cannot represent accurately, and do not return a response.* The plugin uses this information for its own purposes.

- **Reference0**: The requested expression. It takes one of the following values.

  - normal …… Usually surface0
  - embarrassed …… Usually surface1
  - surprised …… Usually surface2
  - anxious …… Usually surface3
  - discouraged …… Usually surface4
  - smile …… Usually surface5
  - relieved …… Usually surface6. Also called "contented"
  - angry …… Usually surface7
  - sweat …… Usually surface8. Also called "sweat smile" or "cold smile"
  - indignant …… Usually surface9. Also called "embarrassed anger"
  - thinking …… Commonly used by some English-speaking ghosts. Also called "thoughtful" or "confused"
  - unamused …… Commonly used by some English-speaking ghosts. Also called "bored"
