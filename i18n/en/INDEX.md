# UKADOC Home

## About UKADOC

This document collection is edited by the [UKADOC project](https://github.com/ukatech/ukadoc-spec), a project that compiles specifications related to Ukagaka.

*The documentation here is treated as the official documentation for [SSP](http://ssp.shillest.net/).*

Please send reports of errors, questions, opinions, requests, and information to [Bugtra Research Institute ToDo](http://ssp.shillest.net/bts/?project=misc&action=top).

Administrator: [UKADOC Project](https://github.com/ukatech/ukadoc-spec)

Banner for linking to this site:

![ukadoc banner](assets/image/ukadoc_banner1.png)

The text on this site is available under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.ja). You may quote, reproduce, or modify it freely, whether or not for ghost creation. If you do, please credit the original author by naming this project (UKADOC project) or linking to this site.

> We provide [ukadoc-spec-offline.zip](https://ukatech.shillest.net/ukadoc-spec/ukadoc-spec-offline.zip), an archive containing the HTML, CSS, JS, and image files from this site, for offline reading. You can read the site by opening `ukadoc-spec/index.html` after extracting the archive.
>
> For AI agents, we provide [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt), a guide to finding information. The Markdown source for each page can be retrieved from the `.md` file at the same path as in the repository (for example: `https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`).

## Target versions

- [SSP](http://ssp.shillest.net/) latest version (official specifications)
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2 (development version)
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) latest version

## External links

- [Ukagaka development information search](http://ukadev.shillest.net/)
- [SSP startup options (SSP Help)](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [Official Ukagaka specifications](http://usada.sakura.vg/contents/specification.html)
- [CROW and SSP specifications](http://crow.aqrs.jp/reference/all/)
- [Oyashima.NET unofficial specifications](http://www.ooyashima.net/db/)
- [Da-debe Wiki specification notes](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## How to use UKADOC

The articles in the sidebar cover the following topics, grouped by category.

- **File structure**: Explains the files that make up Ukagaka-related content and its directory structure.

  Refer to this section to get an overview of the files that are required or available.

- **Configuration files**: Explains the contents of individual configuration files used by Ukagaka-related content.

  Refer to this section when writing configuration files. Examples are provided wherever possible.

- **Sakura Script**: Explains the individual commands in Sakura Script, which directs ghost behavior.

  Refer to this section to learn what commands are available and how to use them.

- **Events**: Explains the IDs of events that baseware notifies to SHIORI, PLUGIN, and others.

  Refer to this section when creating ghosts, PLUGINs, or SHIORI, and when you need to learn about individual events or their References.

- **Specifications**: Compiles various specifications related to Ukagaka content.

  This section mainly covers information related to core system components such as SHIORI, SAORI, and baseware.

- **HowTo**: Introduces basic methods for creating Ukagaka-related content.

  However, covering tips for every individual case is impractical, so look for external sites if you need more specific information.

- **Other**: Notes and supplementary articles on the specifications of SSP and other baseware.

## 目次

### File structure

- [Overall structure](manual/directory.md)
- [Ghost](manual/ghost.md)
- [Shell](manual/shell.md)
- [Owner draw menu](manual/owner-draw-menu.md)
- [Installation](manual/install.md)
- [Network update](manual/update.md)
- [Translator](manual/translator.md)
- [Balloon](manual/balloon.md)

### Configuration files

- Ghost
  - [descript.txt](descript/ghost/index.md)
- Shell
  - [descript.txt](descript/shell/index.md)
  - [surfaces.txt](descript/shell-surfaces/index.md)
  - [surfacetable.txt](descript/shell-surfacetable/index.md)
- Balloon
  - [descript.txt](descript/balloon/index.md)
  - [balloon(s/k)\*s.txt](descript/balloon/balloonsoption/index.md)
- Plugin
  - [descript.txt](descript/plugin/index.md)
- Headline
  - [descript.txt](descript/headline/index.md)
- Install/Update
  - [install.txt](descript/install/index.md)
  - [delete.txt](descript/install/delete.txt/index.md)
  - [developer_options.txt](descript/install/developer_options.txt/index.md)
  - [updates2.dau/updates.txt](spec/update-file/index.md)

### Sakura Script

- [SAKURA Script](list/sakura-script/index.md)
- [Property System](list/propertysystem/index.md)

### Events

- SHIORI
  - [SHIORI Event](list/shiori-event/index.md)
  - [SHIORI Event (External)](list/shiori-event-ex/index.md)
  - [SHIORI Resource](list/shiori-resource/index.md)
- PLUGIN
  - [PLUGIN Event](list/plugin-event/index.md)

### Specifications

- [SHIORI/3.0](spec/shiori3/index.md)
- [SSTP/1.x](spec/sstp/index.md)
- [SAORI/1.0 (External site)](http://www.boreas.dti.ne.jp/~sdn/saori.html)
- [SAORI over DirectSSTP](spec/saori-ex/index.md)
- [PLUGIN/2.0](spec/plugin.md)
- [HEADLINE/2.0](spec/headline.md)
- [DLL](spec/dll.md)
- [FMO/Mutex](spec/fmo-mutex/index.md)
- [Web-related](spec/web/index.md)
- [Specification notes (External site)](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

### HowTo

- [Creating files for distribution](dev/nar.md)
- [Supporting network updates](dev/update.md)
- [Creating a shell](dev/shell.md)
- [Configuring dressup](dev/bind.md)
- [Configuring owner draw menus](dev/ownerdraw.md)
- [Resolving error messages](dev/shell-error.md)

### Other

- [Supplement: What is a SHIORI Event?](memo/shiori-event.md)
- [Notes](memo/memo.md)
