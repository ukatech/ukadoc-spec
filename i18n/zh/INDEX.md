# UKADOC Home Page

## About UKADOC

A collection of documents edited by the [UKADOC project](https://github.com/ukatech/ukadoc-spec), a project that aggregates specification documents related to 伺か (Ukagaka).

*The documents here are treated as the official documentation for [SSP](http://ssp.shillest.net/).*

Please send corrections, questions, opinions, requests, and information to [BaguTora Laboratory ToDo](http://ssp.shillest.net/bts/?project=misc&action=top).

The text on this site is available under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.ja) license. You are free to quote, reproduce, and modify it, not only for ghost creation. When doing so, please credit the original author by naming this project (UKADOC project) or linking to this site.

> For offline reading, we provide [ukadoc-spec-offline.zip](https://ukatech.shillest.net/ukadoc-spec/ukadoc-spec-offline.zip), an archive containing the HTML, CSS, JS, and images for this site. You can read it by opening `ukadoc-spec/index.html` after extracting it.
>
> For AI agents, we provide [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt), a guide to finding information. The Markdown source for each page can be retrieved as a `.md` file at the same path as in the repository (e.g.: `https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`).

## Target versions

- [SSP](http://ssp.shillest.net/) latest version (official specifications)
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2 (development version)
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) latest version

## External links

- [伺か development information search](http://ukadev.shillest.net/)
- [SSP startup options (SSP Help)](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [Official 伺か specifications](http://usada.sakura.vg/contents/specification.html)
- [CROW・SSP specifications](http://crow.aqrs.jp/reference/all/)
- [Ooyashima.NET unofficial specifications](http://www.ooyashima.net/db/)
- [Da-debe Wiki specification notes](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## How to use ukadoc

The articles in the sidebar cover the following topics, organized by category.

- **File structure**: Describes the files that make up various 伺か-related content and their directory structures.

  Refer to this section when you want an overview of what files are required or available.

- **Configuration files**: Explains the contents of individual configuration files used by various 伺か-related content.

  You can refer to these explanations when writing configuration files. Examples are provided wherever possible.

- **Sakura Script**: Explains each Sakura Script command, which controls ghost behavior.

  Refer to this section to learn what commands are available and how to use them.

- **Events**: Explains the IDs of events that the baseware notifies SHIORI, PLUGIN, and others about.

  Refer to this section when creating ghosts, PLUGINs, SHIORI, and related content, or when you need information about individual events and their References.

- **Specifications**: Compiles various specifications related to 伺か-related content.

  This section mainly covers information about core system components such as SHIORI, SAORI, and baseware.

- **HowTo**: Introduces basic methods for creating various 伺か-related content.

  However, it is difficult to cover tips for every individual case, so please also look for external sites if you need more specific information.

- **Other**: Includes notes and supplementary articles about specifications for baseware such as SSP.

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
  - [SHIORI Event (external)](list/shiori-event-ex/index.md)
  - [SHIORI Resource](list/shiori-resource/index.md)
- PLUGIN
  - [PLUGIN Event](list/plugin-event/index.md)

### Specifications

- [SHIORI/3.0](spec/shiori3/index.md)
- [SSTP/1.x](spec/sstp/index.md)
- [SAORI/1.0 (external site)](http://www.boreas.dti.ne.jp/~sdn/saori.html)
- [SAORI over DirectSSTP](spec/saori-ex/index.md)
- [PLUGIN/2.0](spec/plugin.md)
- [HEADLINE/2.0](spec/headline.md)
- [DLL](spec/dll.md)
- [FMO/Mutex](spec/fmo-mutex/index.md)
- [Web-related](spec/web/index.md)
- [Specification notes (external site)](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

### HowTo

- [Creating files for distribution](dev/nar.md)
- [Supporting network updates](dev/update.md)
- [Creating a shell](dev/shell.md)
- [Configuring dressup](dev/bind.md)
- [Configuring an owner draw menu](dev/ownerdraw.md)
- [Resolving error messages](dev/shell-error.md)

### Other

- [Supplement: What is a SHIORI Event?](memo/shiori-event.md)
- [Notes](memo/memo.md)
