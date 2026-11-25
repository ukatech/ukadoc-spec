# `\![timemachine,set,値]`

**カテゴリ:** Uncategorized command

Sets the offset for the virtual change to the current time ("time machine") to the specified value. This shifts the current time visible to ghosts, including properties such as `system.year`, time events such as [OnSecondChange](../../shiori-event/time/OnSecondChange.md), and calendar appointments. This is intended for testing ghosts that depend on dates or times.<br />
This command is effective only when SSP is started with `--allow-timemachine-control`. Otherwise, it does nothing and records a warning in the error log, preventing ghost scripts from changing the global clock. It cannot be executed through unauthorized SSTP (external SSTP).<br />
The offset lasts only for the current session and is not saved in the settings. The command sets the offset to this value rather than adding it to the current offset, so executing the same command repeatedly produces the same result.

- **Value**: The offset, specified in one of the following forms. If the value is omitted or cannot be interpreted, the command records a warning in the error log and does nothing.
  - `+秒` / `-秒`: The offset itself, in seconds. The sign is required. Examples: `+86400` (one day ahead), `-3600` (one hour behind)
  - `0`: Sets the offset to 0, leaving the time at the actual time.
  - An ISO8601 date and time: Calculates the difference from the actual time and uses it as the offset. If no zone is specified, the value is treated as local time. The clock does not stop; it continues from the specified date and time. Example: `2026-12-31T23:59:50`

The offset can be up to approximately 200 years in either direction. Fractions of a second are truncated.<br />
When time is shifted, if the resulting minute or hour differs from that before the shift, events such as [OnMinuteChange](../../shiori-event/time/OnMinuteChange.md) and [OnHourTimeSignal](../../shiori-event/time/OnHourTimeSignal.md) occur during the next one-second update. This also applies when shifting into the past.<br />
Operations that use the actual time, such as measuring intervals for automatic updates, logging, and communication, are not affected.

!!! note "Note"
    The `--time-shift` startup option can also specify the initial offset. The current offset can be read from the `system.os.timeshift` property.<br />
    To set the offset synchronously without going through a ghost script, use SSTP EXECUTE's [SetTimeShift](../../../spec/sstp/method_execute.md). It requires a value in the same format and the same startup option.

**対応:** SSP 2.9.39

## 記述例

```sakurascript
\![timemachine,set,2026-12-31T23:59:50]
```

Sets the time to 23:59:50 on December 31, 2026, and lets the clock advance from there. Use this, for example, to test events that occur across the turn of the year.

```sakurascript
\![timemachine,set,+86400]
```

Sets the time to one day ahead of the actual time.
