# OnHourTimeSignal

**カテゴリ:** Time events

Hourly time signal event. Occurs on the hour (near ? o'clock, 0 minutes, 0 seconds).

If a talk cannot be played, it waits until one can be played. Therefore, **the notification may arrive slightly late.**

- **Reference0**: OS uptime (hours)
- **Reference1**: 1 when clipped, otherwise 0.
- **Reference2**: 1 when overlapping, otherwise 0.
- **Reference3**: Always 1. (Because it waits until a talk can be played)
- **Reference4**: ※SSP only: Time spent idle without any operation (at the OS level), in seconds.

**対応:** SSP
