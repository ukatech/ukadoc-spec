# OnOtherSurfaceChange

**カテゴリ:** Surface event

Notifies when the surface (expression) of another ghost (not this one) changes.<br />
This event is disabled by default to reduce load. To use it, you must enable it in advance with `\![set,othersurfacechange,true]`.

- **Reference0**: Ghost name
- **Reference1**: Ghost Sakura name
- **Reference2**: Window ID whose surface changed (Sakura=0)
- **Reference3**: New surface ID
- **Reference4**: Old surface ID
- **Reference5**: Size of the new surface (coordinates: left, top, right, bottom)

**対応:** SSP / Ninix
