# PLUGIN/2.0

Last modified: 2013-08-10

Reference: [PLUGIN/1.0](http://usada.sakura.vg/contents/plugin.html) (external site)

## Preface

PLUGIN/2.0 is a revised version of the old specification (1.0). It is implemented in SSP.

This specification is under development and may undergo major changes.

## Version Design Philosophy and Impact Assessment

### Design Philosophy

The specification has been revised to make it easy to interact with the baseware and ghosts, and to consolidate the “convenience features” among those that had become fragmented across ghosts as SAORI modules, improving convenience for users.

It is probably better to shift the burden from plugin developers to the execution environment... probably.

### Runtime

Be prepared, as this specification assumes that various burdens will be shifted to the runtime (laugh).

### Plugin Authors

A request export is newly defined for calling, so there is no need to consider conflicts with PLUGIN/1.0.

Notifying ghosts of scripts, events, and so on becomes much easier.

### Ghost Authors

Even if a ghost does not support a particular plugin, the default script specification (described below) prevents anything catastrophic from happening.

If you absolutely do not want the default script to spoil the atmosphere, add support...

### Version Impact Assessment

It is convenient and easy to handle the features that had become scattered across ghosts together.

## Components

Two files are required: the configuration file “descript.txt” and a DLL file.

## DLL

See the [DLL page](dll.md).

*※YAYA/KAWARI as plugin users and module authors can skip this.*

## Request Specification

A typical request example is as follows. ※Line ending = CR+LF

```
GET PLUGIN/2.0
ID: OnGhostChange
Charset: UTF-8
Reference0: 54
```

```
NOTIFY PLUGIN/2.0
ID: OnMenuExec
Charset: UTF-8
Sender: 晶子
Reference0: 17982
```

The request ends with a blank line. As with other DLL specifications, it is not necessarily null-terminated, so be careful.

The PLUGIN/2.0 format is basically based on the SHIORI/3.0 specification.<br />
It consists of an ID header identifying the event and a Reference header containing any number of additional pieces of information (eight or more are also allowed).<br />
The contents of Reference vary depending on the ID.

If you want to include line breaks or similar in the contents of Reference and other fields, or want to require that they be included, \*strongly recommend\* specifying that only the characters to be escaped should be URL-encoded, as in %8f%73 (this is not part of the specification).

If the request is called according to the ghost-side calling specification described below, the contents of Sender will be the ghost name.<br />
If it is called by the baseware, the Sender header itself will be absent or set to an empty string.<br />
Note that it will not contain “the name of the baseware (such as SSP or CROW),” as it does in SHIORI.

For the types of requests (IDs) that are notified, see the [PLUGIN Event page](../list/plugin-event/index.md).

## Response Specification

A response example is as follows. ※Line ending = CR+LF

```
PLUGIN/2.0 200 OK
Charset: Shift_JIS
Target: 54
Event: OnResourceLow
EventOption: notify
Reference0: 19
Reference1: 31
Reference2: 65
Script: すくりぷと～
ScriptOption: nobreak,notranslate
```

※Only for runtimes that support multiple ghosts running※ If a currently running ghost matches Target, the response is processed by that ghost.<br />
If "\_\_SYSTEM_ALL_GHOST\_\_" is specified, the response is sent to “all currently running ghosts.”

If there is no match, or nothing is specified, the response is processed by an appropriate single ghost, depending on the runtime.<br />
Also, if called according to the ghost-side calling specification described below, the response is returned to the calling ghost unless explicitly specified by the Target header.

※Runtimes that do not support this feature have only one ghost, so that ghost is called every time.

### Event/Reference

The Event and Reference headers specify events to send to the ghost.<br />
If the ghost does not respond to them, the Script header, which specifies the default script, is played.

### ScriptOption

ScriptOption specifies options that apply only to the contents of the Script header.

- **notranslate**: Do not pass through the ghost's translate mechanism
- **nobreak**: Run the specified script after the current utterance finishes, without interrupting it

### EventOption

EventOption specifies options that apply only to the contents of the Event header.

- **notify**: Notify the ghost of the specified event using notify

Event, EventOption, Reference, Target, Script, and ScriptOption are all optional.<br />
For example, if you only want to send an event and do not need a default script, omit the Script/ScriptOption headers.<br />
※To send only a script, do the reverse.

## Plugin ID

See the [Plugin configuration ID section](../descript/plugin/descript-txt/id.md).

## descript.txt

See the [Plugin configuration page](../descript/plugin/index.md).

## Ghost-Side Extensions

### Script Extensions

```
\![raiseplugin,プラグイン名またはID,イベント,Reference0...]
\![notifyplugin,プラグイン名またはID,イベント,Reference0...]
```

Sends the specified event to the specified plugin. Unless a Target is specified on the plugin side (system_any), the plugin's response is preferentially routed to the ghost that issued raiseplugin, so it can also be used like a SAORI.

The sending command is GET for [`\![raiseplugin]`](../list/sakura-script/event/bang-raiseplugin-ID-r0-r1-r2.md) and NOTIFY for [`\![notifyplugin]`](../list/sakura-script/event/bang-notifyplugin-ID-r0-r1-r2.md).

### SHIORI Event Extensions

See the [installedplugin entry](../list/shiori-event/notify/installedplugin.md).
