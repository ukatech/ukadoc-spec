# collisionex\*,ID,类型,坐标1,坐标2...

**カテゴリ:** surface大括号

不规则形状的碰撞判定。<br />
\*部分（collisionID）是在同一surface内不重复的连续编号。<br />
类型如下。

- **rect**: 矩形。坐标为起点XY和终点XY，共4个值。<br />
  示例：collisionex0,Head,rect,100,100,200,300
- **ellipse**: 椭圆。坐标为包围椭圆的矩形的起点XY和终点XY，共4个值。<br />
  示例：collisionex0,Head,ellipse,100,100,200,300
- **circle**: 正圆。依次填写中心点的XY值和半径。<br />
  示例：collisionex0,Head,circle,100,200,20
- **polygon**: 多边形。坐标为各顶点，可相交。<br />
  示例：collisionex0,Head,polygon,100,100,200,300,50,200
- **region**: \[SSP 2.5.19～\]将指定图像文件中指定颜色的区域作为碰撞判定区域。<br />
  使用数量过多（100个以上）会导致整体运行变慢，请注意。<br />
  将「反转区域」设为true后，表示「非指定颜色的区域」。可省略。<br />
  指定格式：文件名,R,G,B,反转区域(false或true)<br />
  示例1: collisionex0,Head,region,atari.png,255,0,0<br />
  示例2: collisionex1,Head,region,atari.png,0,255,0,true

**既定値:** 无效果

**対応:** SSP
