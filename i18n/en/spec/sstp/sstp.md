# Overview

SSTP is a general-purpose communication specification between ghosts. It can be used for simple Sakura Script playback, external event notifications, and similar purposes.<br />
Communication is generally done over TCP/IP. The system listens on port 9801 or 9821 (SSP only). Sending a request according to the SSTP protocol returns the processing result.<br />
For security reasons, unless the settings are changed, it currently listens only on localhost, so communication from outside the device is not possible. Port 11000 was also listened on in the past, but it has since been deprecated because the communication was mistaken for malware activity.<br />
For SSP startup options, including [--sstp-listen](https://ukatech.shillest.net/ukadoc-ssp/functions/option/#一般オプション), which temporarily specifies the listening address at startup, see [Startup options in the SSP Help](https://ukatech.shillest.net/ukadoc-ssp/functions/option/).<br />
7743 and 9801 are registered in the [IANA Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=sakura+script), but only port 9801 is actually in use.<br />
Microsoft defined a VPN protocol with the same abbreviation, Secure Socket Tunneling Protocol, but it has no technical relation to SSTP.<br />
By default, the connection is closed at the end of each communication. For frequent communication, the connection can be reused with [keep-alive](keepalive.md), as with HTTP \[SSP 2.9.03\].
