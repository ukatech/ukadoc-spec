# OnHourTimeSignal

**カテゴリ:** Time event

Hourly time signal event. Occurs at the start of each hour (around ? o'clock, 0 minutes, 0 seconds).

If talk playback is unavailable, it waits until talk playback is possible. Therefore, **the notification may arrive slightly later than the scheduled time.**

- **Reference0**: OS uptime (hours)
- **Reference1**: 1 when clipped, otherwise 0.
- **Reference2**: 1 when overlapping, otherwise 0.
- **Reference3**: Always 1. (Because it waits until talk playback is possible)
- **Reference4**: ※SSP only: Time spent idle without any operation (at the OS level), in seconds.

**対応:** SSP
