# animation\*.option, shared-index

**カテゴリ:** surface brace

Continues an animation with the same ID from where it left off, even when the base surface is changed using the `\s` tag.<br />
Specifically, if the animation has run up to pattern4 before `\s` is executed, it restarts from pattern4 after `\s` is executed as well.<br />
This option must be specified on both the source and destination of the `\s` switch; specifying it on only one side resets the animation.<br />
The animation also resets if the destination animation does not have the pattern ID.

**既定値:** No behavior

**対応:** SSP 2.6.02
