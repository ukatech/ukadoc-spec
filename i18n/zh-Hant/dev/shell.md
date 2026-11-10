# 建立 shell

本節說明基本的 shell 建立步驟。

但內容主要著重於設定檔的撰寫，幾乎不會提到繪圖或影像加工，敬請見諒。

另請參閱檔案結構中的[shell](../manual/shell.md)。

## 目次

1. [準備立繪圖片](shell.md#立ち絵となる画像を用意する)

2. [撰寫descript.txt](shell.md#descripttxtを書く)

3. [撰寫surfaces.txt](shell.md#surfacestxtを書く)

   1. [撰寫surfaces.txt - 碰撞判定篇](shell.md#surfacestxtを書く---当たり判定編)
   2. [撰寫surfaces.txt - 動畫篇](shell.md#surfacestxtを書く---アニメーション編)
   3. [撰寫surfaces.txt - element合成篇](shell.md#surfacestxtを書く---element合成編)

4. [撰寫readme.txt](shell.md#readmetxtを書く)

1. [關於半透明的surface](shell.md#半透明のサーフェスについて)
2. [關於追加 shell 的網路更新](shell.md#追加シェルのネットワーク更新について)
3. [關於dressup](shell.md#着せ替えについて)
4. [彙整多個surface的共用設定](shell.md#複数のサーフェスで共通の設定をまとめる)
5. [設定owner draw選單](shell.md#オーナードローメニューを設定する)
6. [設定縮圖](shell.md#サムネイル画像を設定する)

## 準備立繪圖片

首先準備要作為立繪的圖片。

可以自行繪圖，或使用稱為 free shell、公開發佈的現成 shell 等方式。

!!! tip "提示"

    可以從以下網站尋找 free shell。

    [freeshell wiki](http://wikiwiki.jp/feeshell/)

ghost 使用的基本圖片格式是 png。

jpg、bmp 等格式無法使用（SSP 可以）。

使用 png 時，尺寸和色數都沒有限制，但透明度基本上無效（只有 SSP 可依設定啟用。詳見下文[關於半透明的surface](shell.md#半透明のサーフェスについて)）。

若要縮小檔案大小，請使用工具減少色數。

構成 shell 的每張立繪，以及下文提到的動畫每一格，都以稱為*surface*的單位管理。

surface 可以準備名為「surface○○.png」（○○部分填入0以上的數字）的圖片，或透過[下文的surfaces.txt](shell.md#surfacestxtを書く)合成多張圖片。

`surface0.png`和`surface10.png`這兩張圖片基本上是必須的。

`surface0.png`是主側的基本 surface，`surface10.png`是搭檔側的基本 surface。

即使 ghost 中只有一個角色、不需要搭檔，也請準備一張以單色填滿的圖片（＝顯示時全透明。詳見下文）作為`surface10.png`。

即使將 surface 寫成`surface0000.png`、`surface0010.png`等形式，也會和`surface0.png`、`surface10.png`一樣被識別。

surface 圖片左上角的 1 個像素會作為「透明色」，在 ghost 顯示時變成透明。

如果角色身上也有和透明色相同的顏色，那些部分也會變透明，因此請使用角色沒有用到的色系作為透明色。

自行準備要當作 surface 使用的圖片時，有一點需要注意：輪廓的處理方式。

| ![](../assets/image/surface0_alias1.gif) | → | ![](../assets/image/surface0_alias2.gif) |
| --- | --- | --- |

角色輪廓變成半透明並與背景混合後，就會像右圖那樣顯示。

| ![](../assets/image/surface0_alias3.gif) | → | ![](../assets/image/surface0_alias4.gif) |
| --- | --- | --- |

像這樣避免輪廓與背景混合，就能乾淨地去除背景色。

!!! tip "提示"

    若使用 Photoshop 製作，建議使用[ClearBrain Systems](http://homepage3.nifty.com/khsoft/cbs/)（[存檔](https://web.archive.org/web/20100714191818/http://homepage3.nifty.com/khsoft/cbs/)）的[シェル＆縮小サーフェス制作補助プラグインセット for Photoshop](http://homepage3.nifty.com/khsoft/cbs/software/)（[存檔](https://web.archive.org/web/20070103182224/http://homepage3.nifty.com/khsoft/cbs/software/)），應該能更有效率地作業。

    另外，也有一款名為「[ふちどり](http://ukiya.sakura.ne.jp/index.php?%E8%87%AA%E4%BD%9C%E3%82%BD%E3%83%95%E3%83%88%E4%B8%80%E8%A6%A7%2F%E3%81%B5%E3%81%A1%E3%81%A9%E3%82%8A%E3%80%82)（[存檔](https://web.archive.org/web/20251119211223/http://ukiya.sakura.ne.jp/index.php?%E8%87%AA%E4%BD%9C%E3%82%BD%E3%83%95%E3%83%88%E4%B8%80%E8%A6%A7%2F%E3%81%B5%E3%81%A1%E3%81%A9%E3%82%8A%E3%80%82)）」的工具，可以辨識輪廓並加上「邊框」。

## 撰寫descript.txt

`descript.txt`是用來設定該 shell 基本資訊的檔案。

若未妥善準備`descript.txt`，ghost 就無法識別 shell。

首先，將以下內容複製到文字檔中，並命名為`descript.txt`，再修改成適合自己的 shell 的內容。

```
charset,Shift_JIS
type,shell
name,このシェルの名前

craftman,制作者名(英数のみで書いてください)
craftmanw,制作者名(日本語表記でも可能)
craftmanurl,制作者のURL(配布サイトurlなど)
```

charset 基本上請設為 Shift_JIS。

還有許多其他可設定的項目，但最低限度需要的差不多就是上述內容（嚴格來說，只有 name 和 type 是必填項目）。

關於本節未提及的設定，或各項設定的詳細說明，請參閱「[Shell設定](../descript/shell/index.md)」頁面。

舉一個例子，若要變更整個 shell 的基本 balloon 位置，

```
sakura.balloon.offsetx,0
sakura.balloon.offsety,0
kero.balloon.offsetx,0
kero.balloon.offsety,0
```

就需要加入這些項目。

sakura.balloon.offset會變更主側的 balloon 位置，kero.balloon.offset則會變更搭檔側的 balloon 位置。

增加數值時，x 座標會朝角色方向移動，y 座標則會往下移。

加上負號則會朝相反方向移動，x 座標會遠離角色，y 座標則會往上移。

若要在選單中顯示dressup，也需要在`descript.txt`中加入設定；相關說明請參閱[dressup設定](bind.md)頁面。

## 撰寫surfaces.txt

首先建立一個名為`surfaces.txt`的文字檔。

這個檔案用來設定動畫、合成圖片，以及使用滑鼠游標操作角色時的碰撞判定等。

也請參閱「[Shell設定 - surfaces.txt](../descript/shell-surfaces/index.md)」頁面。

建立`surfaces.txt`後，先將以下內容複製到檔案開頭。

```
charset,Shift_JIS

descript
{
version,1
}
```

第一行指定的字元編碼與`descript.txt`相同。除非有特別理由，使用Shift_JIS即可。

以下內容則是動畫設定方式的格式設定。

如果沒有這段內容，動畫相關設定就必須使用舊版定義（SERIKO/1.x）撰寫。

請注意，本頁以下的範例皆使用新版定義（SERIKO/2.0）。

!!! tip "提示"

    已使用舊版定義撰寫的surfaces.txt，可以使用以下工具將舊版定義轉換為新版定義。

    - [櫻花編輯器用巨集「SERIKO1to2.js」](http://gallnuts.webcrow.jp/etc/etc.shtml)（[封存頁面](https://web.archive.org/web/20160621201301/http://gallnuts.webcrow.jp/etc/etc.shtml)）

      使用方法：安裝[櫻花編輯器](http://sakura-editor.sourceforge.net/)，並將其作為巨集使用。詳細資訊請參閱隨附的readme.txt。

    - [將surfaces.txt從舊版定義轉換為新版定義的工具](http://typehoon.kusakage.com/zip/SurfacesTxtConverter.zip)

      使用方法：在surfaces.txt所在的資料夾中執行解壓縮後的.exe。

### 撰寫surfaces.txt - 碰撞判定篇

先從為surface定義碰撞判定開始。

首先，請在`surfaces.txt`中追加以下內容。

```
surface0
{
}
```

這表示要在這對大括號（\{\}）中設定surface0的內容。

除了碰撞判定，稍後會介紹的動畫與element設定也會寫在這裡。

在這裡像以下這樣撰寫，即可定義碰撞判定。

```
surface0
{
collision0,117,71,185,130,Face
collision1,115,174,174,217,Bust
}
```

如上所示，每個碰撞判定區域都依序寫成collision0、collision1、collision2。

請勿在同一個surface內使用重複的編號。

每個surface最多可設定256個collision。

接下來的四個數字是座標設定。

以surface圖片左上角為0,0，依序指定矩形左上角的x,y座標，以及右下角的x,y座標。

最後的字串是ghost端使用的碰撞判定名稱。

此外，可以多次設定相同名稱的碰撞判定（例如上述的Face、Bust）（例如想將手部設定為名為Hand的碰撞判定時，通常右手與左手的區域會分開，因此指定Hand的行也會分成兩行）。

!!! tip "提示"

    使用[Coordin](http://ukgk.s34.xrea.com/poskoma/#content_1_11)工具可方便地取得碰撞判定座標。

    將圖片拖放到Coordin中，再拖曳以建立矩形碰撞判定區域。

    座標會自動複製到剪貼簿，請將其貼到碰撞判定的數字中。

!!! tip "提示"

    在MATERIA中，於設定中勾選開發介面後，就能從オーナードロー選單確認碰撞判定區域。

    在SSP中，於設定→本體設定的「一般」中開啟開發者功能，再開啟功能→開發用面板，選擇顯示碰撞判定即可確認。

### 撰寫surfaces.txt - 動畫篇

伺か中的動畫（稱為SERIKO）是透過連續繪製靜止圖片來呈現的。

以下簡單介紹動畫的執行時機，以及逐張靜止圖片的疊放方式等設定方法。

以下以讓surface0眨眼為例，說明動畫設定。

```
surface0
{
animation0.interval,sometimes
animation0.pattern0,overlayfast,100,50,0,0
animation0.pattern1,overlayfast,101,50,0,0
animation0.pattern2,overlayfast,100,50,0,0
animation0.pattern3,overlay,-1,100,0,0

collision0,117,71,185,130,Face
collision1,115,174,174,217,Bust
}
```

若要讓surface0.png播放動畫，請像這樣寫上surface0，並在其下方的大括號（\{\}）中定義動畫內容。

```
animation0.interval,sometimes
```

animation\*,interval這一行用來定義該編號動畫的執行時機。

「animation」後面的數字是動畫定義的ID（包含時機設定interval，以及後續「畫格」設定pattern等）。

動畫ID可使用任意編號，不必連號，但預期*相同意義的動畫會使用相同的ID*。[※](shell.md#surfacestxtを書く---アニメーション編)

animation0.interval,後面的「sometimes」是間隔定義的內容。

如範例指定sometimes時，動畫會偶爾自行執行（每秒有二分之一的機率）。

也就是說，這項設定代表「ID為0的動畫會偶爾自行播放」。

其他可用的時機設定，請參閱「Shell設定 - surfaces.txt」中的[動畫間隔一節](../descript/shell-surfaces/surface-brace/h-animationinterval/sometimes.md)。

接著定義構成動畫的每張靜止圖片（畫格）。

請依序寫成pattern0、pattern1、pattern2。模式編號不可缺漏或重複。

請勿忘記在開頭加上同一組動畫的ID（animation\*）。

此外，interval定義行與一連串的pattern定義行不要分開寫，請連續撰寫。

```
animation0.pattern0,overlay,100,50,0,0
```

overlay的部分是繪製方式的設定。

overlay表示將圖片疊加在原始圖片上顯示的繪製方式。

除此之外還有各種繪製方式可供使用。

詳細資訊請參閱「Shell設定 - surfaces.txt」中的[surface繪製方法一節](../descript/shell-surfaces/surface-brace/h-drowmethod/base.md)。

```
animation0.pattern0,overlayfast,100,50,0,0
```

100的部分表示這個畫格要繪製surface100。

基本上可以將其視為`surface100.png`。

若指定101，則會使用`surface101.png`圖片。

若指定-1，則會停止繪製該動畫，並重設為顯示底圖（上述範例中的surface0）。

```
animation0.pattern0,overlayfast,100,50,0,0
```

50的部分是顯示時間（單位：毫秒）。

請指定*切換到該畫格前的時間*。

請注意，這不是該畫格本身的顯示時間。

```
animation0.pattern0,overlayfast,100,50,0,0
```

最後的0,0部分是畫格的顯示位置（x座標,y座標）。

指定相對於原始圖片的偏移量。

x方向向右為正，y方向向下為正。

!!! note "註"

    #### [※1](shell.md#surfacestxtを書く---アニメーション編)

    例如，角色有一個正面姿勢的surface0，以及一個側面姿勢的surface5，並且希望兩者都能播放「眨眼」動畫。

    此時除了像上述範例一樣在surface0定義眨眼動畫外，也需要在surface5進行類似的定義；但由於側面與正面姿勢不同，使用的surface圖片應該也會不同。

    不過，兩者都是以相同方式處理的「眨眼」動畫，因此最好使用相同的動畫ID（例如0）。

    尤其是在另一節說明的「[dressup](bind.md)」中，這項規則是必要的。

### Writing surfaces.txt - element compositing

element is a mechanism for combining multiple part images and treating them as a single surface.

For example, if every surface had to be provided as an image such as surface0.png, then adding more character expressions would require preparing a full-body standing illustration for each expression, even if the only difference was a slightly different mouth shape.

However, if body parts and expression parts can be separated and composited, then adding more expressions only requires preparing the expression variations as images, which would greatly reduce the overall size of the shell.

Furthermore, if the eye and mouth parts are separated, combining different eyes and mouths can create various expressions, so it is even possible to produce a range of expressions without actually drawing each one.

The following is an example of an element definition.

```
surface1
{
element0,overlay,body0.png,0,0
element1,overlay,face1.png,0,0
}
```

This defines the image made by overlaying "face1.png" on "body0.png" as surface1.

You can add as many entries as there are parts to composite.

In this case, surface1.png is not needed.

```
element0,overlay,body0.png,0,0
```

The number immediately following "element" is the element ID (serial number) on that surface.

IDs are consecutive numbers starting from 0. The smaller the number, the farther back on the screen the part is composited.

Note that png images with names such as surface\*.png are treated as parts below element0.

```
element0,overlay,body0.png,0,0
```

The next keyword is the drawing method.

It is basically [the same as the one used for animations](../descript/shell-surfaces/surface-brace/h-drowmethod/base.md), but some methods that do not purely composite images, such as start and move, cannot be used.

```
element0,overlay,body0.png,0,0
```

Next, specify the name of the file to composite.

You can specify a png file with any name.

```
element0,overlay,body0.png,0,0
```

The last two numbers specify the compositing position (x coordinate, y coordinate).

They specify how far to offset the image when compositing it over the base image.

The positive direction is right for the x-axis and down for the y-axis.

In this example, unlike the examples for [collision detection](shell.md#surfacestxtを書く---当たり判定編) and [animation](shell.md#surfacestxtを書く---アニメーション編) mentioned earlier, the element definition is on surface1 rather than surface0.

This is only an example, but there is a reason for this.[※](shell.md#surfacestxtを書く---element合成編)

When considering only the behavior of the shell (ghost) itself, there is no problem at all with using elements on surface0 or surface10.

!!! note "Note"

    #### [※2](shell.md#surfacestxtを書く---element合成編)

    Consider a web service such as a ghost database that wants to display ghost previews.

    [As mentioned earlier](shell.md#立ち絵となる画像を用意する), surface0 and surface10 are considered basic surfaces and generally cannot be omitted.

    In other words, since surface0 and surface10 can be assumed to always exist, they are convenient for use in previews.

    However, if surface0 or surface10 is constructed through element compositing, those displaying the preview would need to read the element definitions and composite them as intended.

    This presents some obstacles not only for manual work but also for systems that automate the process with programs.

    Therefore, if you intend to use such services, it may be better to provide surface0 and surface10 as actual png images.

    One service that provides such previews is the update feed "[SiReFaSo](https://sirefaso.appspot.com/) ([archive](https://web.archive.org/web/20170423052451/https://sirefaso.appspot.com/))".

## Writing readme.txt

If a file named `readme.txt` exists, it can be displayed in the owner draw menu or during installation.

It can be omitted, but if the ghost author and shell author are different, for example, it may be a good idea to specify contact information.

Enter any necessary information, such as a description of the shell or notices.

As with other files, readme can use encodings other than Shift JIS if you specify charset,UTF-8, for example, on the first line, or include a BOM.

## About translucent surfaces

To make an image translucent, create a "pna" file with the same name as the image to be made translucent.

For example, `surface0.png` would have a corresponding `surface0.pna`.

With SSP, these can also be provided for parts used in [element compositing](shell.md#surfacestxtを書く---element合成編). For example, `face1.png` would have a corresponding `face1.pna`.

A pna is simply a grayscale png representing opacity that has been renamed.

Areas made completely white in a pna are opaque, areas made completely black are transparent, and the shades in between are translucent.

| ![](../assets/image/surface0_png1.jpg) | → | ![](../assets/image/surface0_pna.jpg) | → | ![](../assets/image/surface0_png2.jpg) |
| --- | --- | --- | --- | --- |
| surface0.png |  | surface0.pna |  | Desktop display |

Translucent areas can be clicked as part of the character.

Therefore, make transparent areas completely black (RGB 0,0,0).

Also, with SSP, instead of using pna, you can create `surface*.png` images as PNGs with an alpha channel and use that alpha channel for transparency.

In that case, you need to add the following entry to `descript.txt`.

```
seriko.use_self_alpha,1
```

For information on how to create PNGs with an alpha channel, refer to the documentation for your paint software (some software may not support them. You can also search using keywords such as PNG with transparency, 32-bit PNG, or α PNG).

## 關於追加 shell 的網路更新

在 SSP 中，可以為 shell 本身新增網路更新功能。

詳細資訊請參閱「[支援網路更新](update.md)」頁面。

## 關於 dressup

在伺か中，dressup 是以動畫的一種來設定。

詳細資訊請參閱「[dressup 設定](bind.md)」頁面。

## 彙整多個 surface 共用的設定

例如，可能會有多個角色姿勢相同的 surface，而這些 surface 的碰撞判定或動畫指定等設定也完全相同。

遇到這種情況，除了在各個 surface 的 surface brace 中重複複製貼上相同設定之外，也有幾種方便的寫法。

不過，其中大多數方法都*僅限 SSP*。

詳細資訊請參閱「Shell 設定 - surfaces.txt」頁面中的「[可在 surface\* brace 中指定的 ID](../descript/shell-surfaces/surface-brace/caption_surfacebraceid.md)」。

## 設定 owner draw 選單

可以在 shell 中設定 owner draw 選單（按右鍵選單）的背景圖片、文字顏色等項目。

詳細資訊請參閱「[owner draw 選單設定](ownerdraw.md)」。

## 設定縮圖

在 owner draw 選單的 shell 選擇畫面中，游標移到 shell 上時，可以顯示縮圖。

如果有多個 shell，或是希望一眼就能分辨時，建議準備縮圖。

如果同一個資料夾中有名為 `thumbnail.png` 的圖片，就會自動使用。
