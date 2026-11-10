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

- **[descript.txt](../descript/balloon/index.md)**: A file used to identify the balloon.

  It has more entries than the descript.txt for a ghost or shell.

  See the [linked page](../descript/balloon/index.md) for details.

- **[balloons\*s.txt/balloonk\*s.txt/balloonc\*s.txt](../descript/balloon/balloonsoption/index.md)**: Files for configuring individual balloons.

  When provided for a surface with the corresponding ID (balloons1s.txt for balloons1.png), the settings in descript.txt are overridden for that surface.

  Use these files when you want to change settings for only a specific surface ID, for example.

  ※Note the s in the file name (it is balloons\**s*.txt, not balloons\*.txt)

  These files can also be used for input boxes. Specify the settings in balloonc\*s.txt.

  See the [linked page](../descript/balloon/balloonsoption/index.md) for details.

- **readme.txt**: A file for balloon authors to provide information such as the distribution source.

  This file is optional, but if provided, it can be viewed during installation and from baseware menus.

- **balloons\*.png**: The main-side speech balloons.

  \* is a number representing the balloon surface ID.

  Even-numbered IDs are left-facing balloons, and odd-numbered IDs are right-facing balloons; they are used in pairs.

  The usual assignments are as follows, but these are not fixed. You can add pairs such as 4-5 and 6-7, or use only 0-1.

  - balloons0.png　and　balloons1.png　……　normal speech balloons (left and right)
  - balloons2.png　and　balloons3.png　……　vertically elongated speech balloons (left and right)

- **balloons\*.pna**: Not supported in MATERIA.

  A grayscale PNG image (black: transparent ←→ opaque: white) renamed with the pna extension.

  If you provide a pna corresponding to a PNG with the same ID (balloons0.pna for balloons0.png), it can be used to set transparency.

  SSP also allows the alpha channel of the PNG itself to be used through [settings](../descript/balloon/descript-txt/use_self_alpha.md).

  This file is optional.

- **balloonk\*.png**: Speech balloons for the partner (or third and later characters).

  They are generally the same as balloons\*.png, but slightly shorter in height.

  This file is optional. If omitted, the corresponding ID from the main-side balloon is used.

- **balloonk\*.pna**: The balloonk\*.png version of balloons\*.pna. See the preceding description of balloons\*.pna.

- **balloonp\*def\*.png**: Speech balloons for the third and later characters. The balloon corresponding to `\p[2]` is balloonp2def0.png / balloonp2def1.png.

  This file is optional. If omitted, balloonk is used, or balloons if balloonk is also unavailable.

- **balloonp\*def\*.pna**: The balloonp\*def\*.png version of balloons\*.pna. See the preceding description of balloons\*.pna.

- **balloonc\*.png**: The balloon's input window.

  \* is a number from 0 to 3 (or 4 in SSP), and each file number corresponds to the following:

  - balloonc0.png　……　Send box
  - balloonc1.png　……　Communicate box
  - balloonc2.png　……　Teach box
  - balloonc3.png　……　Input box
  - balloonc4.png　……　Address Bar box (SSP only)
  - balloonc5.png　……　Multiline input (Textarea) box (SSP 2.9.10 and later. If absent, the balloon's main image is used)

- **balloonc\*.pna**: The input-box version of balloons\*.pna.

- **online\*.png**: Images displayed while receiving network information.

  The animation repeats in numerical order.

- **arrow\*.png**: Images used to scroll text.

  0 points upward, and 1 points downward.

  In SSP, separate images can be defined for the main character and partner. See below.

- **sstp.png**:

  - When displaying sender information and other details upon receiving SSTP
  - When executing the `\![*]` tag (also applies to %\* in SSP)

  The image displayed in these cases. In SSP, separate images can be configured for each use. See below.

- **thumbnail.png**: The thumbnail displayed when selecting a balloon from the menu tree.

  Supported image formats are PNG and JPG.

  Renaming a PNG to PNR makes the pixel at the top left of the image (coordinates 0,0) transparent wherever that color appears.

  This file is optional.

The following files are SSP-specific. All are optional.

- **ok_down.png/ok_up.png**: Images for the OK button in input-box controls.

- **cancel_down.png/cancel_up.png**: Images for the Cancel button in input-box controls.

- **mode_down.png/mode_up.png**: Images for the mode-switching button.

- **sstp_new.png / sstp_newk.png / sstp_newp\*def.png**: Images used to display sender information and other details upon receiving SSTP (unlike sstp.png, these images are dedicated to this purpose).

- **marker.png / markers.png / markerk.png / markerp\*def.png**: Images displayed by the `\![*]` tag (also applies to %\* in SSP; unlike sstp.png, these images are dedicated to this purpose).

  markers is for the main character (using marker instead is recommended for compatibility with older versions), markerk is for the partner, and markerp2def onward are for `\p[2]` and later.

- **arrows\*.png / arrowk\*.png / arrowp\*def.png**: Images used to scroll text. SSP 2.4.78 and later only.

  0 points upward, and 1 points downward.

  arrows is for the main character (using arrow instead is recommended for compatibility with older versions), arrowk is for the partner, and arrowp2def onward are for `\p[2]` and later.

- **clickwait.png / clickwaits\*.png / clickwaitk\*.png / clickwaitp\*def.png**: Images used to indicate a click wait (`\x`). SSP 2.5.54 and later only.

  clickwaits is for the main character, clickwaitk is for the partner, and clickwaitp2def onward are for `\p[2]` and later.
