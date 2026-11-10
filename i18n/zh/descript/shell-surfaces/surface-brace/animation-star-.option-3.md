# animation\*.option,shared-index

**カテゴリ:** surface brace

When switching the base surface with the `\s` tag, continue running an animation with the same ID from where it left off.<br />
Specifically, if the animation has reached pattern4 before `\s` is run, it resumes from pattern4 after `\s` is run.<br />
This option must be specified on both the source and destination of the `\s` switch; specifying it on only one side resets the animation.<br />
The animation also resets if the destination animation does not have the pattern ID.

**既定値:** No effect

**対応:** SSP 2.6.02
