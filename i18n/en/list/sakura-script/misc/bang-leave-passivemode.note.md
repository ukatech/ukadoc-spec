# PassiveMode

In passive mode, the following restrictions apply.<br />
These restrictions apply to user operations; actions performed using Sakura Script are still possible.

- The selectable items in the owner-draw menu are restricted.
- Mail is not checked.
- The headline sensor does not run.
- Auto-change does not run.
- Scripts are not interrupted.
- Choices do not time out.
- Balloons do not disappear over time.
- Dropped files are ignored.
- Installing by double-clicking a nar file is also ignored (in SSP, the installation still occurs, but the ghost does not receive an event).
- OnSurfaceRestore is not issued.
- cantalk is always false. (OnSecondChange and OnMinuteChange events are still issued.)
- The ghost cannot be changed.
- (Materia only:) The communicate box is closed and cannot be reopened.
- It cannot be minimized.
- It cannot be closed.
- Network updates cannot be performed.
- Uninstallation cannot be performed.
