# collisionex\*,ID,類型,座標1,座標2...

**カテゴリ:** surface brace

不規則形狀的命中判定。<br />
\*的部分（collisionID）是同一個surface內不可重複的流水號。<br />
類型如下。

- **rect**: 長方形。座標為起點XY與終點XY，共4個值。<br />
  例：collisionex0,Head,rect,100,100,200,300
- **ellipse**: 橢圓形。座標為包住橢圓的長方形，其起點XY與終點XY，共4個值。<br />
  例：collisionex0,Head,ellipse,100,100,200,300
- **circle**: 正圓形。依序指定中心點的XY值與半徑。<br />
  例：collisionex0,Head,circle,100,200,20
- **polygon**: 多邊形。座標為各頂點，可交叉。<br />
  例：collisionex0,Head,polygon,100,100,200,300,50,200
- **region**: \[SSP 2.5.19～\]將指定圖檔中指定顏色的區域視為命中判定。<br />
  大量（100個以上）使用時，整體執行速度會變慢，請留意。<br />
  將「反轉區域」設為true時，表示「非指定顏色的區域」。可省略。<br />
  指定格式：檔名,R,G,B,反轉區域(false或true)<br />
  例1: collisionex0,Head,region,atari.png,255,0,0<br />
  例2: collisionex1,Head,region,atari.png,0,255,0,true

**既定値:** 無作用

**対応:** SSP
