# OnHandActivate

**カテゴリ:** Ghost “The Hand”

Occurs when The Hand reaches out to touch another ghost or finishes touching it.<br />
While touching, it sends the ghost (OnMouseMove|OnMouseDoubleClick|OnMouseWheel) events with Sender:The Hand.

- **Reference0**: Start of normal touch: NormalStart<br />
  End of normal touch: NormalEnd<br />
  Start of special move: SuperStart<br />
  During special move: SuperContinue<br />
  End of special move: SuperEnd<br />
  Homing activated during special move: SuperHoming
- **Reference1**: Collision area name.<br />
  If stopped, this is escaped.<br />
  For a special move, this is 1–4.
- **Reference2**: Event that occurs for the other ghost.<br />
  During normal touch: (OnMouseMove|OnMouseDoubleClick|OnMouseWheel)<br />
  During a special move: Number of touches<br />
  At the end of a special move: (MAX number of touches|escaped|nocollision|attacked|deleted)
- **Reference3**: Script used when reaching out to touch.<br />
  During a special move, this is the collision area name.
- **Reference4**: Shell number.
