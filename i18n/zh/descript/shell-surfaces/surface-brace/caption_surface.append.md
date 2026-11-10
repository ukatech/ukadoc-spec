# surface\*大括号与surface.append\*大括号

surface.append定义仅会附加到“已经存在的定义”（通过surface大括号或suface\*.png的存在而建立）上。

因此，例如，在

```
surface1,3
{
collision0,188,25,252,63,Head
collision1,180,191,220,222,Bust
}
```

之后，若将以下内容作为追加定义：

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

那么，本来并不打算定义的“surface2”也会*被新建*，并进行定义。

因此，不使用append的范围指定追加定义可能会导致“莫名其妙的重复定义错误”等问题。不过，如果写成

```
surface.append1-3
{
// 略
}
```

则追加定义只会通过append添加到已有定义的“surface1”和“surface3”上，不存在的“surface2”在内部也*不会被新建*。

另外，基于这一关系，请注意，*surface大括号*必须在定义文件（如surfaces.txt）中*先于surface.append大括号书写*。
