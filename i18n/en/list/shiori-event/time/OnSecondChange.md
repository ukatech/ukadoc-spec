# OnSecondChange

**カテゴリ:** Time event

Occurs every second.

If talk playback is unavailable, the event is notified with Reference3 set to 0 using NOTIFY. **The returned script is ignored.**

- **Reference0**: OS uptime (hours)
- **Reference1**: 1 when clipped, otherwise 0.
- **Reference2**: 1 when overlapping, otherwise 0.
- **Reference3**: 1 when talk playback is possible, otherwise 0.
- **Reference4**: ※SSP only: Time spent idle without any operation (at the OS level), in seconds.

**対応:** Materia / SSP / CROW / Ninix
