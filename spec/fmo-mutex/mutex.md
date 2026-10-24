# Mutex

ベースウェアが起動中であることを示すため、SSPは"ssp"、MateriaとCROWは"sakura"という名前のMutexを保持しています。<br />
この名前つきMutexの存在を確認することで、起動中かどうかをローコストに判定できます。<br />
Mutex自体の状態は決められておらず、シグナル状態か否かの確認は不要です。

## 存在確認のみのコード例(C++)

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
