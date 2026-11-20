# shiori.logo.file,filename

**カテゴリ:** descript.txt

The filename of the image used as the AI graph background.<br />
When displaying multiple graphs, files with numbers appended before the extension are loaded.<br />
Example: if aigraph.png is specified, aigraph0.png, aigraph1.png, etc. are loaded.<br />
An image size of 288x288px fills the graph drawing area.<br />
In dark mode, filenames with \_dark appended are used instead. In the example above, this would be aigraph0_dark.png. If absent, the light-mode image is always displayed.

This can also be specified in the ghost's descript.txt. The shell's setting takes precedence if present; otherwise, the ghost's value is used.

**既定値:** ai.png (ai0.png, ai1.png…/ai0_dark.png, ai1_dark.png…), or the baseware's default background if absent

**対応:** Materia deprecated / SSP multiple files since 2.4.26, dark mode since 2.8.56
