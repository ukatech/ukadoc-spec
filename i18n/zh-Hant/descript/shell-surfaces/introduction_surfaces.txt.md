# surfaces.txt

## 概要

用來設定 shell 各項定義的檔案。原則上所有項目皆可省略，只需撰寫必要項目。<br />
例如，各個 surface（表情、零件、動畫格、dressup 零件）的動畫、命中區域、影像合成等設定都在此進行。<br />
此外，也可以在此為 surface ID 設定別名（alias）。<br />
SSP 也可在此設定滑鼠游標持續停留在命中區域上時顯示的工具提示，以及變更游標顯示等。

另一方面，shell 名稱、shell 作者名稱等 shell 基本資訊，以及 dressup 的 owner draw 選單（按右鍵選單）顯示設定，並非在此設定，而是在 [descript.txt](../shell/index.md) 中設定，請注意。

## 基本格式

原則上，大部分設定都*可以省略*，只需視需要設定。

若要撰寫設定，除了必須寫在第一行的 [charset](file/charset.md) 之外，其他設定都記述於各自以「\{」和「\}」括住的 brace 內（各 brace 請參閱本頁的對應項目）。

「\{」和「\}」必須各自單獨占一行，不能像「surface1 \{」這樣接在 brace 名稱後面書寫。

```
ブレス名
{
// 設定内容
}
```

未被辨識為 brace 名稱、\{\} 或各項設定的行，都會視為註解行。慣例上會以「//」作為行首。

各行可使用縮排。

僅 SSP 會讀取所有名稱符合「surfaces\*\*\*.txt（\*\*\*為任意字串）」的文字檔，並將其視同 surfaces.txt。若有多個符合讀取條件的檔案，會依檔名順序讀取。

另外，若準備多個 surfaces\*\*\*.txt，[descript brace](descript-brace/introduction_descriptbrace.md) 的設定（以及 [charset](file/charset.md)）必須在每個檔案中分別設定（換句話說，各檔案可以使用不同的設定）。

## 記述例

```
charset,Shift_JIS

descript
{
version,1
}

surface0
{
animation0.interval,sometimes
animation0.pattern0,overlay,101,100,168,67
animation0.pattern1,overlay,100,100,168,67
animation0.pattern2,overlay,101,100,168,67
animation0.pattern3,overlay,-1,100,168,67
}

surface1
{
element0,overlay,body0.png,0,0
element1,overlay,face1.png,0,0
}

surface10
{
collision0,40,56,95,90,Head

sakura.balloon.offsetx,80
sakura.balloon.offsety,-100
kero.balloon.offsetx,-30
kero.balloon.offsety,20
}

// SSPのみで有効な記法 ←このようにコメント行は//から始める
surface.append0-9
{
collision0,188,25,252,63,Head
collision1,190,92,236,118,Face
collision2,180,191,220,222,Bust
collision3,154,311,248,362,Skirt
}
```
