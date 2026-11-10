# OnSpectrePlugin.Surface

**カテゴリ:** Plugin “Spectre”

Occurs during a Spectre conversation when the currently addressed ghost is asked to change its surface.<br />
Note that this event is not raised directly by the plugin itself; it is called by the ghost through an embedded tag in the conversation.<br />
The expressions included are the [recommended expressions](../../../descript/shell-surfaces/surface-brace/caption_standarddef.md), with a few expressions commonly used by English-language ghosts added.<br />
*Ignore expressions that the ghost’s shell cannot represent accurately, and do not return a response.* The plugin uses this information for its own purposes.

- **Reference0**: The requested expression. One of the following values:

  - normal …… Usually surface0
  - embarrassed …… Usually surface1
  - surprised …… Usually surface2
  - anxious …… Usually surface3
  - discouraged …… Usually surface4
  - smile …… Usually surface5
  - relieved …… Usually surface6. Also called “contented”
  - angry …… Usually surface7
  - sweat …… Usually surface8. Also called “sweat smile” or “cold smile”
  - indignant …… Usually surface9. Also called “embarrassed anger”
  - thinking …… Commonly used by some English-language ghosts. Also called “thoughtful” or “confused”
  - unamused …… Commonly used by some English-language ghosts. Also called “bored”
