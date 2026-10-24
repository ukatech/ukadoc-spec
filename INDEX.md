# UKADOC トップページ

## ukadocについて

伺か関連の仕様文書集約プロジェクトである[UKADOC project](https://github.com/ukatech/ukadoc-spec)の編集するドキュメント集です。

*[SSP](http://ssp.shillest.net/)についてはここのドキュメントが公式文書*として扱われます。

誤りの指摘や、質問、意見、要望、情報提供などは[ばぐとら研究所ToDo](http://ssp.shillest.net/bts/?project=misc&action=top)までお願いします。

ゴースト制作のためのサイト内の文章の引用・転載はご自由に。

> AI エージェント向けに、探し方の案内 [llms.txt](https://ukatech.shillest.net/ukadoc-spec/llms.txt) を用意しています。各ページの Markdown 原稿は、リポジトリと同じパスの `.md`（例: `https://ukatech.shillest.net/ukadoc-spec/manual/ghost.md`）で取得できます。

## 対象version

- [SSP](http://ssp.shillest.net/) 最新版(公式仕様書)
- [MATERIA](http://usada.sakura.vg/) period 583
- [CROW](http://crow.aqrs.jp/) ver0.5.2(開発版)
- [ninix-kagari](http://github.com/Tatakinov/ninix-kagari) 最近版

## 外部リンク

- [伺か開発情報検索](http://ukadev.shillest.net/)
- [SSP起動オプション(SSPヘルプ)](https://ukatech.shillest.net/ukadoc-ssp/functions/option/)
- [伺か公式仕様書](http://usada.sakura.vg/contents/specification.html)
- [CROW・SSP仕様書](http://crow.aqrs.jp/reference/all/)
- [大八州.NET　非公式仕様書](http://www.ooyashima.net/db/)
- [駄でべwiki　仕様メモ](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

## ukadocの見方

サイドバーにある記事はカテゴリーごとにそれぞれ以下のような内容を扱っています。

- **ファイル構成**: 各伺か関連コンテンツを構成するファイルの解説や、ディレクトリ構造について扱っています。

  どのようなファイルが必要であるか・利用できるかの全体像を把握したい場合などに参照できるでしょう。

- **設定ファイル**: 各伺か関連コンテンツに用いられる個々の設定ファイルの、記述内容についての解説です。

  それぞれの設定ファイルの記述時に参照できるでしょう。できる限り凡例も用意しています。

- **さくらスクリプト**: ゴーストの動作指示である「さくらスクリプト」の各命令についての解説です。

  どのような命令が可能であるか把握し、利用する際に参照できるでしょう。

- **イベント**: ベースウェアがSHIORIやPLUGINなどに対して通知するイベントのIDそれぞれの解説です。

  ゴーストやPLUGIN、SHIORIなどの製作にあたって、個々のイベントやそのReferenceについて知りたい場合に参照できるでしょう。

- **規格**: 各伺か関連コンテンツにまつわる諸々の規格のまとめです。

  どちらかといえばSHIORIやSAORI、ベースウェアなどの、システムの基幹的部分に関係する情報です。

- **HowTo**: 各伺か関連コンテンツの作成にまつわる、基礎的な方法の紹介です。

  ただし個別のケースに応じたTIPSまで網羅するのは現実的には難しいので、より具体的な情報をお求めの場合は、外部のサイトも探してみてください。

- **その他**: その他、SSP等ベースウェアの仕様に関するメモや補足記事などです。

## 目次

### ファイル構成

- [全体の構成](manual/directory.md)
- [ゴースト](manual/ghost.md)
- [シェル](manual/shell.md)
- [オーナードローメニュー](manual/owner-draw-menu.md)
- [インストール](manual/install.md)
- [ネットワーク更新](manual/update.md)
- [トランスレータ](manual/translator.md)
- [バルーン](manual/balloon.md)

### 設定ファイル

- Ghost
  - [descript.txt](descript/ghost/index.md)
- Shell
  - [descript.txt](descript/shell/index.md)
  - [surfaces.txt](descript/shell-surfaces/index.md)
  - [surfacetable.txt](descript/shell-surfacetable/index.md)
- Balloon
  - [descript.txt](descript/balloon/index.md)
  - [balloon(s/k)\*s.txt](descript/balloon/balloonsoption/index.md)
- Plugin
  - [descript.txt](descript/plugin/index.md)
- Headline
  - [descript.txt](descript/headline/index.md)
- Install/Update
  - [install.txt](descript/install/index.md)
  - [delete.txt](descript/install/delete.txt/index.md)
  - [developer_options.txt](descript/install/developer_options.txt/index.md)
  - [updates2.dau/updates.txt](spec/update-file/index.md)

### さくらスクリプト

- [SAKURA Script](list/sakura-script/index.md)
- [Property System](list/propertysystem/index.md)

### イベント

- SHIORI
  - [SHIORI Event](list/shiori-event/index.md)
  - [SHIORI Event（外部）](list/shiori-event-ex/index.md)
  - [SHIORI Resource](list/shiori-resource/index.md)
- PLUGIN
  - [PLUGIN Event](list/plugin-event/index.md)

### 規格

- [SHIORI/3.0](spec/shiori3/index.md)
- [SSTP/1.x](spec/sstp/index.md)
- [SAORI/1.0（外部サイト）](http://www.boreas.dti.ne.jp/~sdn/saori.html)
- [SAORI over DirectSSTP](spec/saori-ex/index.md)
- [PLUGIN/2.0](spec/plugin.md)
- [HEADLINE/2.0](spec/headline.md)
- [DLL](spec/dll.md)
- [FMO/Mutex](spec/fmo-mutex/index.md)
- [Web関連](spec/web/index.md)
- [仕様メモ（外部サイト）](http://emily.shillest.net/specwiki/index.php?%E4%BB%95%E6%A7%98%E3%83%A1%E3%83%A2)

### HowTo

- [配布用ファイルの作成](dev/nar.md)
- [ネットワーク更新への対応](dev/update.md)
- [シェルの作成](dev/shell.md)
- [着せ替えの設定](dev/bind.md)
- [オーナードローメニューの設定](dev/ownerdraw.md)
- [エラーメッセージの解消](dev/shell-error.md)

### その他

- [補足: SHIORI Eventとは](memo/shiori-event.md)
- [メモ](memo/memo.md)
