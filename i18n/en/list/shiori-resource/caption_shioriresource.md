# SHIORI Resource

SHIORI Resource originated as a *request for retrieving simple string information*, such as displaying owner-draw menus and homeurl, defined by the legacy protocol [SHIORI/2.5](http://usada.sakura.vg/contents/shiori.html#shiori25).<br />
This specification allows such information to be controlled according to the ghost's state.

In SHIORI/3.0 and later, as a result of organizing the legacy specification, it is not clearly distinguished from ordinary SHIORI Events in terms of implementation.

Unlike ordinary SHIORI Events, its return value is treated as plain (short) text rather than Sakura Script (including bool-like values). Also, request IDs do not begin with "On", and alphabetic characters are written in lowercase.
