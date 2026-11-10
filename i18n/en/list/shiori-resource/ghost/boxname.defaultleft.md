# (input box type).defaultleft　(input box type).defaulttop

**カテゴリ:** Ghost information

The initial screen X and Y coordinates of an input box. left is X, and top is Y. These are valid only when both left and top are returned.<br />
If the position where the user moved the input box has been saved, that position takes precedence.<br />
Negative values indicate the distance from the right/bottom edge of the work area on the monitor displaying the main window to the right/bottom edge of the input box. -0 places it exactly at the right/bottom edge.\[2.9.13\]<br />
Prefixing the value with two hyphens makes it a negative coordinate as-is (--100 means coordinate -100).\[2.9.13\]<br />
The box types are as follows: communicatebox、scriptbox、addressbar、teachbox、dateinput、timeinput、ipinput、sliderinput、passwordinput、inputbox

**対応:** SSP
