# collisionoption块示例

```
sakura.collisionoption
{
nodrag0,Knob
nodrag1,Bust
nocontextmenu0,Bust
}
```

搭档侧的设置为kero.collisionoption、char\*.collisionoption

此块按碰撞区域名称指定是否阻止本体对用户鼠标操作的默认行为。<br />
由于按名称匹配，因此对使用collision、collisionex、animation\*.collision设置的名称均有效。指定的单位是名称而非surface。需要因surface而异时，应使用不同的名称。

由于会妨碍用户操作，请勿滥用。<br />
对于指定的碰撞区域，必须使用cursor块的mouseup\*、mousedown\*、mouserightdown\*等指定能向用户表明无法操作的光标。

**対応:** SSP 2.9.38
