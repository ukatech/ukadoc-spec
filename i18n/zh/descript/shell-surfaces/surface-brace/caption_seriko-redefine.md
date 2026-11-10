# 关于 SERIKO 的旧定义和新定义

## 什么是 SERIKO 的新定义和旧定义

在本家伺か（MATERIA）开发末期的版本中，surfaces.txt 中与 SERIKO（动画）相关的设置格式发生了变化。<br />
对于这一变化，[本家规格书](http://usada.sakura.vg/contents/seriko.html)中的 SERIKO/1.x 系传统格式称为旧定义，而将未被官方文档化的新格式（SERIKO/2.0）称为新定义。

此外，*完全不同于此*，MATERIA 停止开发后，SSP 等也为 sufraces.txt 格式独立追加了一些记法（例如 surface.append、surface1-9 这样的范围指定）。<br />
或许有人或文献会将这些也称为新定义，但请注意，至少 ukadoc 所说的新旧定义并非这种用法，而是专指 SERIKO 的格式。

## 新定义和旧定义的区别

新定义的格式有以下四处变化。

1. 将 [SERIKO 相关的定义行](animation-star-.interval.md)全部改为以「animation」一词开头。
2. [pattern 定义行](animation-star-.pattern-star.md)的参数顺序发生了变化（将绘制方法指定移至开头）。
3. pattern 定义中 wait 参数的单位从 10 毫秒改为 1 毫秒。
4. 绘制方法 [alternativestart](h-drowmethod/alternativestart.md) 中，指定 ID 的括号从 \[\] 改为 ()。

此外，还需要设置 descript brace，并定义「[version,1](../descript-brace/version.md)」。

以下是*定义内容相同*的旧定义和新定义示例。

```
// 旧定義
surface1
{
0interval,rarely
0pattern0,0,0,alternativestart,[1,2]

1interval,never
1pattern0,101,70,overlay,200,100
1pattern1,102,70,overlay,200,100
1pattern2,101,70,overlay,200,100
1pattern3,-1,70,overlay,0,0

2interval,never
2pattern0,101,70,overlay,200,100
2pattern1,102,70,overlay,200,100
2pattern2,101,70,overlay,200,100
2pattern3,-1,70,overlay,0,0
2pattern4,101,70,overlay,200,100
2pattern5,102,70,overlay,200,100
2pattern6,101,70,overlay,0,0
2pattern7,-1,70,overlay,0,0
}
```

```
// 新定義
surface1
{
animation0.interval,rarely
animation0.pattern0,alternativestart,(1,2)

animation1.interval,never
animation1.pattern0,overlay,101,700,200,100
animation1.pattern1,overlay,102,700,200,100
animation1.pattern2,overlay,101,700,200,100
animation1.pattern3,overlay,-1,700,0,0

animation2.interval,never
animation2.pattern0,overlay,101,700,200,100
animation2.pattern1,overlay,102,700,200,100
animation2.pattern2,overlay,101,700,200,100
animation2.pattern3,overlay,-1,700,0,0
animation2.pattern4,overlay,101,700,200,100
animation2.pattern5,overlay,102,700,200,100
animation2.pattern6,overlay,101,700,200,100
animation2.pattern7,overlay,-1,700,0,0
}
```

- 动画 ID
- pattern ID
- surface ID
- 绘制方法
- wait
- x 坐标
- y 坐标

请注意，定义现在以「animation」开头，wait 数值变为原来的 10 倍，并且绘制方法指定移到了参数开头。<br />
此外，alternativestart 的括号从 \[\] 改为 ()；对于 alternativestart 中会被忽略的参数「surface ID」「wait」，旧定义中写入了虚设数值 0，而新定义中由于绘制方法移到了开头，「合成位置 x,y」也可以一并省略。

## 使用新定义的优点

- 对于 SSP 独立追加的设置（本页面中的项目里，显示![Materia](../../../assets/image/icon_m.png)而不显示![SSP](../../../assets/image/icon_s.png)的项目），有时并未预期使用旧定义来编写。<br />
  今后追加的所有设置也可能如此。<br />
  使用这些设置时，最好采用新定义（使用旧定义可能无法正常工作）。<br />
  此时混用新旧定义会导致错误，因此需要统一使用新定义。
- wait 的单位从 10ms 改为 1ms，可以进行更精细的设置。
- 此外，如上例所示，绘制方法移至参数开头后，像 start 或 alternativestart 这类特殊绘制方法中会被忽略的参数也可以整洁地省略，这或许也是一项优点。
- 另外，明确写出「animation」一词后，与 SERIKO 相关的定义更为集中，或许也能让每一行的含义更容易理解。不过，易读性很大程度上取决于熟悉程度和个人差异；习惯旧定义并觉得旧定义更易读，也是很自然的感受。

如果不认为上述几点有优势，并且只考虑 SSP 的支持，那么未必有必要迁移。

另外，UKADOC 中的 SERIKO 内容基本都以新定义编写；如果想使用旧定义，请参考上文并酌情转换。
