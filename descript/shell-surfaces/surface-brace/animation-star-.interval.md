# animation\*.interval,インターバル

**カテゴリ:** surfaceブレス

アニメーションが開始するタイミング（周期）の定義。<br />
インターバルは下記の[アニメーションインターバル](h-animationinterval/index.md)参照。SSPのみ+区切りで列挙する事で組み合わせ指定が可能。<br />
\*の部分（animationID）は任意の数字。そのスコープ内（`\0`、`\1`、...）の全surfaceで、共通して同じIDのアニメーションが同じ意味（例えば「瞬き」「口パク」「同じ服の着せ替え」など）を持つようにする。<br />
interval定義はそのIDのアニメーション定義全体の始点を示し、一連のanimation定義の中で必ず最初に記述されなければならない。<br />
アニメーションの重なり方とIDの順序の関係は[animation-sort](../descript-brace/animation-sort.md)参照。<br />
[旧定義](caption_seriko-redefine.md)：\*interval,インターバル

**既定値:** 挙動なし

**対応:** Materia / SSP / CROW
