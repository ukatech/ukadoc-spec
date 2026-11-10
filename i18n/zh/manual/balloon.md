# balloon

balloon 文件夹中的文件如下。

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

- **[descript.txt](../descript/balloon/index.md)**: 用于识别 balloon 的文件。

  与 ghost 或 shell 的 descript.txt 相比，记录项也更多。

  详情请参阅[链接目标](../descript/balloon/index.md)。

- **[balloons\*s.txt/balloonk\*s.txt/balloonc\*s.txt](../descript/balloon/balloonsoption/index.md)**: 用于单独设置各 balloon 的文件。

  为对应 ID 的 surface（例如 balloons1.png 对应 balloons1s.txt）准备此文件后，其中的设置将覆盖 descript.txt 中对该 surface 的设置。

  用于只想更改特定 ID 的 surface 设置等场景。

  ※请注意文件名中的 s（不是 balloons\*.txt，而是 balloons\**s*.txt）

  现在也可用于输入框。请使用 balloonc\*s.txt 指定。

  详情请参阅[链接目标](../descript/balloon/balloonsoption/index.md)。

- **readme.txt**: 供 balloon 作者填写发布来源等信息的文件。

  可以省略，但准备该文件后，可在安装时或通过 baseware 的菜单等位置查看。

- **balloons\*.png**: 本体侧的对话框。

  \* 是作为 balloon surface ID 的数字。

  偶数 ID 表示朝左的 balloon，奇数 ID 表示朝右的 balloon，两者成对使用。

  一般采用以下分配方式，但也可以自由安排。可以按 4-5、6-7 等继续添加成对的 ID，也可以只使用 0-1。

  - balloons0.png　以及　balloons1.png　……　普通对话框（左・右）
  - balloons2.png　以及　balloons3.png　……　纵向较长的对话框（左・右）

- **balloons\*.pna**: MATERIA 不支持。

  将灰度（黑：透明←→不透明：白）png 图像的扩展名改为 pna。

  如果为对应 ID 的 png（例如 balloons0.png）准备对应的 pna，即可将其用作透明度设置。

  SSP 也可以通过[设置](../descript/balloon/descript-txt/use_self_alpha.md)使用 png 图像本身的 alpha 通道。

  此文件可以省略。

- **balloonk\*.png**: 搭档侧（或第三人及之后角色）的对话框。

  基本上与 balloons\*.png 相同，但通常高度略小。

  此文件可以省略。省略时会使用本体侧对应 ID 的文件。

- **balloonk\*.pna**: balloons\*.pna 的 balloonk\*.png 版本。说明请参阅前述 balloons\*.pna。

- **balloonp\*def\*.png**: 第三人及之后角色的对话框。对应于 `\p[2]` 的 balloon 是 balloonp2def0.png / balloonp2def1.png。

  此文件可以省略。省略时会使用 balloonk；若也没有，则使用 balloons。

- **balloonp\*def\*.pna**: balloons\*.pna 的 balloonp\*def\*.png 版本。说明请参阅前述 balloons\*.pna。

- **balloonc\*.png**: balloon 的输入窗口。

  \* 中填入 0 到 3（SSP 中为 4）的数字，各编号文件对应如下。

  - balloonc0.png　……　Send 框
  - balloonc1.png　……　Communicate 框
  - balloonc2.png　……　Teach 框
  - balloonc3.png　……　Input 框
  - balloonc4.png　……　Address Bar 框（仅限 SSP）
  - balloonc5.png　……　多行输入（Textarea）框（SSP 2.9.10 及以后。若不存在，则使用 balloon 本体图像）

- **balloonc\*.pna**: balloons\*.pna 的输入框版本。

- **online\*.png**: 网络信息接收过程中显示的图像。

  按编号顺序重复播放动画。

- **arrow\*.png**: 用于滚动文本的图像。

  0 表示向上，1 表示向下。

  SSP 中可以定义本体和搭档专用的图像。详见后文。

- **sstp.png**:

  - 收到 SSTP 时，用于显示发送者信息等
  - 执行 `\![*]` 标签时（SSP 中执行 %\* 也相同）

  显示的图像。SSP 中可以分别设置专用图像。详见后文。

- **thumbnail.png**: 在菜单树中选择 balloon 时显示的缩略图。

  可使用的图像格式为 png 或 jpg。

  将 png 重命名为 pnr 后，会将图像左上角的 1 个像素（坐标 0,0）设置为透明色。

  此文件可以省略。

以下为 SSP 专用文件。均可省略。

- **ok_down.png/ok_up.png**: 输入框类 OK 按钮的图像。

- **cancel_down.png/cancel_up.png**: 输入框类取消按钮的图像。

- **mode_down.png/mode_up.png**: 模式切换按钮的图像。

- **sstp_new.png / sstp_newk.png / sstp_newp\*def.png**: 收到 SSTP 时用于显示发送者信息等的图像（与 sstp.png 不同，此图像仅用于此用途）。

- **marker.png / markers.png / markerk.png / markerp\*def.png**: 通过 `\![*]` 标签显示的图像（与 sstp.png 不同，此图像仅用于此用途）。

  markers 用于本体（为兼容旧版本，建议用 marker 代替），markerk 用于搭档，markerp2def 及之后的文件用于 `\p[2]` 及之后的角色。

- **arrows\*.png / arrowk\*.png / arrowp\*def.png**: 用于滚动文本的图像。仅限 SSP 2.4.78 及以后版本。

  0 表示向上，1 表示向下。

  arrows 用于本体（为兼容旧版本，建议用 arrow 代替），arrowk 用于搭档，arrowp2def 及之后的文件用于 `\p[2]` 及之后的角色。

- **clickwait.png / clickwaits\*.png / clickwaitk\*.png / clickwaitp\*def.png**: 用于表示等待点击（`\x`）的图像。仅限 SSP 2.5.54 及以后版本。

  clickwaits 用于本体，clickwaitk 用于搭档，clickwaitp2def 及之后的文件用于 `\p[2]` 及之后的角色。
