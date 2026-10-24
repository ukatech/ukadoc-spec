# blend-linear-burn-fast

**カテゴリ:** surfaceブレス \> 描画メソッド

*ベースレイヤ*の不透明度に応じて、*新規レイヤ*を焼き込みリニア合成で重ねる。<br />
挙動はoverlay-fastと同様で外形は変わらないが、上書きの代わりに現在のサーフェスに対して焼き込みリニア合成処理を行う。<br />
着せ替え・elementでも使用できる。<br />
名称中の「fast」は歴史的な経緯によるもので、処理速度が速いわけではない。<br />
シェルのdescript.txtに[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)を設定することを推奨する。

**対応:** SSP 2.8.40
