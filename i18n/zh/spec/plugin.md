# PLUGIN/2.0

最后修改：2013-08-10

参考：[PLUGIN/1.0](http://usada.sakura.vg/contents/plugin.html)（外部网站）

## 前言

PLUGIN/2.0是对旧版规范（1.0）的修订版。由SSP实现。

这是一项仍在完善中的规范，可能会有大幅变更。

## 版本的设计理念与影响评估

### 设计理念

进行改进，使其能够轻松地与本体和ghost交互；同时整合以SAORI模块形式分散在各个ghost中的“便利功能”，提升用户的使用便利性。

将负担从plugin开发者转移到运行环境会更好……大概吧。

### 处理系统

本规范以将各种负担转移到处理系统为前提，请做好准备（苦笑）。

### Plugin作者

由于新增了用于调用的request导出函数，因此无需考虑与PLUGIN/1.0冲突的问题。

向ghost发送脚本或事件等通知会变得非常简单。

### Ghost作者

即使未适配特定plugin，也有默认脚本规范（后述），因此不会造成致命问题。

如果无论如何都不想让默认脚本破坏氛围，那就进行适配吧……

### 版本的影响评估

能够将原本分散在各个ghost中的功能群统一处理，非常方便省事。

## 实体

需要两个文件：“descript.txt”和DLL文件。

## DLL

请参阅[DLL页面](dll.md)。

*※YAYA/KAWARI as PLUGIN的使用者和模块作者可以跳过此部分。*

## request规范

典型的请求示例如下。※换行符＝CR+LF

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

以空行结束。与其他DLL规范一样，请注意不一定以零结尾。

PLUGIN/2.0的格式基本遵循SHIORI/3.0规范。<br />
它由表示事件标识符的ID头，以及数量不限（可超过8个）的附加信息Reference头组成。<br />
Reference的内容因ID而异。

如果希望Reference等内容包含换行等字符，或规定必须包含这些字符，\*强烈建议\*仅对需要转义的字符进行URL编码后传递，例如%8f%73（这不是规范要求）。

如果请求是通过后述的ghost侧调用规范发起的，Sender的内容就是ghost名称。<br />
如果是由本体侧调用，Sender头本身会被省略，或者被赋为空字符串。<br />
请注意，这里不会像SHIORI那样填入“本体名称（例如SSP或CROW）”。

有关通知的请求类型（ID），请参阅[PLUGIN Event页面](../list/plugin-event/index.md)。

## response规范

响应示例如下。※换行符＝CR+LF

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

※仅适用于支持多实例的处理系统※ 如果当前正在运行的ghost中有与Target对应的ghost，就由该ghost处理。<br />
指定"\_\_SYSTEM_ALL_GHOST\_\_"时，会通知“所有正在运行的ghost”。

如果没有匹配项，或者没有指定任何内容，则由处理系统选择合适的一个ghost进行处理。<br />
此外，如果请求是通过后述的ghost侧调用规范发起的，除非在Target头中明确指定，否则响应会返回给发起调用的ghost。

※不支持此功能的处理系统只有一个ghost，因此每次都会调用该ghost。

### Event/Reference

Event头和Reference头用于向ghost发送事件。<br />
如果ghost没有响应，便会播放作为默认脚本的Script头。

### ScriptOption

ScriptOption是仅适用于Script头内容的选项。

- **notranslate**: 不经过ghost的翻译处理
- **nobreak**: 不打断当前正在播放的对话，等其播放完毕后再执行指定脚本

### EventOption

EventOption是仅适用于Event头内容的选项。

- **notify**: 通过notify向ghost通知指定事件

Event、EventOption、Reference、Target、Script和ScriptOption都可以省略。<br />
例如，只想发送事件而不需要默认脚本时，请省略Script/ScriptOption头。<br />
※如果只想发送脚本，则反过来处理。

## Plugin ID

请参阅[Plugin设置中的ID项](../descript/plugin/descript-txt/id.md)。

## descript.txt

请参阅[Plugin设置页面](../descript/plugin/index.md)。

## Ghost侧扩展

### 脚本扩展

```
\![raiseplugin,プラグイン名またはID,イベント,Reference0...]
\![notifyplugin,プラグイン名またはID,イベント,Reference0...]
```

向指定的plugin发送指定事件。只要plugin没有指定Target（system_any），来自plugin的响应就会优先分配给执行raiseplugin的ghost，因此也可以像SAORI替代品一样使用。

发送命令在[`\![raiseplugin]`](../list/sakura-script/event/bang-raiseplugin-ID-r0-r1-r2.md)的情况下为GET，在[`\![notifyplugin]`](../list/sakura-script/event/bang-notifyplugin-ID-r0-r1-r2.md)的情况下为NOTIFY。

### SHIORI事件扩展

请参阅[installedplugin项](../list/shiori-event/notify/installedplugin.md)。
