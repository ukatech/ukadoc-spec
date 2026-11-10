# Mutex

To indicate that the baseware is running, SSP holds a Mutex named "ssp", while Materia and CROW hold one named "sakura".<br />
You can determine whether they are running at low cost by checking whether this named Mutex exists.<br />
The state of the Mutex itself is unspecified, so there is no need to check whether it is signaled.

## Code example that only checks for existence (C++)

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
