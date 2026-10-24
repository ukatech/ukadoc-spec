# install.txt

## 概要

[ファイル構成「インストール」](../../../manual/install.md)のページも参考に。

ゴースト、バルーン、シェル他の伺か/SSPコンテンツアーカイブ（.narなど）のインストール設定ファイル。 全てのアーカイブは解凍して手動でインストールする事もできるが、適切に設定されたinstall.txtの存在によって、インストーラ機能が有効になり、アーカイブのD&Dなどの簡易な手段でのインストールが可能となる。

## 記述例と基本の書き方

ゴーストの場合（バルーンやプラグインもtype部分を変えるだけでほぼ同じ）

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
```

追加シェルの場合

```
charset,Shift_JIS
name,凡例さんアルティメットフォーム
type,shell
directory,ultimate
accept,凡例さん
```

ゴーストのサプリメント（追加ファイル）の場合

```
charset,Shift_JIS
name,凡例さん猫化パッチ
type,supplement
accept,凡例さん
```

ゴーストにバルーンを同梱する場合

```
charset,Shift_JIS
name,凡例さん
type,ghost
directory,example
balloon.directory,example_balloon
balloon.source.directory,balloon
```

※SSPのみ　複数インストール用パッケージの場合の最上位に置くもの<br />
（同梱する各内容に置くinstall.txtは普通どおりの記述でよい）

```
charset,Shift_JIS
name,凡例さんファミリー一括入居パッケージ
type,package
```

charset指定は必ず1行目で行う（Shift_JISの場合省略可）。

name、typeは必須。directoryもtypeがsupplementかpackage以外の場合は必須。<br />
それ以外の項目は、必要に応じて指定する。

追加シェルやサプリメントの場合、想定外のゴーストにインストールされる事を避けるためにaccept指定が利用できる。<br />
特にサプリメントは予期せぬファイルの上書き破損事故の危険性があるためほぼ必須。<br />
accept指定に用いるのはゴースト名ではなく*本体側名*であることに注意。

SSPでは、バルーンやプラグインをゴーストかシェルに同梱させる場合、\*.directoryを利用する。<br />
詳しくは[「同時インストール」](introduction_install_multi.md)を参照。

なおnameは主に、[インストール系SHIORI Event](../../../list/shiori-event/install/OnInstallComplete.md)のReferenceでの通知内容に用いられる。<br />
ゴーストによってはこの情報を利用して、インストールされた直後の対象へ切り替えを実行できるような機能を備えている場合があるが、descript.txtにある実際のゴーストのnameとinstall.txtでの表記が異なると、その切り替えが正常に働かなくなるので注意。
