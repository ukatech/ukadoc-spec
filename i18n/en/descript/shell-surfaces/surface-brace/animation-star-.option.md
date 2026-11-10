# animation\*.option, exclusive

**カテゴリ:** surface brace

The option to run an animation exclusively.<br />
That is, when an animation with the exclusive option starts, all other animations stop, and no other animations can start until the exclusive animation ends.<br />
The \* following animation is the animationID (the same as the \* in animation\*.interval).<br />
Note that this option is undefined for animations whose interval is bind.<br />
SSP-only: writing animation\*.option,exclusive,(1,3,5) limits exclusive control to animations with the specified IDs.<br />
[Old definition](caption_seriko-redefine.md): \*option,exclusive

**既定値:** No behavior

**対応:** Materia / SSP / CROW
