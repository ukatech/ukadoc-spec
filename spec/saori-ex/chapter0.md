# SAORI over DirectSSTP

参考：[SAORI/1.0](http://www.boreas.dti.ne.jp/~sdn/saori.html)（外部サイト）

SAORI/1.0の要求を、DLLのrequest関数ではなく[Direct SSTP](../sstp/direct.md)でベースウェアに送り、ベースウェアに内蔵された機能（内蔵モジュール）をSAORIとして呼び出すための拡張規格です。\[SSP 2.9.13\]<br />
SHIORIから見ると「DLLを置かずに使えるSAORI」になります。ハッシュ・暗号・乱数・日時の計算など、これまでゴーストごとにDLLを同梱していた機能をベースウェアが提供します。<br />
このページの前半（SAORI/1.0の概要～送信側の手順）はベースウェアに依存しない規格、後半（内蔵モジュール）はSSPが内蔵しているモジュールの説明です。
