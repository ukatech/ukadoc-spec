# OnHandActivate

**カテゴリ:** Ghost “The Hand”

Occurs when The Hand starts or finishes touching another ghost.<br />
While touching, it sends the (OnMouseMove|OnMouseDoubleClick|OnMouseWheel) event to the ghost with Sender:The Hand.

- **Reference0**: Normal touch start: NormalStart<br />
  Normal touch end: NormalEnd<br />
  Special move start: SuperStart<br />
  Special move in progress: SuperContinue<br />
  Special move end: SuperEnd<br />
  Homing activated during special move: SuperHoming
- **Reference1**: Collision region name.<br />
  If interrupted, escaped.<br />
  For a special move, 1–4.
- **Reference2**: Event triggered for the other party.<br />
  Normal: (OnMouseMove|OnMouseDoubleClick|OnMouseWheel)<br />
  During a special move: number of touches<br />
  At the end of a special move: (MAX touch count|escaped|nocollision|attacked|deleted)
- **Reference3**: Script used when moving in to touch.<br />
  During a special move, the collision region name.
- **Reference4**: Shell number.
