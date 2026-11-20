# Choosing between default and recommended

- **Default**: The balloon to select on first launch or when settings are reset.<br />
  The user can freely change it later.
- **Recommended**: Behaves like "default" but *indicates a stronger dependency*.<br />
  A warning may appear when the user tries to switch to another balloon.<br />
  Setting this without care restricts the user's choices, so *do not specify it without good reason* unless there is a very strong dependency.<br />
  If you only want to discourage the removal of certain balloons, specifying them as "default" also produces a warning.
- **Shell default**: A default can also be specified in [balloon](../../shell/descript-txt/balloon.md) in the shell's descript.txt.<br />
  When switching shells, the balloon switches to the one the user previously selected for that shell, if any; otherwise, it is chosen in the order "ghost recommended > shell default > ghost default".
- **Other**: A "recommended" relationship can also be set from the balloon side. For details, see [Balloon descript.txt entries](../../balloon/index.md).
