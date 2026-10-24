# トランスレータ

トランスレータのことをゴーストではMAKOTOと称する。

ゴースト側・シェル側の両方に配置できる（CROWはゴースト側のみ）。

ゴースト側で使用する場合はmaster直下に`makoto.dll`がある必要がある。

```
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-makoto.dll
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　:
　　　　　　:
```

シェル側で使用する場合は各シェルのフォルダ直下にmakoto.dllがある必要がある。

```
+-(myghost)
　　+-shell
　　　　+-master(またはadditional_shell)
　　　　　　+-makoto.dll
　　　　　　+-descript.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-surfaces.txt
　　　　　　:
　　　　　　:
```

SHIORIが作成したスクリプトに対し、フィルタとして働き文字列を置き換えるための仕組み。

ゴースト側とシェル側療法にある場合、先にゴースト側のトランスレートが行われてから、続けてシェル側のトランスレートが行われる。

トランスレートのタイミングはバルーンに表示される直前。

SHIORI同様MAKOTOとして使用できるファイルは多数あり、詳しい使い方はそれぞれのドキュメントを参照する必要がある。

過去、SHIORIのなかった時代にトークに変化を与えるために使用されていたが、今はそのような役割は主にSHIORIが担う。

現在では、シェルによって口調を変化させるなどの仕掛けに利用される事がある。

SHIORI EventのOnTranslateでもトランスレートが可能（＝SHIORIはゴースト側のMAKOTOを兼ねる）。

もしMAKOTOとSHIORIの両方でトランスレートをする場合の処理順序は、SHIORI→MAKOTO。
