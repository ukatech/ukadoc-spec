# `\![set,balloonwait,倍率]`

**カテゴリ:** Balloon, text command

Specifies the multiplier for the speed at which text flows in the balloon (the wait per character).<br />
Number only: 0–100 can be specified. 1 is normal speed. Decimal values are allowed. Example: specifying 1.5 makes it 50% slower.<br />
With a trailing %: 0–10000 can be specified. 100 is normal speed. Integers of 0 or greater only.<br />
With a trailing ms: 0–10000 can be specified. Specifies the wait time per character as an absolute value in milliseconds.

Omitting the value or specifying 1: Reverts to the default value<br />
Specifying 0: Always displays immediately

After the script finishes running, the setting resets to the equivalent of 100%.

**対応:** SSP
