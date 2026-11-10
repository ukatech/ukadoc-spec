# Generation process

updates2.dau / updates.txt can be generated from a ghost's file list using SSP's "Create update files" feature and similar tools.

- **File scanning**: Recursively scans directories. The following files are excluded.

  - Hidden files (`FILE_ATTRIBUTE_HIDDEN`)
  - Files specified by `noupdate` in [developer_options.txt](../../descript/install/developer_options.txt/index.md)
  - Files excluded by .gitignore-format filter files

- **Copying to ghost\\master**: If a `ghost\master` folder exists directly under the directory, the generated update files are also copied there.
