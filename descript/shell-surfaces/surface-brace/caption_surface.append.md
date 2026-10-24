# surface\*ブレスとsurface.append\*ブレス

surface.appendによる定義は、「既に（surfaceブレス、またはsuface\*.pngの存在によって）ある定義」に対してのみ付け加えられる。

従って例えば、

```
surface1,3
{
collision0,188,25,252,63,Head
collision1,180,191,220,222,Bust
}
```

の後に、追加定義のつもりで

```
surface1-3
{
animation0.interval,sometimes
animation0.pattern0,overlay,101,100,168,67
animation0.pattern1,overlay,100,100,168,67
animation0.pattern2,overlay,101,100,168,67
animation0.pattern3,overlay,-1,100,168,67
}
```

などとすると、本来定義するつもりのない「surface2」が*新設されて*、定義が行われてしまう。

このため、appendを使わない範囲指定の追加定義は「覚えのない重複定義エラー」などの原因になり得る。しかし、

```
surface.append1-3
{
// 略
}
```

とした場合は、既に定義のある「surface1」および「surface3」のみにappendで追加した定義が加わり、予め存在しない「surface2」は内部的にも*新設されない*。

なお、この関係から、*surfaceブレスは*定義ファイル（surfaces.txtなど）内で*surface.appendブレスより先に書く*必要がある事に注意。
