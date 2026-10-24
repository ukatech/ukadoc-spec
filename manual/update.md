# ネットワーク更新

ネットワーク更新のための設定などは「[ネットワーク更新への対応](../dev/update.md)」のページを参照。

ネットワーク更新に関係するファイルの配置は以下の通り。

- **ゴーストの場合**:

  ```
  +-(myghost)
  　　+-ghost
  　　+-shell
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt (SSPのみ)
  　　+-readme.txt
  　　+-thumbnail.png
  ```

- **(SSPのみ)追加シェルをネットワーク更新に対応させる場合**:

  ```
  +-(myshell)
  　　+-ghost
  　　+-shell
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt
  　　+-readme.txt
  　　+-thumbnail.png
  ```

- **(SSPのみ)バルーンをネットワーク更新に対応させる場合**:

  ```
  +-(myballoon)
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt
  　　+-descript.txt
  　　+-balloons*s.txt
  　　+-balloonk*s.txt
  　　+-readme.txt
  　　+-balloons*.png
  　　+-balloonk*.png
  　　:
  　　:
  ```

  他、プラグイン、ヘッドラインなども同様に、そのフォルダ内に設置すればよい。

- **updates2.dau**: 更新対象とするファイルのMD5ハッシュ値などが列挙されたファイル。

  ネットワーク更新で、サーバにあるファイルと実際にダウンロードされたファイルの間で、ファイルが破損・改竄などされていないかを検出する目的で用いられる。

  普通ベースウェアの機能を用いるなどして作成するもので、人が編集する必要はない。

  作成手順などは「[ネットワーク更新への対応](../dev/update.md)」のページを参照

- **updates.txt**: updates2.dauとほぼ同じ意味を果たすもの。どちらか一方があればよい（両方あっても問題ない）。

  書式が多少異なるほか、拡張子制限でdauがアップロードできない等の問題を回避できる。

- **[delete.txt](../descript/install/delete.txt/index.md)**: ファイルの削除設定ファイル。

  サーバ上でupdates2.dauと同じ位置に配置する。

  不要になったファイルが肥大するのを防ぐなどの目的で使う。

  書式など詳しくは[リンク先](../descript/install/delete.txt/index.md)を参照。

- **[developer_options.txt](../descript/install/developer_options.txt/index.md)**: SSPのみ。

  updates2.dauを作成したい位置（一番上のディレクトリ）に配置する。

  SSPでupdates2.dau（updates.txt）を作る場合に、対象に含めないファイルなどを指定するためのファイル。

  サーバ上にアップロードする必要はない（自身を除外ファイルに指定するなどで可能）が、あっても害はないので、ユーザが再度narにしなおすなどの状況を考えつつ自由に。

  書式など詳しくは[リンク先](../descript/install/developer_options.txt/index.md)を参照。
