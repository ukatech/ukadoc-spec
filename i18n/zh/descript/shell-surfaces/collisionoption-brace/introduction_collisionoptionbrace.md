# collisionoption 块记述例

```
sakura.collisionoption
{
nodrag0,Knob
nodrag1,Bust
nocontextmenu0,Bust
}
```

搭档侧的设置为 kero.collisionoption、char\*.collisionoption

此块针对碰撞判定名称指定是否禁止主程序对用户鼠标操作的默认行为。<br />
由于按名称查找，因此无论名称由 collision、collisionex 还是 animation\*.collision 设置，都会应用。设置按名称而非 surface 区分。如需针对不同 surface 设置不同的行为，请使用不同的名称。

此功能会妨碍用户操作，请勿滥用。<br />
必须在 cursor 块中通过 mouseup\*、mousedown\*、mouserightdown\* 等为指定的碰撞判定设置光标，使用户了解无法进行该操作。

**対応:** SSP 2.9.38
