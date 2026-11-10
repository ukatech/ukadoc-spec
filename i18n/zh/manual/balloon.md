# Balloon

The files in a balloon folder are as follows.

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

- **[descript.txt](../descript/balloon/index.md)**: File used to identify the balloon.

  It has more fields than the descript.txt for a ghost or shell.

  See the [linked page](../descript/balloon/index.md) for details.

- **[balloons\*s.txt/balloonk\*s.txt/balloonc\*s.txt](../descript/balloon/balloonsoption/index.md)**: Files for per-balloon settings.

  When provided for the surface with the corresponding ID (balloons1s.txt for balloons1.png), the settings override those in descript.txt for that surface.

  Use these files when changing settings for only certain surface IDs, for example.

  Note the s in the filename (use balloons\**s*.txt, not balloons\*.txt)

  These files can also be used for input boxes. Specify them in balloonc\*s.txt.

  See the [linked page](../descript/balloon/balloonsoption/index.md) for details.

- **readme.txt**: File for balloon authors to provide information such as the distribution source.

  It is optional, but providing one makes it accessible during installation and from baseware menus.

- **balloons\*.png**: The speech balloon for the main character.

  \* is a number that becomes the balloon surface ID.

  Even-numbered IDs are left-facing balloons, and odd-numbered IDs are right-facing balloons; they form pairs.

  The following assignments are common, but are not required. You can add pairs such as 4-5 and 6-7, or use only 0-1.

  - balloons0.png　and　balloons1.png　……　Normal speech balloons (left and right)
  - balloons2.png　and　balloons3.png　……　Tall speech balloons (left and right)

- **balloons\*.pna**: Not supported by MATERIA.

  A grayscale PNG image (black: transparent ←→ opaque: white) renamed with the pna extension.

  If you provide a pna matching the PNG with the corresponding ID (balloons0.pna for balloons0.png), it can be used to set transparency.

  In SSP, the alpha channel in the PNG itself can also be used via [settings](../descript/balloon/descript-txt/use_self_alpha.md).

  This file is optional.

- **balloonk\*.png**: The speech balloon for the partner (or the third character onward).

  It is basically the same as balloons\*.png, but is generally somewhat shorter.

  This file is optional. If omitted, the corresponding ID from the main character is used.

- **balloonk\*.pna**: The balloonk\*.png version of balloons\*.pna. See the earlier description of balloons\*.pna.

- **balloonp\*def\*.png**: Speech balloons for the third character onward. The balloon for `\p[2]` is balloonp2def0.png / balloonp2def1.png.

  This file is optional. If omitted, balloonk is used, or balloons if that is also unavailable.

- **balloonp\*def\*.pna**: The balloonp\*def\*.png version of balloons\*.pna. See the earlier description of balloons\*.pna.

- **balloonc\*.png**: Balloon input windows.

  \* is a number from 0 to 3 (or 4 in SSP); each file number corresponds to the following.

  - balloonc0.png　……　Send box
  - balloonc1.png　……　Communicate box
  - balloonc2.png　……　Teach box
  - balloonc3.png　……　Input box
  - balloonc4.png　……　Address Bar box (SSP only)
  - balloonc5.png　……　Multiline input (Textarea) box (SSP 2.9.10 and later. If unavailable, the image for the balloon itself is used)

- **balloonc\*.pna**: The input box version of balloons\*.pna.

- **online\*.png**: Images displayed while receiving network information.

  Animation repeats in numerical order.

- **arrow\*.png**: Images used to scroll text.

  0 points up, and 1 points down.

  In SSP, images specifically for the main character and partner can be defined. See below.

- **sstp.png**:

  - When displaying sender information and similar data upon receiving SSTP
  - When executing the `\![*]` tag (SSP also supports %\*)

  The image displayed in these cases. In SSP, separate images can be configured for each use. See below.

- **thumbnail.png**: Thumbnail displayed when selecting a balloon in the menu tree.

  Supported image formats are PNG and JPG.

  Renaming a PNG to PNR makes pixels matching the color of the top-left pixel (coordinates 0,0) transparent.

  This file is optional.

SSP only. All files are optional.

- **ok_down.png/ok_up.png**: Images for the OK button in input box windows.

- **cancel_down.png/cancel_up.png**: Images for the Cancel button in input box windows.

- **mode_down.png/mode_up.png**: Images for the mode switch button.

- **sstp_new.png / sstp_newk.png / sstp_newp\*def.png**: Images used to display sender information and similar data upon receiving SSTP (unlike sstp.png, these are dedicated to this use).

- **marker.png / markers.png / markerk.png / markerp\*def.png**: Images displayed by the `\![*]` tag (SSP also supports %\*) (unlike sstp.png, these are dedicated to this use).

  markers is for the main character (using marker is recommended for compatibility with older versions), markerk is for the partner, and markerp2def onward are for `\p[2]` onward.

- **arrows\*.png / arrowk\*.png / arrowp\*def.png**: Images used to scroll text. Supported only in SSP 2.4.78 and later.

  0 points up, and 1 points down.

  arrows is for the main character (using arrow is recommended for compatibility with older versions), arrowk is for the partner, and arrowp2def onward are for `\p[2]` onward.

- **clickwait.png / clickwaits\*.png / clickwaitk\*.png / clickwaitp\*def.png**: Images used to indicate a click wait (`\x`). Supported only in SSP 2.5.54 and later.

  clickwaits is for the main character, clickwaitk is for the partner, and clickwaitp2def onward are for `\p[2]` onward.
