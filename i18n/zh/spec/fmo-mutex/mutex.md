# Mutex

为表示baseware正在运行，SSP会持有名为"ssp"的Mutex，Materia和CROW则会持有名为"sakura"的Mutex。<br />
通过确认这个命名Mutex是否存在，即可低开销地判断baseware是否正在运行。<br />
Mutex本身的状态没有规定，无需检查它是否处于有信号状态。

## 仅检查是否存在的代码示例(C++)

```
HANDLE hmutex = OpenMutex(MUTEX_ALL_ACCESS,FALSE,"ssp");
if ( hmutex ) {
  // いる
  CloseHandle(hmutex);
}
else {
  //いない
}
```
