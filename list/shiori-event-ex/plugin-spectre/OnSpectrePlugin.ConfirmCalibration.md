# OnSpectrePlugin.ConfirmCalibration

**カテゴリ:** プラグイン「Spectre」

Occurs upon opening the plugin menu if this ghost is not yet "calibrated". Also occurs any time the user chooses to "racalibrate" this ghost.<br />
Returning a specific response completes a handshake that allows the ghost to complete the "calibration" step automatically.<br />
The required response is the following tag: `\![raiseplugin,Spectre,OnCustomCalibrationConfirm]`<br />
Within this tag, references should be sent containing expression data. The references should be written the same as the ones received in the OnSpectrePlugin.Surface event, and may be written in any order.<br />
*By default, only expressions that the ghost does not provide should be sent.* The plugin assumes that any expressions not listed are present.<br />
For ghosts with few compatible expressions, an option may be used to invert this behavior, and make the plugin use only expressions that are listed.<br />
For ghosts with no compatible expressions, a special reference is provided.<br />
*Expressions which the ghost's shell cannot produce accurately should be listed as references in this tag* (or should be omitted, if using the inverted behavior), as the plugin will use this information for its own purposes.

- **--option=include**: Only surfaces that are listed will be used. (Inverted behavior.)
- **\_\_NO_EXPRESSIONS\_\_**: No expressions will be used. Must be sent as reference0.
