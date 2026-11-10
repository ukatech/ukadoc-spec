# `\![set,balloonwait,倍率]`

**カテゴリ:** balloon, text command

Specifies the multiplier for the speed at which text flows in the balloon (the wait time per character).<br />
Numbers only: accepts 0–100. 1 means normal speed. Decimal values are allowed. Example: specifying 1.5 makes it 50% slower.<br />
With a % suffix: accepts 0–10000. 100 means normal speed. Integers of 0 or greater only.<br />
With an ms suffix: accepts 0–10000. Specifies the absolute wait time per character in milliseconds.

Omitting the value or specifying 1: restores the default value<br />
Specifying 0: always displays text immediately

After the script finishes executing, it resets to the equivalent of a 100% specification.

**対応:** SSP
