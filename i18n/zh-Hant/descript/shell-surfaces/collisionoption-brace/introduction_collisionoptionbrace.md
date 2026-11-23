# collisionoption 區塊記述範例

```
sakura.collisionoption
{
nodrag0,Knob
nodrag1,Bust
nocontextmenu0,Bust
}
```

搭檔側的設定為 kero.collisionoption、char\*.collisionoption

此區塊針對碰撞判定名稱，指定停止主程式對使用者滑鼠操作的預設動作。<br />
由於依名稱查找，因此無論名稱由 collision、collisionex 或 animation\*.collision 指定，都會生效。指定的單位是名稱，而非各個 surface。若要依 surface 改變設定，請使用不同的名稱。

由於會妨礙使用者操作，請勿濫用。<br />
對於指定的碰撞判定，務必透過 cursor 區塊的 mouseup\*、mousedown\*、mouserightdown\* 等指定游標，讓使用者知道無法操作。

**対応:** SSP 2.9.38
