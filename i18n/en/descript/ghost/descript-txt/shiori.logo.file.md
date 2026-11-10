# shiori.logo.file,File name

**カテゴリ:** descript.txt

The image file name used as the AI graph background.<br />
When displaying multiple graphs, files with a number appended before the extension are loaded.<br />
Example: if you specify aigraph.png, aigraph0.png, aigraph1.png…<br />
The image size is 288x288px, filling the graph display area.<br />
In dark mode, a file name with \_dark appended is used. In the example above, this would be aigraph0_dark.png. If no such file exists, the image is always displayed in light mode.

**既定値:** ai.png (ai0.png, ai1.png…/ai0_dark.png, ai1_dark.png…), or the baseware's standard background if not found

**対応:** Materia deprecated specification / SSP; multiple files supported from 2.4.26; dark mode from 2.8.56
