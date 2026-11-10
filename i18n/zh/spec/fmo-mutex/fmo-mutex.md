# FMO 用 Mutex

FMO 本身没有排他控制机制，因此需要另外持有 Mutex，以避免读写冲突。<br />
Mutex 的名称为 FMO 名称+"FMO"，例如：<br />
FMO = Sakura : Mutex = SakuraFMO<br />
FMO = SakuraUnicode : Mutex = SakuraUnicodeFMO<br />
这里需要正确判断信号状态和非信号状态。<br />
读写时，务必使用 WaitForSingleObject 或同等的等待函数获取所有权，完成后使用 ReleaseMutex 释放所有权。

较旧的 baseware 等可能不支持 FMO 用 Mutex，因此即使获取 Mutex 失败，也不要视为错误。<br />
不过，此时应考虑到可能获取到正在进行不完整写入的 FMO，并注意编写尽可能安全的处理代码。

## FMO 读写代码示例（C++）

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
