# scaling

**カテゴリ:** surface braces \> Drawing method

Enlarges or reduces the character window at the specified scale.<br />
Only this drawing method allows decimal values for the X and Y coordinates (e.g. 92.5).<br />
The scale is calculated as follows.<br />
User-specified scale x `\![scaling]` tag scale x currently running scaling animation value 1 x currently running scaling animation value 2 ...<br />
Note 1: Scaling the window is very costly, so do not overuse it.<br />
Note 2: Unless there are exceptional circumstances, failing to return to 100% at the end of an animation may cause bugs.<br />
Note 3: If the feature that disables move is enabled, scaling will also stop working.

**対応:** SSP 2.7.28
