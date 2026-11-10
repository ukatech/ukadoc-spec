# PassiveMode

In passive mode, the following restrictions apply.<br />
These restrictions apply to user operations; they can be performed when invoked through Sakura Script.

- The selectable items in the owner draw menu are restricted.
- Mail is not checked.
- The headline sensor is not run.
- Automatic changes do not occur.
- Scripts are not interrupted.
- Choices do not time out.
- Balloons do not disappear over time.
- Files dropped via DnD are ignored.
- Installation by double-clicking a nar file is also ignored (SSP installs it, but no event is sent to the ghost).
- OnSurfaceRestore is not sent.
- cantalk is always false. (OnSecondChange and OnMinuteChange events are still sent.)
- Ghosts cannot be switched.
- (Materia only:) The communicate box is closed and cannot be opened.
- Cannot be minimized.
- Cannot be closed.
- Network updates cannot be performed.
- Uninstallation cannot be performed.
