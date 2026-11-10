# insert,ID

**カテゴリ:** surface brace \> drawing method

Insert the dressup group with the specified ID (the number in animation\*の\*の番号) at that position.< br />
This method is intended for dressup; using it with animations or elements that are not dressups is undefined.<br />
For example, if a dressup A has a structural positional relationship with another dressup B in which some parts are in front and others behind, inserting dressup B with insert between the frames of dressup A that are behind and those that are in front allows a natural front-to-back display. At this time, the integrity of the display is maintained regardless of whether dressup B is visible or hidden.<br />
It is also possible to insert into an insert destination (nesting).<br />
However, this only *reserves the display order of dressups A and B*; it does not forcibly display dressup B.<br />
Whether dressup B is actually displayed depends on whether dressup B is enabled or disabled.

**対応:** Materia / SSP
