# currentghost.balloon.scope(ID).vertical

**カテゴリ:** プロパティシステム

目前 balloon 是否為[縱書](../../../descript/balloon/descript-txt/vertical.md)。縱書時為 1，橫書時為 0。<br />
[validwidth](currentghost.balloon.scope-ID-.validwidth.md)・[validheight](currentghost.balloon.scope-ID-.validheight.md) 即使在縱書時，仍表示名稱所指的「畫面上的方向」數值；縱書時，validwidth 是「欄位前進方向的可用寬度」，validheight 則是「一欄的長度」。[lines](currentghost.balloon.scope-ID-.lines.md)無論縱書或橫書，皆表示「可容納的行數」（縱書時為欄數）。<br />
若要計算一行（一欄）可容納多少字元，縱書時請參照 validheight，橫書時請參照 validwidth。此屬性可用來判斷應參照哪個值。<br />
※SSP 2.8.83 變更規格。2.8.80 中，縱書時的 validwidth・validheight 表示以「文字排列方向為基準的方向」為準的數值。

**対応:** SSP 2.8.80
