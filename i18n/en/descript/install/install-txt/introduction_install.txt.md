# install.txt

## Overview

See also the page [File structure: “Installation”](../../../manual/install.md).

An installation settings file for Ukagaka/SSP content archives (.nar, etc.), such as ghosts, balloons, and shells. All archives can also be installed manually by extracting them, but the presence of a properly configured install.txt enables the installer feature, allowing installation through simple means such as drag and drop.

## 記述例 and basic usage

For a ghost (balloons and plugins work in much the same way; just change the type value)

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
```

For an additional shell

```
charset,Shift_JIS
name,凡例さんアルティメットフォーム
type,shell
directory,ultimate
accept,凡例さん
```

For a ghost supplement (additional files)

```
charset,Shift_JIS
name,凡例さん猫化パッチ
type,supplement
accept,凡例さん
```

To include a balloon with a ghost

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
balloon.directory,example_balloon
balloon.source.directory,balloon
```

※SSP only: Place this at the top level of a package for installing multiple items<br />
（The install.txt files placed with each included item can use the usual format）

```
charset,Shift_JIS
name,凡例さんファミリー一括入居パッケージ
type,package
```

The charset must be specified on the first line (it can be omitted for Shift_JIS).

name and type are required. directory is also required unless type is supplement or package.<br />
Specify the other entries as needed.

For additional shells and supplements, you can use accept to avoid installing them on an unintended ghost.<br />
This is especially important for supplements, which pose a risk of accidentally overwriting and corrupting unexpected files.<br />
Note that accept uses the *baseware-side name*, not the ghost name.

In SSP, use \*.directory when including a balloon or plugin with a ghost or shell.<br />
For details, see [“Simultaneous installation”](introduction_install_multi.md).

The name is used mainly for the notification content in the Reference of [installation-related SHIORI Events](../../../list/shiori-event/install/OnInstallComplete.md).<br />
Some ghosts use this information to switch to the newly installed item immediately after installation. However, if the actual ghost name in descript.txt differs from the name given in install.txt, this switching may not work correctly.
