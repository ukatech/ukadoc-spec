# OnPokerNotify

**カテゴリ:** Ghost “Tabletop Yuugi”

This event does not require a response.

- **Reference0**: Protocol version (POKER/1.0)

## Additional information from Reference1 onward in POKER/1.0

- **Reference1**: game_start
- **Reference\***: Names of ghosts that joined

- **Reference1**: round_start
- **Reference2**: Blind amount
- **Reference\***: Ghost name (byte value 1) stack

- **Reference1**: hand
- **Reference2**: Information about the dealt card
- **Reference3**: Information about the dealt card<br />
  The suit is one of four initials (S,H,C,D), followed by a number.<br />
  Example:<br />
  Reference2: S1<br />
  Reference3: H12<br />
  This format is also used for FLIP.

- **Reference1**: flip
- **Reference2**: Current pot
- **Reference\***: Community card information<br />
  For a pre-flop, Reference3 onward does not exist.

- **Reference1**: blind_bet
- **Reference2**: Forced bet amount<br />
  Notifies that a forced bet was made as SB or BB.

- **Reference1**: bet (information about the player who took an action and the bet.)
- **Reference2**: Current total bet amount
- **Reference3**: Current bet amount
- **Reference4**: Ghost name of the player who took the action
- **Reference5**: Action taken

- **Reference1**: show_down (Card information is sent at showdown.)
- **Reference\***: Ghost name (byte value 1) first card (byte value 1) second card

- **Reference1**: round_result (Information about the winner of the round and the participants’ remaining stacks.)
- **Reference2**: The current round’s winner(s), separated by byte value 1.
- **Reference\***: Ghost name (byte value 1) stack<br />
  There is usually one winner, but there may be two or more.<br />
  Note that a stack reaching 0 is only reported here.

- **Reference1**: game_result
- **Reference2**: Ghost name of the game winner
