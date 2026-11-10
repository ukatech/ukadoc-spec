# animation\*.option,shared-index

**カテゴリ:** surface brace

Continues an animation with the same ID from where it left off, even when the base surface is switched with the `\s` tag.<br />
Specifically, if the animation has played up to pattern4 before `\s` is executed, it restarts from pattern4 after `\s` is executed as well.<br />
This option must be specified on both the source and destination of the `\s` switch; if specified on only one side, the animation is reset.<br />
The animation is also reset if the pattern ID cannot be found in the destination animation.

**既定値:** No behavior

**対応:** SSP 2.6.02
