# バルーン

バルーンフォルダのファイルは以下の通り。

```filetree
+-(myballoon)
　　+-descript.txt
　　+-readme.txt
　　+-balloons*.png
　　+-balloons*.pna （MATERIA不可）
　　+-balloons*s.txt
　　+-balloonk*.png
　　+-balloonk*.pna （MATERIA不可）
　　+-balloonk*s.txt
　　+-balloonp*def*.png  (SSP 2.5.51～)
　　+-balloonp*def*.pna  (SSP 2.5.51～)
　　+-balloonp*def*s.txt
　　+-balloonc*.png
　　+-balloonc*.pna  (SSP 2.5.37～)
　　+-balloonc*s.txt  (SSP 2.5.37～)
　　+-online*.png
　　+-sstp.png
　　+-arrow0.png
　　+-arrow1.png
　　+-arrows0.png  (SSP 2.4.78～)
　　+-arrows1.png  (SSP 2.4.78～)
　　+-arrowk0.png  (SSP 2.4.78～)
　　+-arrowk1.png  (SSP 2.4.78～)
　　+-arrowp*def0.png  (SSP 2.5.51～)
　　+-arrowp*def1.png  (SSP 2.5.51～)
　　+-thumbnail.png
　　+-ok_down.png/ok_up.png （SSPのみ）
　　+-cancel_down.png/cancel_up.png （SSPのみ）
　　+-mode_down.png/mode_up.png （SSPのみ）
　　+-sstp_new.png （SSPのみ）
　　+-sstp_newk.png  (SSP 2.5.51～)
　　+-sstp_newp*def.png  (SSP 2.5.51～)
　　+-marker.png （SSPのみ）
　　+-markers.png  (SSP 2.4.78～)
　　+-markerk.png  (SSP 2.4.78～)
　　+-markerp*def.png  (SSP 2.5.51～)
　　+-clickwait.png  (SSP 2.5.54～)
　　+-clickwaits.png  (SSP 2.5.54～)
　　+-clickwaitk.png  (SSP 2.5.54～)
　　+-clickwaitp*def.png  (SSP 2.5.54～)
```

- **[descript.txt](../descript/balloon/index.md)**: バルーンを識別するためのファイル。

  ゴーストやシェルのdescript.txtと比べても記載項目が多い。

  詳細は[リンク先](../descript/balloon/index.md)を参照。

- **[balloons\*s.txt/balloonk\*s.txt/balloonc\*s.txt](../descript/balloon/balloonsoption/index.md)**: バルーンごとの個別設定用ファイル。

  対応するIDのサーフェス（balloons1.pngに対してballoons1s.txt）について用意すると、そのサーフェスに対してdescript.txtの記述を上書きする形で適応される。

  特定IDのサーフェスのみ設定を変更したいとき等に使用する。

  ※ファイル名のsに注意（balloons\*.txtではなくてballoons\**s*.txt）

  入力ボックスにも利用できるようになった。balloonc\*s.txtで指定すること。

  詳細は[リンク先](../descript/balloon/balloonsoption/index.md)を参照。

- **readme.txt**: バルーン作者が配布元などを記載するためのもの。

  省略可能だが、用意しておくと、インストール時やベースウェアのメニューなどから参照できる。

- **balloons\*.png**: 本体側の吹き出し。

  \*はバルーンのサーフェスIDになる数字。

  偶数番のIDは左向きのバルーン、奇数番のIDは右向きのバルーンとして、二つセットになる。

  なお一般的に下記のような割り当てになっているが、自由。4-5、6-7とセットを追加していってもよいし0-1だけでもよい。

  - balloons0.png　および　balloons1.png　……　通常の吹き出し(左・右)
  - balloons2.png　および　balloons3.png　……　縦長の吹き出し(左・右)

- **balloons\*.pna**: MATERIAでは不可。

  グレースケール（黒：透明←→不透明：白）のpng画像の拡張子部分pnaにリネームしたもの。

  対応するID（balloons0.pngに対してballoons0.pna）のpngに対応したpnaを用意すると、それを透明度設定として利用できる。

  SSPでは[設定](../descript/balloon/descript-txt/use_self_alpha.md)でpng自体のアルファチャンネルを利用できる点も同じ。

  このファイルは省略可。

- **balloonk\*.png**: 相方側（または三人目以降）の吹き出し。

  基本的にballoons\*.pngと同じだが縦サイズがやや小さめなのが一般的。

  このファイルは省略可。省略時は本体側の対応するIDのものが使われる。

- **balloonk\*.pna**: balloons\*.pnaのballoonk\*.png版。説明は先述のballoons\*.pna参照。

- **balloonp\*def\*.png**: 三人目以降の吹き出し。`\p[2]`に当たるバルーンが balloonp2def0.png / balloonp2def1.png になる。

  このファイルは省略可。省略時はballoonk、さらになければballoonsが使われる。

- **balloonp\*def\*.pna**: balloons\*.pnaのballoonp\*def\*.png版。説明は先述のballoons\*.pna参照。

- **balloonc\*.png**: バルーンの入力ウインドウ。

  \*には0から3（SSPは4）の数字が入り、各番号のファイルは以下に対応している。

  - balloonc0.png　……　Sendボックス
  - balloonc1.png　……　Communicateボックス
  - balloonc2.png　……　Teachボックス
  - balloonc3.png　……　Inputボックス
  - balloonc4.png　……　Address Barボックス(SSP専用)
  - balloonc5.png　……　複数行入力(Textarea)ボックス(SSP 2.9.10以降。無い場合はバルーン本体の画像を使う)

- **balloonc\*.pna**: balloons\*.pnaの入力ボックス版。

- **online\*.png**: ネットワーク情報受信中に表示される画像。

  番号順にアニメーションを繰り返す。

- **arrow\*.png**: 文章をスクロールさせるのに使用する画像。

  0が上向き、1が下向き。

  SSPでは本体・相方専用のものを定義できる。後述。

- **sstp.png**:

  - SSTP受信時に、送信者情報などを表示する際
  - `\![*]`タグ（SSPは%\*でも同様）を実行した際

  に表示される画像。SSPではそれぞれ専用のものを設定できる。後述。

- **thumbnail.png**: メニューツリーでバルーンの選択時に表示されるサムネイル。

  使用可能な画像形式はpngもしくはjpg。

  pngをpnrにリネームすると画像左上の1ドット(座標0,0)と同色が透過される。

  このファイルは省略可能。

以下SSP専用。全て省略可能。

- **ok_down.png/ok_up.png**: 入力ボックス系のOKボタンの画像。

- **cancel_down.png/cancel_up.png**: 入力ボックス系のキャンセルボタンの画像。

- **mode_down.png/mode_up.png**: モード切替ボタンの画像。

- **sstp_new.png / sstp_newk.png / sstp_newp\*def.png**: SSTP受信時に、送信者情報などを表示する際に使用される画像（sstp.pngと異なりこの用途専用）。

- **marker.png / markers.png / markerk.png / markerp\*def.png**: `\![*]`タグ（SSPは%\*でも同様）で表示される画像（sstp.pngと異なりこの用途専用）。

  markersが本体用(旧バージョン対応のためにmarkerで代用を推奨)、markerkが相方用、markerp2def以降が`\p[2]`以降用。

- **arrows\*.png / arrowk\*.png / arrowp\*def.png**: 文章をスクロールさせるのに使用する画像。SSP 2.4.78以降専用。

  0が上向き、1が下向き。

  arrowsが本体用(旧バージョン対応のためにarrowで代用を推奨)、arrowkが相方用、arrowp2def以降が`\p[2]`以降用。

- **clickwait.png / clickwaits\*.png / clickwaitk\*.png / clickwaitp\*def.png**: クリック待ち(`\x`)を表すのに使用する画像。SSP 2.5.54以降専用。

  clickwaitsが本体用、clickwaitkが相方用、clickwaitp2def以降が`\p[2]`以降用。
