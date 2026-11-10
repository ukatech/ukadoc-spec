# 异步调用

内置模块（名称以`internal_`开头）中的函数添加选项`--async=标识符`后会以异步方式运行。接受请求后，会立即返回204响应，结果稍后会通过事件发送给调用方的ghost。<br />
不适用于没有ghost的调用（400 `ghost required`）。标识符为空时会返回400（`invalid parameter`）。<br />
对于耗时较长的处理（大型文件的哈希、密码哈希、密钥派生、生成RSA密钥对等），请使用`--async`。<br />
SSP中同时运行的异步调用数量最多为CPU核心数（2～4）。超出数量的调用会排队，直到前面的调用完成。

## 传递结果的事件

- **事件名**: 如果标识符以`On`开头（区分大小写），成功时使用该名称，失败时使用“标识符＋`Failure`”。请避免将已有事件名称（如`OnBoot`）用作标识符，否则结果会作为该事件送达。<br />
  否则，成功时为[OnInternalSaoriComplete](../../list/shiori-event/other/OnInternalSaoriComplete.md)，失败时为[OnInternalSaoriFailure](../../list/shiori-event/other/OnInternalSaoriFailure.md)。
- **成功时的Reference**: Reference0＝标识符，Reference1＝结果（与同步调用的`Result`相同），Reference2＝模块名，Reference3＝函数名，Reference4及之后＝`Value0`及之后。
- **失败时的Reference**: Reference0＝标识符，Reference1＝失败原因（与同步调用的`ErrorDescription`字符串相同），Reference2＝模块名，Reference3＝函数名。

参数数量或选项名称有误时，会在受理请求时返回400。参数内容有误（例如无法读取的十六进制数据）时，会通过失败事件送达。

## 结果送达的条件与顺序

- 只要调用方的ghost未处于结束过程中，结果就一定会送达。即使ghost处于时间临界状态、被动模式或引导模式，结果也会送达（即使已转存到缓存中，只要SHIORI仍处于加载状态，就会送达）。\[SSP 2.9.27\] 在此版本之前，处理在这些状态期间结束时，结果可能不会送达。
- SHIORI正在处理其他请求时，会等该请求处理完成后再送达。
- 如果调用方的ghost在结果送达前结束（包括重新加载SHIORI），结果将不会送达。
- 多个异步调用的结果送达顺序不一定与调用顺序一致（结果按处理完成顺序送达；超过并发数量而等待的调用，会按空出执行位置的顺序启动）。如果需要保证顺序，请通过标识符对应结果，或等前一个结果送达后再发起下一个调用。
