# OnSecondChange

**カテゴリ:** Time event

Occurs every second.

When a talk cannot be played, the event is notified with Reference3 set to 0 via NOTIFY. **The returned script is ignored.**

- **Reference0**: OS uptime (hour)
- **Reference1**: 1 when clipped, otherwise 0.
- **Reference2**: 1 when overlapping, otherwise 0.
- **Reference3**: 1 when a talk can be played, otherwise 0.
- **Reference4**: ※SSP only: Time spent idle (at the OS level), in seconds.

**対応:** Materia / SSP / CROW / Ninix
