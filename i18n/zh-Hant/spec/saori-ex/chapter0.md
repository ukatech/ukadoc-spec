# 透過 DirectSSTP 使用 SAORI

參考：[SAORI/1.0](http://www.boreas.dti.ne.jp/~sdn/saori.html)（外部網站）

這是SAORI/1.0的擴充規格，透過[Direct SSTP](../sstp/direct.md)將要求傳送給baseware，而非使用DLL的request函式，藉此以SAORI方式呼叫baseware內建的功能（內建模組）。\[SSP 2.9.13\]<br />
從SHIORI的角度來看，這是「不放置DLL也能使用的SAORI」。baseware提供雜湊、加密、亂數、日期與時間計算等功能，這些功能過去需要在每個ghost中附帶DLL。<br />
本頁前半部（SAORI/1.0概要～傳送端的步驟）是與baseware無關的規格，後半部（內建模組）則說明SSP內建的模組。
