# Mutex

To indicate that baseware is running, SSP maintains a Mutex named "ssp", while Materia and CROW maintain one named "sakura".<br />
You can determine whether they are running at low cost by checking for the existence of this named Mutex.<br />
The state of the Mutex itself is unspecified, so there is no need to check whether it is signaled.

## Code example checking only for existence (C++)

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
