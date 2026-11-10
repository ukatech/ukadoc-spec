# `\![set,balloonwait,倍率]`

**カテゴリ:** balloon, text command

Specifies the multiplier for the speed at which text flows in the balloon (the wait between characters).<br />
Numbers only: 0–100 can be specified. 1 means normal speed. Decimals are allowed. Example: 1.5 specifies a speed 50% slower.<br />
With a % suffix: 0–10000 can be specified. 100 means normal speed. Integers of 0 or greater only.<br />
With an ms suffix: 0–10000 can be specified. Sets the absolute wait time per character in milliseconds.

Omitting the value or setting it to 1: restores the default value<br />
Setting it to 0: always displays text immediately

After the script finishes running, the setting is reset to the equivalent of 100%.

**対応:** SSP
