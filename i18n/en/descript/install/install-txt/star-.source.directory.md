# \*.source.directory,Directory Name

**カテゴリ:** install.txt

The directory name within the archive for content to be installed at the same time. ASCII alphanumeric characters are recommended.<br />
Set this when the directory name after installation differs from the directory name within the archive for content to be installed at the same time.<br />
Numbered entries (such as balloon0.source.directory) can also be specified in the same way.

Starting with SSP 2.9.00, you can also specify a relative path that traverses directories within the archive, such as extra\\bal1.<br />
Either「\\」or「/」can be used as a separator. References to parent directories using「..」are not allowed (they are removed).<br />
Before 2.9.00, separators are replaced with「\_」, so only a single-level directory name can be specified.

**既定値:** Directory name set by \*.directory

**対応:** SSP
