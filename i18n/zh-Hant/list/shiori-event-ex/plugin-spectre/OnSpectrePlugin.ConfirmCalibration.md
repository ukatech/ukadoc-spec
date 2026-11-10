# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** Plugin "Spectre"

Triggered when opening the plugin menu if this ghost has not yet been "calibrated". Also triggered when the user selects "recalibrate" for this ghost.<br />
Returning a specific response establishes a handshake that allows the ghost to automatically complete the "calibration" procedure.<br />
The required response is the following tag: `\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
Send this tag with References containing expression data. The References use the same format as those received by the OnSpectrePlugin.Surface event, and may be in any order.<br />
*By default, send only expressions the ghost does not provide.* Expressions not listed are assumed to be available to the plugin.<br />
For ghosts with only a few supported expressions, this behavior can optionally be reversed, so that the plugin only uses expressions listed.<br />
A dedicated Reference is available for ghosts that have no supported expressions at all.<br />
*List any expressions that the ghost's shell cannot represent accurately as References for this tag* (omit them when using the reversed behavior). The plugin uses this information for its own purposes.

- **--option=include**: Use only the listed surfaces (reversed behavior).
- **\_\_NO_EXPRESSIONS\_\_**: Do not use any expressions. Must be sent as reference0.
