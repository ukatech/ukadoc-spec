# SAORI over DirectSSTP

Reference: [SAORI/1.0](http://www.boreas.dti.ne.jp/~sdn/saori.html) (external site)

This is an extension specification for sending SAORI/1.0 requests to the baseware using [Direct SSTP](../sstp/direct.md), rather than the DLL request function, and calling functionality built into the baseware (built-in modules) as SAORI. \[SSP 2.9.13\]<br />
From SHIORI's perspective, this is “SAORI that can be used without placing a DLL.” The baseware provides functions such as hashing, encryption, random number generation, and date and time calculations, which ghosts previously bundled with DLLs individually.<br />
The first half of this page (from the overview of SAORI/1.0 through the sender-side procedure) describes a specification independent of the baseware; the second half (built-in modules) describes modules built into SSP.
