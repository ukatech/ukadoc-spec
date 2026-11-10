# PassiveMode

In PassiveMode, the following restrictions apply.<br />
These restrictions apply to user actions; actions performed with Sakura Script are still possible.

- The selectable items in the owner draw menu are restricted.
- Mail is not checked.
- The headline sensor does not run.
- Auto-change does not run.
- Scripts cannot be interrupted.
- Choices do not time out.
- Balloons do not disappear over time.
- Dropped files are ignored.
- Double-clicking a nar file to install it is also ignored (SSP still installs it, but the ghost does not receive an event).
- OnSurfaceRestore is not issued.
- cantalk is always false. (OnSecondChange and OnMinuteChange events are still issued.)
- The ghost cannot be switched.
- (Materia only:) The communicate box is closed and cannot be opened.
- Cannot be minimized.
- Cannot be closed.
- Network updates cannot be performed.
- The ghost cannot be uninstalled.
