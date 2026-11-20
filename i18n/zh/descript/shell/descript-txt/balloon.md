# balloon,balloon名称

**カテゴリ:** descript.txt

此shell的默认balloon名称。用户未显式切换balloon时，切换到此shell会自动切换到此balloon。<br />
如果用户显式切换过balloon，则优先使用用户选择的balloon。如果ghost侧指定了[recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md)（推荐balloon），也会优先使用该值。<br />
也可写在ghost侧descript.txt的[balloon](../../ghost/recommended-balloon/balloon.md)（默认balloon）中。如果shell侧有指定，则优先使用shell侧的值；否则使用ghost侧的值。<br />
仅因遵循默认值而切换不视为用户显式切换。因此，切换到其他shell时，会按照该shell的定义再次切换。<br />
指定多个值时，使用最先找到的balloon（[default.balloon.path](default.balloon.path.md)的指定值优先）。

**既定値:** ghost的descript设置

**対応:** SSP
