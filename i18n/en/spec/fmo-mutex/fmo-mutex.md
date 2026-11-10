# Mutex for FMO

FMO itself has no mechanism for exclusive control, so a separate Mutex is held to prevent read/write conflicts.<br />
Its name is the FMO name + "FMO", for example:<br />
FMO = Sakura : Mutex = SakuraFMO<br />
FMO = SakuraUnicode : Mutex = SakuraUnicodeFMO<br />
It is important to determine whether the Mutex is in a signaled or non-signaled state.<br />
When reading or writing, always acquire ownership using WaitForSingleObject or an equivalent wait function, then release ownership with ReleaseMutex when finished.

Some older baseware may not support the Mutex for FMO, so failure to acquire the Mutex should not be treated as an error.<br />
In this case, however, consider the possibility of obtaining an FMO during an incomplete write, and take care to write code that processes it as safely as possible.

## Example code for reading and writing FMO (C++)

```
//ベースウェア等の保持すべきアプリは代わりにCreateMutexを使う
HANDLE hMutex = OpenMutex(MUTEX_ALL_ACCESS,FALSE,"SakuraFMO");

//FMO用Mutexに対応していないベースウェアもあるので、見つからなかったら単にスキップ
bool isWaitSuccess = true;

if ( hMutex ) {

    //INFINITEで待機すると永遠に待ち続けてGUIが止まるので適宜工夫すること
    DWORD result = WaitForSingleObject(hMutex,INFINITE);
    
    if ( result != WAIT_OBJECT_0 ) {
        isWaitSuccess = false;
    }
}

if ( isWaitSuccess ) {

    //保持すべきアプリは代わりにCreateMutexを使う
    HANDLE hFMO = OpenFileMapping(FILE_MAP_ALL_ACCESS,FALSE,"Sakura");

    if ( hFMO ) {

        char *pDataStart = static_cast<char*>(MapViewOfFile(hFMO,FILE_MAP_ALL_ACCESS,0,0,0));

        if ( pDataStart ) {

            //頭の4バイトはFMO最大サイズ。
            //文字列終端（C言語文字列のゼロ終端）とは異なるので注意。
            unsigned long length = *reinterpret_cast<unsigned long*>(pDataStart);

            char *pData = pDataStart;
            pData += 4;

            //****************************************
            //ここでpDataとlengthをつかってなにかやる
            //****************************************

            //MapViewOfFileの解除
            UnmapViewOfFile(pDataStart);
        }
            
        //FMOハンドルを開放
        //ベースウェア等の保持すべきアプリは開放せず持ち続けること
        CloseHandle(hFMO);
    }
}

if ( hMutex ) {
    if ( isWaitSuccess ) {
    
        //WaitForSingleObjectでMutexが非シグナル状態になるので、シグナル状態に戻す(Release)
        ReleaseMutex(hMutex);
    }

    //最後にMutexのハンドルも要らないので開放
    //ベースウェア等の保持すべきアプリは開放せず持ち続けること
    CloseHandle(hMutex);
}
```
