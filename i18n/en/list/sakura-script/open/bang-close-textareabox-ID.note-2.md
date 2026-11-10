# InputBox IDs

When input is confirmed, [OnUserInput](../../shiori-event/inputbox/OnUserInput.md) is triggered. However, if the ID is a string that starts with "On", an event named after the ID is triggered instead.<br />
For OnUserInput, the specified ID is placed in Reference0 and the input is placed in Reference1. For an event named after the ID, the input is placed in Reference0 instead.<br />

Example<br />
When input is confirmed using `\![open,inputbox,インプットテスト,10000,テスト入力]`.

- "OnUserInput" is triggered
- Reference0 contains "インプットテスト"
- Reference1 contains the input
- Reference2 contains supplementary input information (sliderinput only: minimum and maximum; otherwise empty)
- Reference3 and later contain additional information specified by --reference=

When input is confirmed using `\!`\[open,inputbox,*On*インプットテスト,10000,テスト入力\].

- "Onインプットテスト" is triggered
- Reference0 contains the input
- Reference1 contains supplementary input information (sliderinput only: minimum and maximum; otherwise empty)
- Reference2 and later contain additional information specified by --reference=

Regardless of the ID, [OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md) is triggered when the close button is pressed or the input times out.
