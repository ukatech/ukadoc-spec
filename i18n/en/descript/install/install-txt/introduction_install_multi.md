# Simultaneous installation

## Overview

In SSP, you can include a balloon or other content in a ghost or shell archive and install them together.<br />
Specify the included content with an entry that begins with “\*.”; the \* part takes the type of content being included.

The following five types can be written in place of \*.

- **balloon**: balloon
- **headline**: headline sensor
- **plugin**: plugin
- **calendar.skin**: calendar appearance file
- **calendar.plugin**: calendar schedule sensor

Note that unlike the notation in [type](type.md), calendar-related entries use *dot separators* (calendar.skin, not calendar skin).

This works regardless of the archive's own [type](type.md), but in practice it is used with archives whose type is *ghost* or *shell*.

## Numbering when including multiple items

To include multiple items of the same type, append a zero-based number after the type in place of \*, such as balloon0, balloon1, … (SSP 2.7.00 and later).

Items are searched for in the order *unnumbered → 0 → 1 → 2…*, and the search *stops when a number is missing*.<br />
Therefore, *do not leave gaps in the numbering*. For example, if you specify only balloon0 and balloon2, the search stops when balloon1 is missing, so balloon2 is not read.

Unnumbered entries and entries numbered 0 are treated separately. If you specify both balloon and balloon0, two balloons will be installed.

[\*.directory](star-.directory.md), [\*.source.directory](star-.source.directory.md), [\*.refresh](star-.refresh.md), and [\*.refreshundeletemask](star-.refreshundeletemask.md) can each be specified independently for every number.

Note that *only the first item is configured as the balloon associated with the ghost or shell*.<br />
The second and subsequent items are installed, but do not become that ghost's default balloon.

## 記述例

To include two balloons and one plugin with a ghost

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
balloon0.directory,example_balloon
balloon0.source.directory,balloon_normal
balloon1.directory,example_balloon_ex
balloon1.source.directory,balloon_special
plugin0.directory,example_plugin
```
