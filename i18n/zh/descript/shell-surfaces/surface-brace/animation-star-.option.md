# animation\*.option,exclusive

**カテゴリ:** surface brace

Exclusive execution option for animations.<br />
That is, as soon as an animation with the exclusive option starts, all other animations stop, and no other animation can start until the exclusive animation ends.<br />
The \* following animation is the animationID (the same as the \* in animation\*.interval).<br />
This option is undefined for animations whose interval is a bind.<br />
SSP alone supports limiting exclusive control to only animations with specified IDs, as in animation\*.option,exclusive,(1,3,5).<br />
[Legacy definition](caption_seriko-redefine.md): \*option,exclusive

**既定値:** No effect

**対応:** Materia / SSP / CROW
