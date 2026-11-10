# OnHandActivate

**カテゴリ:** ghost「The Hand」

The Hand前去触碰其他ghost或触碰结束时触发。<br />
触碰期间，会以Sender:The Hand向ghost发送(OnMouseMove|OnMouseDoubleClick|OnMouseWheel)事件。

- **Reference0**: 普通触碰开始：NormalStart<br />
  普通触碰结束：NormalEnd<br />
  必杀技开始：SuperStart<br />
  必杀技进行中：SuperContinue<br />
  必杀技结束：SuperEnd<br />
  必杀技进行中触发追踪：SuperHoming
- **Reference1**: 命中判定名称。<br />
  如果被停止，则为escaped。<br />
  必杀技时为1～4。
- **Reference2**: 对方发生的事件。<br />
  普通时：(OnMouseMove|OnMouseDoubleClick|OnMouseWheel)<br />
  必杀技期间：触碰次数<br />
  必杀技结束时：(MAX触碰次数|escaped|nocollision|attacked|deleted)
- **Reference3**: 前去触碰时使用的脚本。<br />
  必杀技期间为命中判定名称。
- **Reference4**: shell编号。
