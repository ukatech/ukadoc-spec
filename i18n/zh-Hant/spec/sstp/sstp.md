# 概要

SSTP是ghost之間的通用通訊規格。可用於播放簡單的SakuraScript，或從外部通知事件等。<br />
通訊基本上透過TCP/IP進行。程式會監聽連接埠9801或9821（僅SSP），依照SSTP協定傳送request後，便會傳回處理結果。<br />
基於安全考量，目前除非變更設定，否則只會監聽localhost，無法從終端裝置外部進行通訊。此外，過去也曾監聽連接埠11000，但因曾被誤認為是惡意軟體的通訊，目前已廢止。<br />
如需了解啟動時暫時指定監聽位置的[--sstp-listen](https://ukatech.shillest.net/ukadoc-ssp/functions/option/#一般オプション)等SSP啟動選項，請參閱[SSP說明的啟動選項](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)。<br />
[IANA的Port number registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=sakura+script)中登錄了7743與9801，但實際運作的只有9801。<br />
Microsoft也制定了名稱縮寫相同、用於VPN通訊的Secure Socket Tunneling Protocol，但在技術上並無關聯。<br />
預設每次通訊結束時都會中斷連線。頻繁通訊時，可像HTTP一樣透過[keep-alive](keepalive.md)重複使用連線 \[SSP 2.9.03\]。
