# 补充：什么是 SHIORI Event

## 关于本页

本页概述「SHIORI Event」。

以下内容并非 SHIORI/3.0 的正式规范*，而只是帮助理解其概念的粗略指南。

关于各个 SHIORI Event 的说明，请参阅「[SHIORI Event](../list/shiori-event/index.md)」页面中的列表。

## 目次

- [什么是 SHIORI Event（栞事件）](shiori-event.md#shiori-event栞イベントとは)
- [Reference（参考信息）](shiori-event.md#referenceリファレンス)
- [GET 命令和 NOTIFY 命令](shiori-event.md#getコマンドとnotifyコマンド)

## 什么是 SHIORI Event（栞事件）

[![ghost 会随着 baseware 与 ghost（SHIORI）的交互而运行](../assets/image/shiori-event.jpg)](../assets/image/shiori-event.jpg)

*从启动到 ghost 开始运行*

所谓 ghost 运行（说话、改变表情等），究竟是怎么回事呢？

粗略地说，这是由*baseware*（MATERIA、CROW、SSP 等）与*SHIORI*（作为 ghost 核心的组件）协同实现的功能。

SHIORI Event 是帮助理解这一过程的关键术语，它说明了 baseware 和 SHIORI 各自承担什么职责。

在 ghost 的运行过程中，最先发挥作用的是 baseware。

baseware 首要承担的一项重要工作，是创造*ghost 说话或行动的时机*。

baseware 会监视时间、鼠标输入等各种状态，并在发生特定变化时（例如经过 1 秒或 1 分钟，或者鼠标光标碰到 ghost）向 ghost（其核心 SHIORI）发送通知。

这种通知称为*SHIORI Event*。

而 SHIORI 的工作从这里开始。SHIORI 收到 SHIORI Event 后，会利用称为自身词典的文件内容等，*生成 ghost 的动作指令*（这种动作指令称为 Sakura Script）。

然后，SHIORI 将动作指令*发送回 baseware*。baseware 收到后，会读取动作指令的内容，并呈现 ghost 的动作。

通过这种方式，每当发生 SHIORI Event，ghost 就会在用户的显示器中实际运行。

反过来说，*SHIORI 在收到 SHIORI Event 之前无法让 ghost 运行*。原则上，所有 ghost 动作都在 SHIORI Event 中执行，并且是被动发生的。

即使看起来并非如此，也请注意，许多 ghost 都具备的「随机对话」「AI 对话」功能，在许多 SHIORI 中是通过处理每秒发出的 [OnSecondChange](../list/shiori-event/time/OnSecondChange.md) 来实现的（这一点完全取决于各个 SHIORI 的实现，详细信息需要参阅相应 SHIORI 的文档）。

## Reference（参考信息）

许多 SHIORI Event 会在通知 SHIORI Event 的 ID（名称、类型）的同时，以*Reference*的形式通知相关信息。

例如，ghost 被点击时发出的 ID [OnMouseClick](../list/shiori-event/mouse/OnMouseClick.md)，会通过 Reference 通知点击的是哪个 scope（主体一侧、搭档一侧、第三个角色……）、点击了该 scope 的哪个命中区域，以及使用哪个按钮（右键、左键、滚轮……）点击等信息。

例如，SHIORI 可以利用 Reference 来改变 ghost 的动作。

以 OnMouseClick 为例，许多 ghost 会根据点击了哪个 scope 的哪个部位，改变执行的功能或对话。

*所有 Reference 都会获得从 0 开始的连续编号*，同一 ID 的 SHIORI Event 所带的 Reference，基本上*始终由相同编号对应相同内容*。

查看 [SHIORI Event 列表页面](../list/shiori-event/index.md)中各个 ID 条目下随 ID 一同通知的 Reference 列表，或许就能更容易理解这一点。

不过，有些 ID 的 Reference 数量并不固定。

例如，在 SHIORI Event 列表页面查看名为 [installedghostname](../list/shiori-event/notify/installedghostname.md) 的 SHIORI Event 的 Reference 时，会看到编号没有明确写出，而是以「Reference*」这样的形式表示。

installedghostname 会在启动后立即等时机发生，并告知所有安装在该 baseware 中的 ghost 名称。用户安装的 ghost 数量自然各不相同，因此 Reference 的数量也不固定。

即使 Reference 的总数不固定，所有 Reference 都以从 0 开始的连续编号表示这一原则仍然不变。

## GET 命令和 NOTIFY 命令

[![所有 SHIORI Event 都会以两种封装形式之一送达 SHIORI：一种是附有回邮信封的「GET 命令」，另一种是不附回邮信封的「NOTIFY 命令」。](../assets/image/shiori-command.png)](../assets/image/shiori-command.png)

*如果把 SHIORI Event 比作邮件……*

实际上，所有 SHIORI Event 不仅有各种不同的 ID，其发出方式和目的也分为两种。

其中一种就是前面提到的，作为 ghost 运行时机而发出的 SHIORI Event。

这称为*GET 命令*，顾名思义，是为了让 baseware 从 SHIORI 接收动作指令（Sakura Script）等内容（get）而发出的 SHIORI Event。

另一种是稍有不同的*NOTIFY 命令*。对于通过 NOTIFY 命令发出的 SHIORI Event，ghost 无法运行。

这是因为即使 SHIORI 针对 NOTIFY 命令的 SHIORI Event 返回了某种动作指令，baseware 也会忽略它。

NOTIFY 命令的目的是向 SHIORI 通知（notify）信息（Reference）。

SHIORI 可以利用收到的信息，为之后 ghost 的运行提供帮助，而不一定要在收到该 SHIORI Event 时使用这些信息。

前面提到的 [installedghostname](../list/shiori-event/notify/installedghostname.md)，就是通过 NOTIFY 命令发出的典型 ID。SHIORI 可以通过其 Reference 了解用户环境中安装了哪些 ghost。ghost 可以根据这些信息实现诸如「如果安装了特定 ghost，就在菜单中显示用于呼叫该 ghost 的项目」这样的功能。

需要注意的是，两种命令的存在*并不意味着*所有 SHIORI Event ID 被分成两个「组」。

这是因为原则上*所有 ID 的 SHIORI Event 都有可能通过 NOTIFY 或 GET 发出*。命令类型与 ID 类型彼此独立，本质上不存在依赖关系（不过，观察实际实现时可以发现一些倾向和规律。详情请参阅 [SHIORI Event 列表页面](../list/shiori-event/index.md)中的各个条目）。
