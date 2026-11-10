# 转译器

在 ghost 中，转译器称为 MAKOTO。

它既可以放置在 ghost 一侧，也可以放置在 shell 一侧（CROW 仅支持放置在 ghost 一侧）。

要在 ghost 一侧使用，必须在 master 目录下直接放置`makoto.dll`。

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-makoto.dll
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　:
　　　　　　:
```

要在 shell 一侧使用，必须在各 shell 文件夹的根目录下放置 makoto.dll。

```filetree
+-(myghost)
　　+-shell
　　　　+-master(またはadditional_shell)
　　　　　　+-makoto.dll
　　　　　　+-descript.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-surfaces.txt
　　　　　　:
　　　　　　:
```

它是一种作为过滤器，对 SHIORI 创建的脚本进行字符串替换的机制。

如果 ghost 一侧和 shell 一侧都配置了转译器，则先执行 ghost 一侧的转译，然后再执行 shell 一侧的转译。

转译发生在内容即将显示在 balloon 上时。

与 SHIORI 一样，可作为 MAKOTO 使用的文件有很多，详细用法需要参阅各自的文档。

过去，在没有 SHIORI 的时代，人们曾用它来改变对话内容；如今，这类职责主要由 SHIORI 承担。

现在有时会利用它实现根据 shell 改变说话语气等效果。

也可以通过 SHIORI Event 的 OnTranslate 进行转译（也就是说，SHIORI 兼任 ghost 一侧的 MAKOTO）。

如果同时使用 MAKOTO 和 SHIORI 进行转译，处理顺序为 SHIORI→MAKOTO。
