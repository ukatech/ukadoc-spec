# animation\*.option,exclusive

**カテゴリ:** surface brace

動畫的互斥執行選項。<br />
也就是說，指定 exclusive 選項的動畫一旦開始執行，所有其他動畫都會停止；直到該動畫結束前，其他任何動畫都不會開始。<br />
animation 後方的 \* 部分是 animationID（與 animation\*.interval 的 \* 相同）。<br />
另外，interval 為 bind 的動畫未定義此選項。<br />
僅限 SSP，可用 animation\*.option,exclusive,(1,3,5) 這種寫法，只對指定 ID 的動畫進行有限範圍的互斥控制。<br />
[舊定義](caption_seriko-redefine.md)：\*option,exclusive

**既定値:** 無動作

**対応:** Materia / SSP / CROW
