# 通过DirectSSTP调用SAORI

参考：[SAORI/1.0](http://www.boreas.dti.ne.jp/~sdn/saori.html)（外部网站）

这是一项扩展规范，用于通过[Direct SSTP](../sstp/direct.md)将SAORI/1.0请求发送给baseware，而不是通过DLL的request函数，并将baseware内置的功能（内置模块）作为SAORI调用。\[SSP 2.9.13\]<br />
从SHIORI的角度看，它就是“无需放置DLL即可使用的SAORI”。baseware提供哈希、加密、随机数、日期时间计算等过去需要各个ghost随附DLL才能使用的功能。<br />
本页面的前半部分（SAORI/1.0概要～发送方的步骤）是不依赖baseware的规范，后半部分（内置模块）则介绍SSP内置的模块。
