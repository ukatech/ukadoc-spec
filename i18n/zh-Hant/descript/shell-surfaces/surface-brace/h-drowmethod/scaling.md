# scaling

**カテゴリ:** surface brace \> drawing methods

Enlarges or shrinks the character window by the specified scale factor.<br />
This is the only drawing method that allows decimal values for the X and Y coordinates (e.g., 92.5).<br />
The scale factor is calculated as follows.<br />
User-specified scale x `\![scaling]` tag-specified scale x currently running scaling animation setting 1 x currently running scaling animation setting 2 ...<br />
Note 1: Scaling the window is quite costly, so do not overuse it.<br />
Note 2: Unless there are special circumstances, failing to return to 100% at the end of an animation can cause bugs.<br />
Note 3: If the feature that disables move is enabled, scaling will also stop working.

**対応:** SSP 2.7.28
