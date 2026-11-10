# Supplement: What Is a SHIORI Event?

## About This Page

This page provides an overview of “SHIORI Event.”

The following article is *not* a proper SHIORI/3.0 specification; it is only a general guide to help you understand the underlying concepts.

For explanations of individual SHIORI Events, see the list on the “[SHIORI Event](../list/shiori-event/index.md)” page.

## 目次

- [What Is a SHIORI Event (栞イベント)?](shiori-event.md#shiori-event栞イベントとは)
- [Reference](shiori-event.md#referenceリファレンス)
- [GET and NOTIFY Commands](shiori-event.md#getコマンドとnotifyコマンド)

## What Is a SHIORI Event (栞イベント)?

[![A ghost runs as a result of interaction between the baseware and the ghost (SHIORI)](../assets/image/shiori-event.jpg)](../assets/image/shiori-event.jpg)

*From startup until the ghost starts running*

What does it mean for a ghost to run (talk, change its expression, etc.)?

Broadly speaking, this functionality is achieved through cooperation between the *baseware* (MATERIA, CROW, SSP, etc.) and *SHIORI* (the component at the core of a ghost).

SHIORI Event is an important keyword for understanding what roles the baseware and SHIORI each play in this process and what happens behind the scenes.

When a ghost runs, the first thing to work is the baseware.

The baseware's first major task is to create the *timing at which the ghost talks or moves*.

The baseware monitors various states, such as the time and mouse input, and issues a notification to the ghost (its core, SHIORI) when a specific change occurs (for example, one second or one minute has elapsed, or the mouse cursor has touched the ghost).

This notification is called a *SHIORI Event*.

SHIORI's work begins here. When SHIORI receives a SHIORI Event, it uses the contents of files called its dictionary, among other things, to *create instructions for the ghost's actions* (these instructions are called Sakura Script).

When SHIORI *sends those instructions back to the baseware*, the baseware receives them, reads their contents, and makes the ghost's actions appear on screen.

In this way, the ghost actually moves on the user's monitor each time a SHIORI Event occurs.

Conversely, *SHIORI cannot make the ghost move until it receives a SHIORI Event*. As a rule, all ghost actions take place in response to SHIORI Events, and are therefore passive.

Even if it may not seem that way at first, note that the “random talk” and “AI talk” features found in many ghosts are implemented by many SHIORI systems through handling [OnSecondChange](../list/shiori-event/time/OnSecondChange.md), which is issued every second (this is ultimately an implementation detail of each SHIORI, so consult the documentation for the relevant SHIORI for details).

## Reference

For many SHIORI Events, along with the SHIORI Event ID (name or type), related information is sent in the form of *Reference*.

For example, consider the ID [OnMouseClick](../list/shiori-event/mouse/OnMouseClick.md), which is issued when a ghost is clicked. Reference provides information such as which scope (the main character, the partner, the third character, and so on) was clicked, which hit area of that scope was clicked, and which button (right, left, wheel, and so on) was used.

For example, SHIORI can use Reference to vary the ghost's actions.

In the case of OnMouseClick, many ghosts change the function or talk they execute depending on which part of which scope was clicked.

*All References are assigned sequential numbers starting from 0*, and References belonging to the same SHIORI Event ID generally *always have the same content associated with the same number*.

This may be easiest to understand by looking at the list of References sent with each ID in the relevant section of the [SHIORI Event list page](../list/shiori-event/index.md).

However, some IDs may have a variable number of References.

For example, if you look at the References for the SHIORI Event called [installedghostname](../list/shiori-event/notify/installedghostname.md) on the SHIORI Event list page, you will see that the numbers are not specified in a form such as “Reference\*”.

installedghostname is a SHIORI Event that occurs immediately after startup, for example, and tells you all the names of ghosts installed in that baseware. Since the number of installed ghosts naturally varies by user, the number of References also varies.

Even when the total number of References is variable, the rule that all References are represented with sequential numbers starting from 0 remains unchanged.

## GET and NOTIFY Commands

[![All SHIORI Events arrive at SHIORI in one of two packages: a “GET command” with a return envelope, or a “NOTIFY command” without one.](../assets/image/shiori-command.png)](../assets/image/shiori-command.png)

*If you compare SHIORI Events to mail...*

In fact, SHIORI Events differ not only in their IDs, but also in the form and purpose of their issuance, which can be one of two types.

One type is the issuance of a SHIORI Event as the timing for the ghost to act, as described above.

This is called a *GET command* and, as the name suggests, is the issuance of a SHIORI Event for the baseware to receive (get) instructions for actions (Sakura Script) and other content from SHIORI.

The other type, the *NOTIFY command*, is a little different: a ghost cannot act in response to a SHIORI Event issued with a NOTIFY command.

This is because even if SHIORI sends back instructions for some action in response to a SHIORI Event from a NOTIFY command, the baseware is supposed to ignore them.

The purpose of a NOTIFY command is to notify SHIORI of information (Reference).

Rather than using the information it receives in that SHIORI Event, SHIORI can put it to use for the ghost's future actions.

The previously mentioned [installedghostname](../list/shiori-event/notify/installedghostname.md) is a typical ID issued with a NOTIFY command. SHIORI can use its References to find out which ghosts are installed in the user's environment. Based on that information, a ghost could, for example, create a feature that displays a menu item for calling a particular ghost if that ghost is installed.

One point to note is that the existence of these two commands *does not mean* that all SHIORI Event IDs are divided into two “groups.”

This is because, in principle, *any SHIORI Event ID may be issued as either NOTIFY or GET*. The command type and ID type are independent and have no essential dependency on each other (however, when looking at actual implementations, certain tendencies and patterns can be observed. For details, see the relevant sections of the [SHIORI Event list page](../list/shiori-event/index.md)).
