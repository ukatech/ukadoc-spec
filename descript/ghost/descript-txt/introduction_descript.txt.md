# descript.txt（Ghostの）

## 概要

ゴーストの基本設定ファイル。<br />
ゴースト名や作者名を始め、shioriの設定や、バルーンの基本位置情報、アイコンなど様々な情報を設定する（できる）。

## 記述例と基本の書き方

```
charset,Shift_JIS
type,ghost
name,凡例さん
sakura.name,凡例さん
kero.name,斑糲岩
homeurl,http://ssp.shillest.net/ukadoc/manual/hogehoge/example/

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

shiori,satori.dll
```

type、name、sakuraname、keroname、craftman、craftmanwは必須（SSPの場合省略可能なものもある）。

SHIORIに里々などのdll名が「shiori.dll」でないものを使う場合、shioriにdll名の指定を忘れないように注意。

homeurlはdescript.txtに書く他、ベースウェアからの[SHIORI Resource](../../../list/shiori-resource/ghost/homeurl.md)要求に返却する方法でも設定可能（方法はSHIORIによるため略）。<br />
基本的にどちらか一方で指定すればよく、両方指定する場合はサイト移転時などに片方を修正し忘れるなどのミスに要注意。

なお、\\や%で始まる文字列はさくらスクリプトや環境変数のタグと見なされ、セキュリティ上のリスクから破棄される。もし単なる文字としてそれらを含めたい場合は、\\\\や\\%などとしてエスケープする必要がある。
