# \*.source.directory,Directory name

**カテゴリ:** install.txt

Directory name inside the archive for content to be installed at the same time. Half-width alphanumeric characters are recommended.<br />
Set this when the directory name after installation differs from the directory name inside the archive for content to be installed at the same time.<br />
Numbered entries (such as balloon0.source.directory) can also be specified in the same way.

From SSP 2.9.00 onward, relative paths that traverse directories inside the archive, such as extra\\bal1, can also be specified.<br />
Either「\\」or「/」can be used as a separator. References to parent directories using「..」are not allowed (they are removed).<br />
Before 2.9.00, separators are replaced with「\_」, so only single-level directory names can be specified.

**既定値:** Directory name set with \*.directory

**対応:** SSP
