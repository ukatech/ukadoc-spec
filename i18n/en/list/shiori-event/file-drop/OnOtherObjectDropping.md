# OnOtherObjectDropping

**カテゴリ:** File drop event

Occurs when the cursor is over a ghost with an object that cannot be treated as a "file." Examples: Windows "My Computer" and similar objects.

- **Reference0**: Scope number of the dropped character. The main character is 0, the partner is 1, and the third character onward is 2 or higher.
- **Reference1**: Name of the dropped object (affected by the OS language settings).<br />
  If there are multiple objects, they are separated by byte value 1.
- **Reference2**: An ID-like value for the dropped object that is not identified by the OS language settings.<br />
  If there are multiple objects, they are separated by byte value 1. The following are examples on Windows.
  - PC (My Computer) = ::\{20D04FE0-3AEA-1069-A2D8-08002B30309D\}
  - Recycle Bin = ::\{645FF040-5081-101B-9F08-00AA002F954E\}
  - (My) Network = ::\{F02C1A0D-BE21-4350-88B0-7367FC96EF3C\}

**対応:** SSP 2.6.41
