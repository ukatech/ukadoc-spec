# insert,ID

**カテゴリ:** surface brace \> drawing method

Inserts the dressup group for the specified ID (the number in animation\*'s \*) at that position.<br />
This method is intended for dressup; its use with non-dressup animations or elements is undefined.<br />
For example, if dressup A has a structure in which it is partly in front of and partly behind another dressup B, inserting dressup B with insert between the frames of A that go behind B and the frames that go in front of B allows the front-to-back relationship to be displayed naturally. In this case, the display remains complete regardless of whether dressup B is visible or hidden.<br />
Insertion into an insert destination (nesting) is also possible.<br />
However, this only *reserves the display order of dressups A and B*; it does not forcibly display dressup B.<br />
Whether dressup B is actually displayed depends on whether dressup B is enabled or disabled.

**対応:** Materia / SSP
