# InputBox options

Specify in the form ○○. All options are optional.

- **--option=(noclose|noclear)**: noclose: Keep the inputbox open after input.<br />
  noclear: Keep displaying the input without clearing it after input.<br />
  Specify this together with noclose (example: `\![inputbox,入力内容,,,--option=noclose,--option=noclear]`).<br />
  noclear has no effect on inputboxes that do not accept text (sliderinput, dateinput, timeinput, ipinput).
- **--text=default display**: The string to display initially.<br />
  For sliderinput: initial value, minimum, maximum / for dateinput: year, month, day / for timeinput: hour, minute, second
- **--placeholder=guidance text \[2.9.10\]**: A string displayed faintly only when the input field is empty, indicating what to enter (equivalent to the HTML placeholder). It disappears when text is entered and reappears when the field is empty again.<br />
  Unlike --text=, this is not included in the input and is not counted toward the character limit set by --limit=.<br />
  The text color can be set with the balloon's [communicatebox.placeholder.color](../../../descript/balloon/descript-txt/communicatebox.placeholder.color.r.md). If not specified, the input text color is shifted toward the background color and its saturation is further reduced.<br />
  Valid for inputbox, passwordinput, and textareabox (passwordinput also displays the text as-is, without masking it). In textareabox, `\1` represents a line break.
- **--timeout=timeout in milliseconds**: How long to wait before automatically closing the input box. A value of zero or less prevents it from closing.
- **--balloon=ID**: Specify an ID to use the corresponding image in place of the ? in balloonc?.png/txt.<br />
  If not specified, the default ID for each input box is used. (SSP 2.6.23)
- **--limit=maximum input length**: Limit the number of characters that can be entered in the input box.
- **--reference=additional information**: Add the specified information to OnUserInput's Reference3, or to Reference2 and later for a specified event that starts with On.
