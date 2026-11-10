# currentghost.balloon.scope(ID).vertical

**カテゴリ:** プロパティシステム

当前 balloon 是否为[纵排](../../../descript/balloon/descript-txt/vertical.md)。纵排时为 1，横排时为 0。<br />
[validwidth](currentghost.balloon.scope-ID-.validwidth.md)・[validheight](currentghost.balloon.scope-ID-.validheight.md)即使在纵排时也表示名称所指的「画面上的方向」的值；纵排时，validwidth 表示「可用于列推进方向的宽度」，validheight 表示「单列长度」。[lines](currentghost.balloon.scope-ID-.lines.md)在横排和纵排时均表示「可容纳的行数」（纵排时为列数）。<br />
若要计算一行（列）可容纳多少字符，纵排时应查看 validheight，横排时应查看 validwidth。此属性用于判断排版方向。<br />
※SSP 2.8.83 中更改了规格。在 2.8.80 中，纵排时的 validwidth・validheight 表示「以字符推进方向为基准的方向」的值。

**対応:** SSP 2.8.80
