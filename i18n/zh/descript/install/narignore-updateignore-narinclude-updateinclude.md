# .narignore / .updateignore / .narinclude / .updateinclude

## .narignore / .updateignore

.narignore/.updateignore allow the .gitignore syntax to be used as-is, providing more flexibility than the developer_options.txt syntax.

For the syntax, consult the [.gitignore manual](https://git-scm.com/docs/gitignore/ja) or ask an LLM (text-generating AI) to generate it by describing what you want to do.

However, unlike .gitignore, these files do not work when placed in a subdirectory. They are effective only when placed directly in the ghost's root directory.

As a special feature exclusive to 伺か, include: directives are available. For example,<br />
include:.narignore<br />
causes the contents of the .narignore file to be processed as if they had been inserted in their entirety at that line.

Relative paths specified in include: are resolved relative to the directory containing the file where the line is written, not the ghost's root directory. Files that are read can themselves contain include: directives; in that case, the base directory is updated each time to the directory containing the currently read file (the base moves from parent to child, then from child to grandchild).

Recursive reading has a limit and can traverse at most 3 levels. include: directives that exceed this depth are rejected. Either / or \\ can be used as the path separator.

For example, if you write include:sub/extra.txt in .narinclude directly under the ghost's root directory, sub/extra.txt is read. If you then write include:foo.txt in extra.txt, sub/foo.txt is read relative to the sub/ directory containing extra.txt, not the ghost's root directory.

**対応:** SSP

## .narinclude / .updateinclude

Whitelist versions of .narignore/.updateignore. Only the items written here are included in update files/NAR.<br />
Unlike gitignore, subdirectories are handled so that, for example, writing only shell/master without writing shell/ still correctly includes the parent directory.

Also, like .narignore/.updateignore and unlike .gitignore, these files do not work when placed in a subdirectory. They are effective only when placed directly in the ghost's root directory.

**対応:** SSP
