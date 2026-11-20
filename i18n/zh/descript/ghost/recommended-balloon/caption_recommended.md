# 默认与推荐的区别

- **默认**：首次启动或重置设置时应选择的项。<br />
  用户之后可以自由更改。
- **推荐**：行为与“默认”相同，但*表示更强的依赖关系*。<br />
  尝试切换到其他balloon时会显示警告。<br />
  随意设置会剥夺用户的选择权，因此除非存在很强的依赖关系，否则*不要随意指定*。<br />
  如果只是想防止删除部分balloon，指定为“默认”也会显示警告。
- **shell的默认项**：也可以通过shell的descript.txt中的[balloon](../../shell/descript-txt/balloon.md)指定默认项。<br />
  切换shell时，如果用户曾在该shell中切换过balloon，则切换到该balloon；否则按“ghost的推荐项 ＞ shell的默认项 ＞ ghost的默认项”的顺序确定切换目标。
- **其他**：也可以从balloon侧设置“推荐”关系。详情参见[balloon的descript.txt的写法](../../balloon/index.md)。
