# animation\*.pattern\*,绘制方法,surface编号,等待时间,X坐标,Y坐标(,选项...)

**カテゴリ:** surface块

定义动画的各个帧。通常，每一帧都会先重置此前的帧，再合成到基础surface上进行绘制（严格来说，具体取决于绘制方法）。<br />
animation后面的\*部分为animationID（与animation\*.interval中的\*相同）。<br />
pattern后面的\*部分（pattern ID）为一系列animation\*.pattern定义中从0开始的连续编号。materia的上限为127。编号越小，绘制时越靠下。<br />
绘制方法请参见下文的[绘制方法](h-drowmethod/index.md)。<br />
等待时间是绘制该帧*之前*的等待时长，单位为毫秒。仅SSP支持用连字符分隔“最小等待时间-最大等待时间”的写法，此时会在最小值到最大值之间随机选择。<br />
X坐标、Y坐标用于指定该帧相对于基础（截至该帧的绘制结果）的偏移量。<br />
将surface编号设为-1可停止该动画，设为-2可停止当前运行的所有其他动画。在这两种情况下，绘制方法、X坐标和Y坐标都会被忽略。<br />
surface编号也可以指定name定义中指定的ID以外的别名。（SSP 2.8.25～）<br />
[旧定义](caption_seriko-redefine.md)：\*pattern\*,surface ID,等待时间,绘制方法,X坐标,Y坐标

选项如下。指定多个选项时，可以像「animation0.pattern0,overlay,101,700,0,0,--alpha,128,--option2,...」这样接续书写。

- **--alpha,值(0-255)**: \[SSP 2.8.37～\]指定绘制时的不透明度。0为完全透明，255为完全不透明。<br />
  例：animation0.pattern0,overlay,101,700,0,0,--alpha,128

**既定値:** 无效果

**対応:** Materia / SSP / CROW
