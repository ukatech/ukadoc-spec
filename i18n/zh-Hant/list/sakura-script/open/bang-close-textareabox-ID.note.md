# InputBox options

Specify in the form ○○. They work even if not all options are specified.

- **--option=(noclose|noclear)**: noclose: Keep the inputbox open after input.<br />
  noclear: Keep displaying the inputbox after input without clearing its contents.<br />
  Specify together with noclose (example: `\![inputbox,入力内容,,,--option=noclose,--option=noclear]`).<br />
  noclear has no effect on inputboxes that do not accept text (sliderinput,dateinput,timeinput,ipinput).
- **--text=default display**: The string to display initially.<br />
  For sliderinput: initial value, minimum, maximum / for dateinput: year, month, day / for timeinput: hour, minute, second
- **--placeholder=prompt \[2.9.10\]**: A string displayed faintly only when the input field is empty, indicating what to enter (equivalent to HTML's placeholder). It disappears when text is entered and reappears when the field is empty again.<br />
  Unlike --text=, it is not included in the input and is not counted toward the character limit of --limit=.<br />
  The text color can be set with the balloon's [communicatebox.placeholder.color](../../../descript/balloon/descript-txt/communicatebox.placeholder.color.r.md). If not specified, the color is shifted toward the input field's background color and its saturation is further reduced.<br />
  Valid for inputbox, passwordinput, and textareabox (passwordinput also displays the text as entered, without masking it). In textareabox, `\1` represents a line break.
- **--timeout=timeout in milliseconds**: The time until the input box closes automatically. It does not close if a value of zero or less is specified.
- **--balloon=ID**: Specify the ID to use in place of ? in balloonc?.png/txt to use the image corresponding to that ID.<br />
  If not specified, the ID is determined by default for each input box. (SSP 2.6.23)
- **--limit=character input limit**: Limit the number of characters that can be entered in the input box.
- **--reference=additional information**: Add the specified information to Reference3 of OnUserInput, or to Reference2 and later of the specified event beginning with On.
