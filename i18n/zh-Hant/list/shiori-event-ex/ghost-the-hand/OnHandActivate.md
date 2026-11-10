# OnHandActivate

**カテゴリ:** ghost「The Hand」

The Hand前往觸碰其他ghost或完成觸碰時會發生。<br />
觸碰期間會以Sender:The Hand為寄件者，向ghost傳送(OnMouseMove|OnMouseDoubleClick|OnMouseWheel)事件。

- **Reference0**: 一般觸碰開始：NormalStart<br />
  一般觸碰結束：NormalEnd<br />
  必殺技開始：SuperStart<br />
  必殺技進行中：SuperContinue<br />
  必殺技結束：SuperEnd<br />
  必殺技進行中觸發追蹤：SuperHoming
- **Reference1**: 命中判定名稱。<br />
  若遭到停止則為escaped。<br />
  必殺技時為1～4。
- **Reference2**: 對手身上發生的事件。<br />
  一般狀態：(OnMouseMove|OnMouseDoubleClick|OnMouseWheel)<br />
  必殺技期間：觸碰次數<br />
  必殺技結束時：(MAX觸碰次數|escaped|nocollision|attacked|deleted)
- **Reference3**: 前往觸碰時執行的指令。<br />
  必殺技期間為命中判定名稱。
- **Reference4**: shell編號。
