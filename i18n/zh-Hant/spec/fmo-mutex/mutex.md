# Mutex

為表示 baseware 正在執行，SSP 會保留名為 "ssp" 的 Mutex，Materia 和 CROW 則會保留名為 "sakura" 的 Mutex。<br />
確認這個具名 Mutex 是否存在，即可用低廉的成本判定是否正在執行。<br />
Mutex 本身的狀態並未定義，因此不需要確認是否為訊號狀態。

## 僅確認是否存在的程式碼範例（C++）

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
