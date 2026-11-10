# Dressup 設定

## Dressup

伺か (Ukagaka) 的 shell 可以設定*dressup*（dressup 本身的說明請參閱「Shell設定 - surfaces.txt」中的「[Dressup（MAYUNA）](../descript/shell-surfaces/surface-brace/introduction_mayuna.md)」）。

使用 dressup 後，從 owner draw 選單選取時，可以在單一 shell 內切換角色外觀的部分元素，或將其開啟、關閉。

SSP 也可以透過[Sakura Script 指令](../list/sakura-script/surface/bang-bind.md)切換 dressup。

只有 MATERIA、SSP 支援 dressup；CROW 只會顯示 dressup 初始配置。

但是，MATERIA 有錯誤，因此只會顯示`\0`端的 dressup 選單。

因此，實際上只有 SSP 完整支援`\1`以後的部分。

另外，本頁的說明假設讀者對動畫設定本身有一定程度的了解。

關於動畫設定，請參閱「建立 shell」頁面的「[撰寫 surfaces.txt - 動畫篇](shell.md#surfacestxtを書く---アニメーション編)」一節。

## 目次

1. [在surfaces.txt中設定](bind.md#surfacestxtでの設定)
2. [在descript.txt中設定](bind.md#descripttxtでの設定)

1. （準備中）SSP dressup 選單設定小技巧
2. （準備中）具有動態效果的 dressup
3. （準備中）某個 dressup 具有跨越其他 dressup 前後的三維結構時

## 在surfaces.txt中設定

```
surface0
{
animation0.interval,bind
animation0.pattern0,add,100,0,0,0
animation0.pattern1,add,101,0,20,35
animation0.pattern2,reduce,102,0,0,0
animation0.pattern3,add,103,0,0,0
}
```

如上所示，將 interval 設為 bind 的動畫就是 dressup。

繪圖方法如 add、reduce 等將於後文說明。

等待時間指定為 0，但若是 interval 為 bind 的動畫（也就是 dressup）設定，指定任何等待時間都會被忽略。

X 座標、Y 座標的偏移位置可以和一般動畫圖樣一樣指定。

此外，animation0 中的「0」是動畫 ID；在 dressup 的情況下，這個 ID 特別重要。

### Dressup 的繪圖方法

在官方伺か中，dressup 基本上使用 bind、add、reduce、insert 這 4 種方法。

SSP 也可以使用 base、overlay、overlayfast、replace、interpolate、asis 等方法，這些方法與一般動畫共用。

但是，start、stop、move 等不會單純合成圖片的方法無法使用。

## 在descript.txt中設定

簡單來說，在 descript.txt 中要做的是準備好讓 dressup 顯示於 owner draw 選單的 dressup 選單中。

請如下所示記述。

```
sakura.bindgroup0.name,服,エプロンドレス,apron.png
sakura.bindgroup1.name,リボン,白リボン,ribbonwhite.png
sakura.bindgroup2.name,服,黒服,black.png
sakura.bindgroup3.name,リボン,黒リボン,ribbonblack.png

sakura.bindgroup0.default,1
sakura.bindgroup1.default,1

kero.bindgroup0.name,ネクタイ,ネクタイ
kero.bindgroup1.name,腕章,黒腕章
kero.bindgroup2.name,腕,ドリル

kero.bindgroup0.default,1
kero.bindgroup1.default,1

sakura.menuitem0,2
sakura.menuitem1,3
sakura.menuitem2,-
sakura.menuitem3,0
sakura.menuitem4,1

kero.menuitem0,0
kero.menuitem1,1
kero.menuitem2,-
kero.menuitem3,2
```

如上所示記述後，主角色的 dressup 選單會出現「圍裙洋裝」「黑衣服」「白緞帶」「黑緞帶」

搭檔的選單則會出現「領帶」「臂章」「手臂」，並且可以自由穿脫這些 dressup。

?.bindgroup\* 依序以逗號分隔記述類別名稱、部件名稱、縮圖檔名。

此時，「bindgroup\*」中 \* 的數字會對應到 surfaces.txt 中設定的 dressup 動畫 ID。

請注意，所有 surface 中相同服裝（dressup）必須使用相同的動畫 ID。

?.bindgroup\*.default 用來設定動畫 ID 為「\*」的 dressup，作為該 shell 的 dressup 初始值。

依照上述範例的設定，預設會穿著圍裙洋裝和白緞帶、領帶和黑臂章。

指定 0 或省略時，dressup 會處於關閉狀態。

?.menuitem\*,\* 表示選單項目的結構。

依照選單顯示順序編號，並以逗號分隔，指定對應 bindgroup\* 中 \* 的編號（請注意，此處指定的不是動畫 ID）。

若以「-」取代 bindgroupID，則該位置會在選單中顯示分隔線。

以上述範例來說，主角色的 dressup 選單會由上而下顯示黑衣服、黑緞帶、（分隔線）、圍裙洋裝、白緞帶。

縮圖會在選單項目被選取時顯示，作為提示。

若不需要可以省略；但 dressup 數量較多，或難以從名稱推測 dressup 內容時，指定縮圖會很方便。

## SSP dressup 選單設定小技巧

準備中

## 具有動態效果的 dressup

準備中

## 某個 dressup 具有跨越其他 dressup 前後的三維結構時

準備中
