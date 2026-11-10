# 关于`\![move]`和`\![moveasync]`

新规格：（SSP 2.3.85及更高版本）

`\![move(async),--X=X座標,--Y=Y座標,--time=移動時間,--base=移動基準,--base-offset=基準とするキャラ基準位置,--move-offset=動かすキャラ基準位置,--option=オプション]`

所有参数均可省略，顺序也可以更改。指定名称不区分大小写（例如也可以写成--x=10）

旧规格：

`\![move(async),X座標,Y座標,移動時間,移動基準,基準とするキャラ基準位置,動かすキャラ基準位置]`

移动时间之后的参数均可省略。

*X坐标、Y坐标*指定目标坐标。<br />
也可以指定负值。<br />
省略其中一个坐标或指定为"fix"时，该坐标保持不变。<br />
省略时为"fix"

*移动时间*以毫秒为单位。<br />
省略移动时间或指定为0时，会立即移动。<br />
省略时为0

*基准位置*指定作为移动基准（相对坐标原点）的角色等。<br />
指定方法如下。<br />
省略时为screen

- **screen**: 以当前角色窗口所在显示器的左上角为原点的坐标。初始值
- **primaryscreen**: 以主显示器（ID=1）的左上角为原点的坐标。
- **ID**: 相对于指定为0、1等的ID号作用域（对应于`\0`、`\1`、`\p[2]`等数量）的角色的坐标
- **本体侧名/ID**: 相对于使用本体侧名称（sakura名、`\0`名）指定的其他ghost的ID号作用域角色的坐标
- **me**: 相对于移动角色自身的坐标
- **primaryscreen**: 以主显示器左上角为原点的坐标
- **global**: 系统坐标系（Windows中与primaryscreen相同）

*作为基准的角色基准位置*用于指定以角色或screen为移动基准时，哪个位置作为原点。<br />
以X基准.Y基准的形式指定，分别组合以下选项：<br />
X基准：left、right、base、center<br />
Y基准：top、bottom、base、center<br />
组合这4个选项并写成right.base等形式。<br />
其中，base遵循surfaces.txt中的point.basepos设置。<br />
省略时为left.top

基准指定为screen时，不能使用base；指定为global时，不能使用right、bottom、center。

*移动角色基准位置*的指定方法与作为基准的角色基准位置相同。

*选项*可以指定多次。指定方法如下。仅新规格的格式可以指定。

- **ignore-sticky-window**: 忽略通过`\![set,sticky-window]`设置的联动，单独移动
