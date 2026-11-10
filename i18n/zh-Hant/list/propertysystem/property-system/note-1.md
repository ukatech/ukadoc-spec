# Notes

## ※SHIORI Status header

Multiple values may be returned separated by commas (,), or an empty value may be returned.

- **talking**: A script is currently running (speaking).
- **passive**: In passive mode (`\![enter,passivemode]`).
- **induction**: In induction mode (`\![enter,inductionmode]`).
- **timecritical**: Locked by the `\t` tag.
- **nouserbreak**: In nouserbreak mode (`\![enter,nouserbreak]`).
- **online**: Online (retrieving headline data, synchronizing the time, performing its own network update, etc.).
- **choosing**: Displaying choices using the `\q` or `\__q` tag.
- **minimizing**: Minimized (shown as a task tray icon).
- **opening(type)**: An input window is open.<br />
  The type is one or more of communicate, input, teach, textarea, or dialog, separated by slashes.<br />
  Example: opening(input/dialog)<br />
  ※Slash-separated since SSP 2.3.97; comma-separated before that<br />
  ※textarea supported since SSP 2.9.10
- **balloon(info)**: A balloon is displayed.<br />
  The info lists the displayed balloons in the form (character ID)=(balloon ID). Balloon IDs do not distinguish between left and right (they are always even).<br />
  Example: balloon(0=2/1=0)<br />
  ※Slash-separated since SSP 2.3.97; comma-separated before that

※The Status header can also be retrieved as follows for each SHIORI.

- Kawari……System.Request.Status entry
- YAYA……within the status variable
- Satori……information retrieval variable (Status)
