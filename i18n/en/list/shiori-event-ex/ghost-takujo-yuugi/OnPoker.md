# OnPoker

**カテゴリ:** Ghost “Tabletop Yuugi”

This event requires a response. Use raiseother or notifyother to respond.

- **Reference0**: Protocol version (POKER/1.0)
- **Reference1**: Server ghost name
- **Reference2**: Server event name

## Additional information from Reference3 onward in POKER/1.0

- **Reference3**: hello (request to join. The request may be declined.)

- **Reference3**: action (Reference4 onward contains the available actions.)
- **Reference\***: The available actions are some of the following six: bet,raise,allin,check,call,fold.<br />
  Note that if no response is sent, fold is performed automatically.<br />
  When betting or raising, the raise amount must also be sent.
