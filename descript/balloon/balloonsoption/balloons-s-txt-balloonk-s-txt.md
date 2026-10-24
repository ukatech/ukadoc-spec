# balloons\*s.txt/balloonk\*s.txt

## 概要

バルーンの各サーフェス（balloons0.png、balloonk0.png、...）や入力ボックスに対する個別設定ファイル。<br />
descript.txtでの設定を標準設定とし、こちらに同じ項目を設定すれば、設定した項目のみ上書きされる。

一つのサーフェスに対して一つ（例えばballoons0.pngに対してballoons0s.txt。ファイル名末尾のsに注意）用意できる。

基本的に全ての項目について設定できるが、バルーン全体に関する設定であるname、type、craftman、craftmanurl、id、homeurl、readmeについては設定不可（無意味）。<br />
また、シェル側サーフェスに対する表示位置の調整用にwindowposition.x、windowposition.yという設定が追加されている（SSPのみdescript.txt側でも設定可能）。

複数行入力ボックス用のballoonc5.png(SSP 2.9.10)では、balloonc5s.txtのcommunicatebox.x/y/width/heightが入力欄とその下端のボタン行を合わせた範囲になる。<br />
この範囲はdescript.txt側の値(1行の入力ボックス向け)を引き継がない。balloonc5s.txtで指定しなかった場合は、画像の四辺から8ピクセル内側の範囲になる。<br />
文字の大きさはballoonc5s.txtのfont.height(省略時はdescript.txtのfont.height)、書体と色はcommunicatebox.font.name/font.color/background.colorに従う。

**対応:** Materia / SSP / CROW
