# 關於 `\![move]`、`\![moveasync]`

新規規格：（SSP 2.3.85 以後）

`\![move(async),--X=X座標,--Y=Y座標,--time=移動時間,--base=移動基準,--base-offset=基準とするキャラ基準位置,--move-offset=動かすキャラ基準位置,--option=オプション]`

所有項目皆可省略，順序也可以變更。指定名稱不區分大小寫（例如也可以寫成 --x=10）。

舊規格：

`\![move(async),X座標,Y座標,移動時間,移動基準,基準とするキャラ基準位置,動かすキャラ基準位置]`

移動時間之後的項目皆可省略。

*X 座標、Y 座標*指定目標座標。<br />
也可以指定負值。<br />
省略任一座標或指定為 "fix" 時，會保留該座標。<br />
省略時為 "fix"。

*移動時間*的單位為毫秒。<br />
省略移動時間或指定為 0 時，會立即移動。<br />
省略時為 0。

*基準位置*是作為移動基準（相對座標原點）的角色等。<br />
指定方法如下。<br />
省略時為 screen。

- **screen**：以目前角色視窗所在螢幕的左上角為原點的座標。初始值。
- **primaryscreen**：以主螢幕（ID=1）的左上角為原點的座標。
- **ID**：與指定為 0、1 等 ID 的 scope（相當於 `\0`、`\1`、`\p[2]` 等數值）的角色之相對座標。
- **本體側名稱/ID**：與以本體側名稱（sakura 名稱、`\0` 名稱）指定的其他 ghost 之 ID scope 角色的相對座標。
- **me**：與移動中的角色本身的相對座標。
- **primaryscreen**：以主螢幕左上角為原點的座標。
- **global**：系統座標系（在 Windows 中與 primaryscreen 相同）。

*基準角色基準位置*是在移動基準指定角色或 screen 時，指定以哪個位置為原點。<br />
以 X 基準.Y 基準的形式指定，分別組合以下 4 種指定值：<br />
X 基準：left、right、base、center<br />
Y 基準：top、bottom、base、center<br />
組合後以 right.base 等形式記述。<br />
其中，base 依照 surfaces.txt 中的 point.basepos 指定。<br />
省略時為 left.top。

指定 screen 時不能使用 base；指定 global 時不能使用 right、bottom、center。

*移動角色基準位置*的指定方式與基準角色基準位置相同。

*選項*可以指定多次。指定方法如下。僅能使用新規格式。

- **ignore-sticky-window**：忽略 `\![set,sticky-window]` 的連動設定，單獨移動
