# SHIORI Resource

SHIORI Resource源自旧协议[SHIORI/2.5](http://usada.sakura.vg/contents/shiori.html#shiori25)中的定义：它是一种*用于获取简单字符串信息的请求*，例如显示owner draw菜单或获取homeurl。<br />
通过此规范，可以根据ghost侧的状态控制这些信息。

SHIORI/3.0及之后的版本中，经过对旧规范的整理，它在实现上与普通SHIORI Event并没有明确区别。

与普通SHIORI Event不同的是，返回值不是Sakura Script，而是作为单纯的（短）文本（包括类似bool值的内容）处理。此外，请求ID不以「On」开头，英文字母以小写形式书写。
