# collisionoption 大括號記述範例

```
sakura.collisionoption
{
nodrag0,Knob
nodrag1,Bust
nocontextmenu0,Bust
}
```

搭檔側的設定為 kero.collisionoption、char\*.collisionoption

此大括號針對碰撞判定名稱，指定停止本體對使用者滑鼠操作的預設動作。<br />
由於以名稱查找，因此無論名稱是由 collision、collisionex 或 animation\*.collision 指定，都會套用。設定是以名稱為單位，而非以 surface 為單位。若要依 surface 改變設定，請使用不同名稱。

此設定會妨礙使用者操作，請勿濫用。<br />
務必透過 cursor 大括號的 mouseup\*、mousedown\*、mouserightdown\* 等項目，為指定的碰撞判定設定能讓使用者了解無法操作的游標。

**対応:** SSP 2.9.38
