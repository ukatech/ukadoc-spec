# 动画间隔

## 概要

在[animation\*.interval](../animation-star-.interval.md)中指定动画运行的周期和时机（触发器）。

## 组合指定（SSP扩展功能）

在SSP中，可以用「+」分隔列出多个动画间隔，从而组合指定多个条件。此规范原本预期用于bind，因此即使不带bind时看起来能正常运行，也要谨慎使用。

以下是组合指定的示例。

- **bind+always**: dressup启用时，始终执行的动画。
- **bind+runonce**: dressup启用时，切换到定义了该dressup的surface时，或在显示该surface时启用该dressup时，仅执行一次的动画。
- **bind+random,频度**: dressup启用时，每秒以1/频度的概率触发的动画。
- **bind+periodic,间隔**: dressup启用时，每隔（间隔）秒触发的动画。
- **bind+runonce+random,5**: dressup启用时，切换到定义了该dressup的surface时，或在显示该surface时启用该dressup时，先执行一次，之后每秒以五分之一的概率播放的动画。

对bind使用「+」分隔符组合指定其他条件时，bind间隔原有的特性会失效，例如「忽略pattern定义的权重参数，并与基础surface合为一体作为静止图像」。

此外，对于random、periodic、talk等需要参数的指定，即使是组合指定，参数也要写在末尾。

以下是*错误*示例。

```
animation0.interval,random,5+bind
```

以下是*正确*示例。

```
animation1.interval,bind+random,5
```

不允许组合带参数的间隔指定。
