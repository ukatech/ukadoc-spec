# Notes

## Update Options

- **checkonly**: Instead of normal update events, the SHIORI event [OnUpdateCheckComplete](../../shiori-event/network-update/OnUpdateCheckComplete.md) is notified, or [OnUpdateCheckFailure](../../shiori-event/network-update/OnUpdateCheckFailure.md) if the check fails. Processing is interrupted as soon as it is possible to determine whether an update is available.<br />
  After all updates are complete, a summary event is raised: [OnUpdateCheckResultEx](../../shiori-event/network-update/OnUpdateCheckResultEx.md) for updateother, and [OnUpdateCheckResult](../../shiori-event/network-update/OnUpdateCheckResult.md) otherwise.
- **testonly**: Update files are downloaded as they would be in a production update, but the actual files are not replaced.<br />
  In SSP, this behaves the same as "Update Full Check", which can be run from the development palette.
- **recovery \[SSP 2.5.26～\]**: Runs the update in recovery mode. In SSP, this behaves the same as updating while holding down the key configured under Settings-Ghost (1)-Enable key to switch to recovery mode.<br />
  All local update definition files are ignored. Only update definitions downloaded from the network are used; these are compared against the hashes of all local files, and files that differ are downloaded.
