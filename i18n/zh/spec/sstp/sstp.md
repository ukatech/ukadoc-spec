# 概要

SSTP是ghost之间的通用通信规范。可用于播放简单的Sakura Script，或从外部通知事件等。<br />
通信基本上通过TCP/IP进行。程序监听端口9801或9821（仅SSP），按SSTP协议发送请求后会返回处理结果。<br />
出于安全考虑，当前除非更改设置，否则只监听localhost，无法从设备外部进行通信。此外，过去也监听过11000端口，但因通信被误认为是恶意软件通信，目前已废止。<br />
关于启动时临时指定监听地址的[--sstp-listen](https://ukatech.shillest.net/ukadoc-ssp/functions/option/#一般オプション)等SSP启动选项，请参阅[SSP帮助中的启动选项](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)。<br />
[IANA的Port number registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=sakura+script)中登记了7743和9801端口，但实际运行中仅使用9801端口。<br />
Microsoft制定了一个简称相同、用于VPN通信的Secure Socket Tunneling Protocol，但它与本协议在技术上没有关联。<br />
默认情况下，每次通信结束时都会断开连接。频繁通信时，可以像HTTP一样通过[keep-alive](keepalive.md)复用连接 \[SSP 2.9.03\]。
