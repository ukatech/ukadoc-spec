# 默认与推荐的区别

- **默认**：首次启动或重置设置时应选择的项目。<br />
  用户之后可以自由更改。
- **推荐**：行为与“默认”相同，但*表示更强的依赖关系*。<br />
  尝试切换到其他balloon时会显示警告。<br />
  随意设置会剥夺用户的选择权，因此除非存在很强的依赖关系，否则*不要随意指定*。<br />
  如果只是想防止某些balloon被删除，指定为“默认”也会显示警告。
- **shell的默认值**：也可以在shell的descript.txt的[balloon](../../shell/descript-txt/balloon.md)中指定默认值。只要用户没有显式切换balloon，每次切换shell时，balloon都会按照该shell的指定值切换。<br />
  优先级为：用户显式切换的balloon ＞ ghost的推荐值 ＞ shell的默认值 ＞ ghost的默认值。
- **其他**：也可以从balloon侧设置“推荐”关系。详情参见[balloon的descript.txt的写法](../../balloon/index.md)。
