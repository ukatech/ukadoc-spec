# Notes

## ※SHIORI Status header

Multiple values may be returned separated by commas (,), or an empty value may be returned.

- **talking**: A script is currently running (the ghost is talking).
- **passive**: In passive mode (`\![enter,passivemode]`).
- **induction**: In induction mode (`\![enter,inductionmode]`).
- **timecritical**: Locked by the `\t` tag.
- **nouserbreak**: In nouserbreak mode (`\![enter,nouserbreak]`).
- **online**: Online (for example, while retrieving headline data, synchronizing the time, or performing a network update).
- **choosing**: Displaying choices via the `\q` or `\__q` tag.
- **minimizing**: Minimized (converted to a task tray icon).
- **opening(type)**: An input window is open.<br />
  The type is one of communicate, input, teach, textarea, and dialog; the open types are listed, separated by slashes.<br />
  Example: opening(input/dialog)<br />
  ※Slashes are used starting with SSP 2.3.97; earlier versions use commas<br />
  ※textarea is available starting with SSP 2.9.10
- **balloon(info)**: A balloon is displayed.<br />
  The info lists the displayed balloons in the format (character ID)=(balloon ID). Balloon IDs do not distinguish left from right (they are always even).<br />
  Example: balloon(0=2/1=0)<br />
  ※Slashes are used starting with SSP 2.3.97; earlier versions use commas

The Status header can also be retrieved for each SHIORI as follows.

- Kawari……System.Request.Status entry
- YAYA……inside the status variable
- Satori……information retrieval variable (Status)
