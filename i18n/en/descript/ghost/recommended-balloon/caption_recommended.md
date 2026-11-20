# Default and recommended settings

- **Default**: The selection to use on first launch or when settings are reset.<br />
  The user can change it freely afterward.
- **Recommended**: Behaves like "default", but *indicates a stronger dependency*.<br />
  For example, a warning may appear when the user tries to switch to another balloon.<br />
  Setting this casually restricts the user's choices, so *do not specify it unnecessarily* unless there is a very strong dependency.<br />
  If the only goal is to discourage deletion of a particular balloon, the "default" setting also produces a warning.
- **Shell default**: A default can also be specified in the shell's descript.txt as [balloon](../../shell/descript-txt/balloon.md). Until the user explicitly switches balloons, switching shells also switches the balloon according to the new shell's setting.<br />
  The order of precedence is: balloon explicitly selected by the user > ghost recommendation > shell default > ghost default.
- **Other**: A balloon can also specify a "recommended" relationship. For details, see [Balloon descript.txt entries](../../balloon/index.md).
