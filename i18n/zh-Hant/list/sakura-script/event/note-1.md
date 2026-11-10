# Notes

## Specifying Update Options

- **checkonly**: Instead of the regular update events, the SHIORI event [OnUpdateCheckComplete](../../shiori-event/network-update/OnUpdateCheckComplete.md) is notified, or [OnUpdateCheckFailure](../../shiori-event/network-update/OnUpdateCheckFailure.md) if the update fails. Processing is interrupted as soon as it is possible to determine whether an update is available.<br />
  After all updates have finished, a summary of the results is reported: [OnUpdateCheckResultEx](../../shiori-event/network-update/OnUpdateCheckResultEx.md) for updateother, and [OnUpdateCheckResult](../../shiori-event/network-update/OnUpdateCheckResult.md) otherwise.
- **testonly**: Update files are downloaded as in a production update, but the actual files are not replaced.<br />
  In SSP, this behaves the same as "Update Full Check", which can be run from the development palette.
- **recovery \[SSP 2.5.26～\]**: Runs the update in recovery mode. In SSP, this behaves the same as updating while holding the key configured at Settings - Ghost (1) - Enable recovery mode toggle key.<br />
  All local update definition files are ignored. Only update definitions downloaded from the network are used, and all local files are compared against their hashes; files that differ are downloaded.
