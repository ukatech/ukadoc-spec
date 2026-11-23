# collisionoptionブレス記述例

```
sakura.collisionoption
{
nodrag0,Knob
nodrag1,Bust
nocontextmenu0,Bust
}
```

相方側の設定はkero.collisionoption、char\*.collisionoption

当たり判定の名前に対して、ユーザーのマウス操作に対する本体の既定の動作を止める指定を付けるブレス。<br />
名前で引くので、collision・collisionex・animation\*.collisionのどれで付けた名前にも効く。指定の単位はサーフェスごとではなく名前ごと。サーフェスによって変えたいときは、別の名前を使うこと。

ユーザーの操作を阻害するので、濫用しないこと。<br />
指定した当たり判定には、cursorブレスのmouseup\*・mousedown\*・mouserightdown\*などで、操作できないことが利用者に伝わるカーソルを必ず指定すること。

**対応:** SSP 2.9.38
