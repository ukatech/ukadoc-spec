# OnPoker

**カテゴリ:** Ghost “卓上誘技”

An event that requires a response. Use raiseother or notifyother to respond.

- **Reference0**: Protocol version (POKER/1.0)
- **Reference1**: Server ghost name
- **Reference2**: Server event name

## Additional information for Reference3 and later in POKER/1.0

- **Reference3**: hello (request to join. The request may be rejected.)

- **Reference3**: action (available actions are in Reference4 and later.)
- **Reference\***: Available actions are some of the following six: bet,raise,allin,check,call,fold.<br />
  Note that if no response is sent, fold is performed automatically.<br />
  When betting or raising, the raise amount must also be sent.
