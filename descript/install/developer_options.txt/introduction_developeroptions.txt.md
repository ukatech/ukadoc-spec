# developer_options.txt

## 概要

[ファイル構成「ネットワーク更新」](../../../manual/update.md)・[ファイル構成「インストール」](../../../manual/install.md)のページも参考に。

SSPがアーカイブやネットワーク更新情報ファイルの作成時に、対象とするファイルにオプションを設定するためのもの。<br />
SSPにゴーストなどのパッケージのフォルダをD&Dすることで、アーカイブ（.nar）やupdateファイル（updates2.dau）を作成する機能があるが、その機能の実行時に参照される。<br />
従って原則的には他のツール、「そだて」や「ゴースト配布系自動化システム」を使ってそれらのファイルを作成した場合は*全く無関係*なので注意。<br />
例外として、「さとりすと」のようにdeveloper_options.txtを読み取って利用する機能が実装されているものもある。

## 記述例

```
ghost/master/savedata.txt,noupdate
shell/old/,nonar
ghost/master/profile/,nonar,noupdate
```

## 注意点

設定は一つの対象（ファイル・フォルダ）に対して*1行で行う*事に注意。例えば以下のような記述を行うと、*後ろ（下）で行っている設定だけが反映されて、nonarオプションが無効*になる。

```
ghost/master/profile/,nonar
ghost/master/profile/,noupdate
```

二つのオプションを指定する場合、正しくは先述の通り

```
ghost/master/profile/,nonar,noupdate
```

とする。
