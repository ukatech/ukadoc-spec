# 网络更新事件的发生顺序

SSP进行常规网络更新（ghost 更新）时，事件的发生顺序如下。

1. OnUpdateProcessExec　※仅在从菜单等位置执行时发生。如果返回脚本，则不会执行后续的标准更新处理。

2. OnUpdateBegin

3. OnUpdateReady　※仅在存在更新文件时发生。如果没有更新文件，则跳过后续事件，并发生 OnUpdateComplete（Reference0 为 none）。

4. 对每个更新文件重复以下处理。

   1. OnUpdate.OnDownloadBegin
   2. OnUpdate.OnMD5CompareBegin
   3. OnUpdate.OnMD5CompareComplete 或 OnUpdate.OnMD5CompareFailure<br />
      如果 MD5 不匹配，则对同一文件从 OnUpdate.OnDownloadBegin 重新开始。如果超过重试次数后仍不匹配，则发生 OnUpdateFailure（md5 miss），后续文件不再处理。

5. 获取所有文件后，替换更新文件并重新加载 SHIORI、shell 等，然后发生 OnUpdateComplete。因此，接收 OnUpdateComplete 的是重新加载后的 ghost。

- 如果中途失败（包括中断），则会立即发生 OnUpdateFailure 并结束。同一次更新不会同时发生 OnUpdateFailure 和 OnUpdateComplete。
- OnUpdateReady、每个文件处理之后以及替换之前，都会等待此前发生的事件脚本播放结束后再继续。因此，如果这些事件返回脚本，更新会一直等到脚本播放结束才进入下一阶段。
- OnUpdateReady 的脚本播放结束、开始获取文件时，如果按住了快进键（在 SSP 设置的“启用快进键”中指定的按键，默认为 Ctrl），则本次更新的所有文件都不会发生 OnUpdate.OnDownloadBegin 和 OnUpdate.OnMD5Compare\*（但仍会获取文件并执行 MD5 校验）。OnUpdateBegin、OnUpdateReady、OnUpdateComplete 和 OnUpdateFailure 仍会照常发生。
- 自动更新（更新原因为 auto）时，OnUpdateBegin 会在确认存在更新文件时发生，也就是紧接在 OnUpdateReady 之前。如果没有更新文件，或在确认更新文件之前发生失败，则 OnUpdateBegin、OnUpdateComplete 和 OnUpdateFailure 均不会发生。
- 仅检查更新（从 ghost 浏览器等位置进行检查）时，不会发生 OnUpdateBegin、OnUpdateReady、OnUpdate.OnDownloadBegin、OnUpdate.OnMD5Compare\*、OnUpdateComplete 和 OnUpdateFailure，而会改为发生 OnUpdateCheckComplete 或 OnUpdateCheckFailure。
- 更新 ghost 以外的项目（例如 shell、balloon）时，上述事件名会替换为 OnUpdateOther〜（例如 OnUpdateOtherBegin、OnUpdateOther.OnDownloadBegin）。发生顺序相同。

同时更新 ghost 本体、shell 和 balloon 时，会依次对 ghost → shell → balloon（→ 推荐 balloon）执行上述一系列事件。所有更新结束后，最后只发生一次 OnUpdateResultEx。只有在 OnUpdateResultEx 未返回脚本时，才会接着发生 OnUpdateResult。仅检查更新时，对应事件为 OnUpdateCheckResultEx 和 OnUpdateCheckResult。
