# インストールの識別子

- shell
- ghost
- balloon
- plugin
- headline
- rss
- supplement

以下はOnInstallComplete / OnNarCreatedのみ<br />
SSPでは廃止されており、ゴーストとバルーンがそれぞれ別の識別子として通知される。

- ghost with balloon
- shell with balloon

以下はSSP専用

- calendar skin
- calendar plugin
- package
- language

SSPで[同時インストール](../../../descript/install/install-txt/introduction_install_multi.md)された物の識別子は、install.txtでの指定と同じく*ドット区切り*の calendar.skin / calendar.plugin になる。<br />
アーカイブ本体側の識別子はinstall.txtのtypeの表記のままなので、空白区切りの calendar skin / calendar plugin になる。
