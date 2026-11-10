# scaling

**カテゴリ:** surface brace \> drawing methods

Enlarges or shrinks the character window by the specified magnification.<br />
Only this drawing method allows decimal values for the X and Y coordinates (e.g. 92.5).<br />
The magnification is calculated as follows.<br />
User-specified magnification x `\![scaling]` tag-specified magnification x scaling animation specification 1 currently in progress x scaling animation specification 2 currently in progress ...<br />
Note 1: Window scaling is very costly, so do not overuse it.<br />
Note 2: Unless there is a special reason, not returning to 100% at the end of an animation may cause bugs.<br />
Note 3: If the feature that disables move is enabled, scaling will also stop working.

**対応:** SSP 2.7.28
