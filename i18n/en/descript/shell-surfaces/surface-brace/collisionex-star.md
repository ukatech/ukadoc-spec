# collisionex\*,ID,Type,Coordinate1,Coordinate2...

**カテゴリ:** surface directive

Irregularly shaped hit-test area.<br />
The \* portion (collisionID) is a sequential number that must be unique within the same surface.<br />
The types are as follows.

- **rect**: Rectangle. The four coordinates are the start XY and end XY.<br />
  Example: collisionex0,Head,rect,100,100,200,300
- **ellipse**: Ellipse. The four coordinates specify the bounding rectangle, as start XY and end XY.<br />
  Example: collisionex0,Head,ellipse,100,100,200,300
- **circle**: Circle. Specify the center XY values, followed by the radius.<br />
  Example: collisionex0,Head,circle,100,200,20
- **polygon**: Polygon. Coordinates specify each vertex; intersections are allowed.<br />
  Example: collisionex0,Head,polygon,100,100,200,300,50,200
- **region**: \[SSP 2.5.19～\]Treats the area of a specified color in the specified image file as a hit-test area.<br />
  Note that using a large number (100 or more) can slow down operation overall.<br />
  Setting "invert region" to true means "areas that are not the specified color." This setting is optional.<br />
  Format: filename,R,G,B,invert region(false or true)<br />
  Example 1: collisionex0,Head,region,atari.png,255,0,0<br />
  Example 2: collisionex1,Head,region,atari.png,0,255,0,true

**既定値:** No effect

**対応:** SSP
