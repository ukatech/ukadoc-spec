# surface\*大括號與surface.append\*大括號

透過surface.append定義的內容，只會附加到「已存在的定義」（透過surface大括號或suface\*.png的存在而建立）上。

因此，例如在

```
surface1,3
{
collision0,188,25,252,63,Head
collision1,180,191,220,222,Bust
}
```

之後，若打算新增定義而寫成

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

就會*新建*原本不打算定義的「surface2」，並為它建立定義。

因此，不使用append的範圍指定新增定義，可能會造成「意料之外的重複定義錯誤」等問題。不過，

```
surface.append1-3
{
// 略
}
```

這樣寫時，透過append新增的定義只會加到已定義的「surface1」和「surface3」上，不會在內部*新建*原本不存在的「surface2」。

此外，根據上述關係，請注意，*surface大括號*必須在定義檔（surfaces.txt等）中*寫在surface.append大括號之前*。
