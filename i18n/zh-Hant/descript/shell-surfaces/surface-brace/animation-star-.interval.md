# animation\*.interval,間隔

**カテゴリ:** surface brace

動畫開始的時間點（週期）定義。<br />
間隔請參照下列[動畫間隔](h-animationinterval/index.md)。僅限 SSP，可用 + 分隔並列出多個項目來組合指定。<br />
\* 部分（animationID）可使用任意數字。在該 scope（`\0`、`\1`、...）內的所有 surface 中，相同 ID 的動畫都應具有相同意義（例如「眨眼」、「嘴部動作」、「相同服裝的 dressup」等）。<br />
interval 定義表示該 ID 的整體動畫定義起點，必須在一系列 animation 定義中最先記述。<br />
動畫的重疊方式與 ID 順序之間的關係，請參照 [animation-sort](../descript-brace/animation-sort.md)。<br />
[舊定義](caption_seriko-redefine.md)：\*interval,間隔

**既定値:** 無動作

**対応:** Materia / SSP / CROW
