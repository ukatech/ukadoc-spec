# x-ukagaka-link スキーム

\[現在SSP限定\] ワンクリックでWebサイト上からなにかしらを実行するために、x-ukagaka-link というURLスキームを用意しています。<br />
必ず文字コードはUTF-8で、URLエンコードされた文字列である必要があります。<br />
書き方は以下の通りです。

- **x-ukagaka-link:type=event&ghost=(ゴースト名)&info=(追加情報)**: URLを開くと[OnXUkagakaLinkOpen](../../list/shiori-event/url-drop/OnXUkagakaLinkOpen.md)イベントが発生する。<br />
  (ゴースト名)はdescript.txtのnameかsakura.nameと同じもの、(追加情報)内は任意の文字列。<br />
  サンプル：[x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding](x-ukagaka-link:type=event&ghost=Emily&info=sweet-potato-feeding)
- **x-ukagaka-link:type=install&url=(エンコード済URL)**: URLを開くと、指定したURLにあるNARファイルをインストールする。<br />
  (エンコード済URL)はURLエンコードされたNARの置き場所。<br />
  サンプル：[x-ukagaka-link:type=install&url=http%3A%2F%2Fssp.shillest.net%2Fghost%2Fbonsyou.nar](x-ukagaka-link:type=install&url=http%3A%2F%2Fssp.shillest.net%2Fghost%2Fbonsyou.nar)
- **x-ukagaka-link:type=homeurl&url=(エンコード済URL)**: \[2.5.76\] URLを開くと、指定したURLを更新先URLとして認識し、ネットワーク更新と同じ方法でファイル群を取得した後、それをインストールする。<br />
  (エンコード済URL)はURLエンコードされたNARの置き場所。<br />
  サンプル：[x-ukagaka-link:type=homeurl&url=http%3A%2F%2Fms.shillest.net%2Fghost%2Fghost%2Fmobilemaster%2F](x-ukagaka-link:type=homeurl&url=http%3A%2F%2Fms.shillest.net%2Fghost%2Fmobilemaster%2F)
