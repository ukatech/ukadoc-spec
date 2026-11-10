# animation\*.option,exclusive

**カテゴリ:** surface brace

Exclusive execution option for animations.<br />
That is, when an animation with the exclusive option runs, all other animations stop, and no other animation can start until the exclusive animation ends.<br />
The \* following animation is the animationID (the same as the \* in animation\*.interval).<br />
Note that this option is undefined for animations whose interval is bind.<br />
SSP alone allows exclusive control to be limited to animations with specified IDs by using a definition such as animation\*.option,exclusive,(1,3,5).<br />
[Legacy definition](caption_seriko-redefine.md): \*option,exclusive

**既定値:** No behavior

**対応:** Materia / SSP / CROW
