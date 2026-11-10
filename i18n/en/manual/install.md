# Installation

For how to create a distribution archive, see “[Creating distribution files](../dev/nar.md)”.

Ghosts are generally distributed as archives with the `nar` extension (NAR, Nanika ARchive).

A nar is just a zip file with a different extension, so some servers may distribute it as a zip.

It is possible to install an lzh archive if you have a decompression DLL, but do not use this format unless there is a compelling reason.

SSP can also install cab files and self-extracting exe files.

An archive can also be installed manually by extracting it, but if `install.txt` is set up correctly, the installer feature can install it automatically by means such as drag and drop.

A nar can be created by dragging and dropping a ghost folder containing install.txt onto the baseware (SSP) itself.

This is equivalent to manually compressing the folder as a zip and renaming it, but take care not to make the folder hierarchy too deep.

When distributing a ghost, take care not to include the profile folders in the ghost and shell folders, save data, and similar files.

The same applies to network updates.

SSP provides `developer_options.txt` for controlling this.

- **For a standard ghost**:

  ```filetree
  +-(myghost)
  　　+-ghost
  　　+-shell
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-readme.txt
  　　+-thumbnail.png
  　　:
  　　:
  ```

  !!! tip "Tip"

      For a *supplement*, archive only the files to be added, keeping the *folder structure exactly as shown above*.

      For example, to add a file named dic_supplement.txt to ghost/master/

      ```filetree
      +-(mysupplement)
      　　+-install.txt
      　　+-developer_options.txt (SSPのみ)
      　　+-ghost
      　　　　+-master
      　　　　　　+-dic_supplement.txt
      ```

      that is how it should be structured.

- **For a standard additional shell**:

  ```filetree
  +-(additional_shell)
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-descript.txt
  　　+-readme.txt
  　　+-thumbnail.png
  　　+-surface*.png
  　　+-surfaces.txt
  　　:
  　　:
  ```

- **For a standard balloon**:

  ```filetree
  +-(myballoon)
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-descript.txt
  　　+-balloonc*.png
  　　+-balloons*.png
  　　+-balloonk*.png
  　　:
  　　:
  ```

- **When bundling a balloon or similar item with a ghost**:

  ```filetree
  +-(myghost)
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-ghost
  　　+-shell
  　　+-(myballoon)
  　　　　+-descript.txt
  　　　　+-balloons0.png
  　　　　:
  　　　　:
  ```

  The same applies to plugins and similar items (if bundling a shell, place it under the regular shell folder instead).

  The included item (the balloon in the example above) does not need install.txt. If present, it is ignored.

- **(SSP only) Package for installing multiple items**:

  ```filetree
  +-(mypackage)
  　　+-install.txt (package用)
  　　+-(myghost1)
  　　　　+-install.txt (myghost1用)
  　　　　+-developer_options.txt (SSPのみ)
  　　　　+-ghost
  　　　　+-shell
  　　　　:
  　　+-(myghost2)
  　　　　+-install.txt (myghost2用)
  　　　　+-developer_options.txt (SSPのみ)
  　　　　+-ghost
  　　　　+-shell
  　　　　:
  ```

  Note that separate install.txt files are required for the package and for each individual item.

  You can bundle any items that can be made into standalone archives, not just ghosts, but take care not to mix items for different targets when they are intended for a specific target, such as shells or supplements.

Similarly, for headline sensors, standalone plugin distributions, and other items, place install.txt in the top-level directory.

- **[install.txt](../descript/install/index.md)**: A text file containing installation settings.

  Without this file, automatic installation by means such as drag and drop will not work.

  It specifies the archive content type, archive name, directory name, and other details.

  See the [linked page](../descript/install/index.md) for details.

- **[developer_options.txt](../descript/install/developer_options.txt/index.md)**: SSP only. Optional.

  Place it in the same location as install.txt.

  However, for a package for installing multiple items, note that it must be placed alongside each content item's install.txt, not alongside the top-level install.txt.

  This file specifies files to exclude when creating a nar in SSP.

  See the [linked page](../descript/install/developer_options.txt/index.md) for details on the format and other information.
