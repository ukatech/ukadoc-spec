# SERIKO 的舊定義與新定義

## 什麼是 SERIKO 的新定義與舊定義

在官方伺か（MATERIA）開發末期的版本中，surfaces.txt 中與 SERIKO（動畫）相關的設定格式有所變更。<br />
在[官方規格書](http://usada.sakura.vg/contents/seriko.html)中記載的 SERIKO/1.x 系列傳統格式稱為舊定義，而未經官方文件記載的新格式（SERIKO/2.0）則有時稱為新定義。

另外，*與此完全不同的是*，MATERIA 結束開發後，SSP 等也各自新增了 surfaces.txt 格式的記法（例如 surface.append、surface1-9 這類範圍指定）。<br />
有些人或文獻可能會將這些也稱為新定義，但請注意，至少 ukadoc 所說的新舊定義並非這種用法，而是指 SERIKO 的格式。

## 新定義與舊定義的差異

新定義的格式有以下四項變更。

1. 將所有 [SERIKO 相關的定義行](animation-star-.interval.md)改為以「animation」一詞開頭。
2. [pattern 定義行](animation-star-.pattern-star.md)的參數順序有所變更（將繪製方法移至最前面）。
3. pattern 定義的權重參數單位，從 10 毫秒改為 1 毫秒。
4. 繪製方法的 [alternativestart](h-drowmethod/alternativestart.md) 中，ID 指定的括號從 \[\] 改為 ()。

除此之外，還需要設定 descript 區塊並定義「[version,1](../descript-brace/version.md)」。

以下是*定義內容相同*的舊定義與新定義範例。

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

- 動畫 ID
- pattern ID
- サーフェス ID
- 繪製方法
- 權重
- x 座標
- y 座標

請注意，除了改為以「animation」開頭之外，權重數值也變成原來的 10 倍，繪製方法的指定也移到了參數最前面。<br />
此外，alternativestart 的括號從 \[\] 改為 ()；對於在 alternativestart 中會被忽略的參數「サーフェス ID」和「權重」，舊定義會填入虛設數值 0，而新定義則因為繪製方法移到了最前面，可以連同「合成位置 x,y」一起省略。

## 使用新定義的優點

- 對於 SSP 自行新增的設定（本頁項目中![Materia](../../../assets/image/icon_m.png)沒有顯示，而只有![SSP](../../../assets/image/icon_s.png)顯示的項目），有些可能不預期以舊定義撰寫。<br />
  之後新增的所有設定也可能有同樣的情況。<br />
  使用這類設定時，建議採用新定義（以舊定義撰寫可能無法正常運作）。<br />
  此時若混用新舊定義會發生錯誤，因此必須統一使用新定義。
- 權重單位從 10ms 改為 1ms，可以進行更細緻的設定。
- 如上例所示，繪製方法移到參數最前面後，start 或 alternativestart 這類特殊繪製方法會忽略的參數也能簡潔地省略，這或許也是一項優點。
- 此外，明確標示「animation」一詞，也可能讓 SERIKO 相關定義的範圍更清楚，使各行的意義更容易理解。不過，可讀性大多取決於熟悉程度與個人差異；習慣舊定義並覺得它較易閱讀，也是很自然的感受。

如果不覺得以上各點有其優點，且只考慮支援 SSP，則不一定有遷移的必要。

另外，UKADOC 基本上使用新定義記述 SERIKO，因此若要使用舊定義撰寫，請參考以上內容並適當換算。
