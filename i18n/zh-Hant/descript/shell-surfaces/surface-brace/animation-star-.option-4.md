# animation\*.option,選項

**カテゴリ:** surface brace

exclusive、background、shared-index 選項可同時指定，也可用 + 分隔指定多個選項。例如：exclusive+background<br />
animation 後方的 \* 部分是 animationID（與 animation\*.interval 的 \* 相同）。<br />
如 animation\*.option,exclusive+background,(1,3,5) 這樣指定時，只有 *exclusive* 會生效。<br />
另外，interval 為 bind 的動畫未定義 exclusive 選項。

**既定値:** 無動作

**対応:** SSP
