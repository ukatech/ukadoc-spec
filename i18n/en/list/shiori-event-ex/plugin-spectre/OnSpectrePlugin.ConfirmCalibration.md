# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** Plugin “Spectre”

Occurs when the plugin menu is opened if this ghost has not yet been “calibrated.” It also occurs when the user selects “recalibrate” for this ghost.<br />
Returning a specific response completes a handshake that allows the ghost to complete the “calibration” process automatically.<br />
The required response is the following tag: `\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
Send this tag with References containing expression data. The References use the same format as those received by the OnSpectrePlugin.Surface event, and their order does not matter.<br />
*By default, send only expressions that the ghost does not provide.* Expressions not listed are assumed to be available.<br />
For ghosts with few supported expressions, this behavior can optionally be reversed, so that the plugin uses only the expressions in the list.<br />
A special Reference is available for ghosts that do not have any supported expressions.<br />
*List as References for this tag any expressions that the ghost’s shell cannot represent accurately* (omit them when using the reversed behavior). The plugin uses this information for its own purposes.

- **--option=include**: Use only the listed surfaces (reversed behavior).
- **\_\_NO_EXPRESSIONS\_\_**: Do not use any expressions. This must be sent as reference0.
