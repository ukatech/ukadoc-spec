# OnOtherObjectDropping

**カテゴリ:** File drop event

Occurs when an item that cannot be treated as a "file" is hovered over the ghost. Example: Windows "My Computer", etc.

- **Reference0**: Scope number of the dropped character. The main character is 0, the partner is 1, and the third character onward is 2 or higher.
- **Reference1**: Name of the dropped item (affected by the OS language settings).<br />
  If there are multiple items, they are separated by byte value 1.
- **Reference2**: An ID-like value for the dropped item that is not identified by the OS language settings.<br />
  If there are multiple items, they are separated by byte value 1. Examples on Windows follow.
  - PC (My Computer) = ::\{20D04FE0-3AEA-1069-A2D8-08002B30309D\}
  - Recycle Bin = ::\{645FF040-5081-101B-9F08-00AA002F954E\}
  - (My) Network = ::\{F02C1A0D-BE21-4350-88B0-7367FC96EF3C\}

**対応:** SSP 2.6.41
