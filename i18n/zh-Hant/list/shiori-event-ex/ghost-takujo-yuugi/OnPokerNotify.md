# OnPokerNotify

**カテゴリ:** Ghost “卓上誘技”

An event that does not require a response.

- **Reference0**: Protocol version (POKER/1.0)

## Additional information for Reference1 and later in POKER/1.0

- **Reference1**: game_start
- **Reference\***: Names of ghosts that joined

- **Reference1**: round_start
- **Reference2**: Blind amount
- **Reference\***: Ghost name (byte value 1) stack

- **Reference1**: hand
- **Reference2**: Information about the dealt cards
- **Reference3**: Information about the dealt cards<br />
  The suit is one of the four initials (S,H,C,D), followed by a number.<br />
  Example:<br />
  Reference2: S1<br />
  Reference3: H12<br />
  This format is also used for FLIP.

- **Reference1**: flip
- **Reference2**: Current pot
- **Reference\***: Community card information<br />
  For a pre-flop, Reference3 and later do not exist.

- **Reference1**: blind_bet
- **Reference2**: Forced bet amount<br />
  Notifies that a forced bet was made as the SB or BB.

- **Reference1**: bet (information about the player who acted and the bet.)
- **Reference2**: Current total bet amount
- **Reference3**: Current bet amount
- **Reference4**: Ghost name of the player who acted
- **Reference5**: Action performed

- **Reference1**: show_down (sends card information at showdown.)
- **Reference\***: Ghost name (byte value 1) first card (byte value 1) second card

- **Reference1**: round_result (information about the winner of the round and participants' remaining stacks.)
- **Reference2**: The winner of the current round, separated by byte value 1.
- **Reference\***: Ghost name (byte value 1) stack<br />
  There is generally one winner, but there may be two or more.<br />
  Note that a stack reaching 0 is only reported here.

- **Reference1**: game_result
- **Reference2**: Ghost name of the game winner
