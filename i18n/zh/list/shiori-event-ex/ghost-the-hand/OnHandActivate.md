# OnHandActivate

**カテゴリ:** Ghost “The Hand”

Occurs when The Hand reaches out to touch another ghost or finishes touching it.<br />
While touching, it sends (OnMouseMove|OnMouseDoubleClick|OnMouseWheel) events to the ghost with Sender:The Hand.

- **Reference0**: Normal touch start: NormalStart<br />
  Normal touch end: NormalEnd<br />
  Special move start: SuperStart<br />
  Special move in progress: SuperContinue<br />
  Special move end: SuperEnd<br />
  Homing activated during special move: SuperHoming
- **Reference1**: Hitbox name.<br />
  If stopped, escaped.<br />
  For a special move, 1–4.
- **Reference2**: Event that occurs to the other ghost.<br />
  During normal touch: (OnMouseMove|OnMouseDoubleClick|OnMouseWheel)<br />
  During a special move: number of touches<br />
  At the end of a special move: (MAX touch count|escaped|nocollision|attacked|deleted)
- **Reference3**: Script used when reaching out to touch.<br />
  During a special move, the hitbox name.
- **Reference4**: Shell number.
