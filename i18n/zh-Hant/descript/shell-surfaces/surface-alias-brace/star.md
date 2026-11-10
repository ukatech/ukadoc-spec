# \*,\[\*\]

**カテゴリ:** surface.alias brace

Assigns an arbitrary alias ID to a surface ID.<br />
For example, setting 驚き,\[2\] means that `\s[驚き]` is equivalent to `\s[2]`.<br />
Multiple surfaces can also be specified as a comma-separated list, such as 1,\[1,11,21\].<br />
In this case, `\s[1]` randomly selects one of 1, 11, and 21.

**既定値:** No behavior

**対応:** Materia / SSP / CROW
