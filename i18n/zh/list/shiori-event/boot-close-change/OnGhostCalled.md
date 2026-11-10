# OnGhostCalled

**カテゴリ:** Startup, shutdown, and switching events

Occurs when called by another ghost.<br />
In SSP, if no script is returned for this event (204), [OnBoot](OnBoot.md) occurs next.

- **Reference0**: Name of the calling ghost on the baseware side.
- **Reference1**: Script used when the calling ghost called this ghost.
- **Reference2**: Name of the calling ghost.
- **Reference3**: Path of the calling ghost.
- **Reference7**: Shell name of the *called ghost*.

**対応:** SSP
