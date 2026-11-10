# FMO 用 Mutex

FMO 本身沒有排他控制機制，因此會另外持有 Mutex，以避免讀寫衝突。<br />
名稱由 FMO 名稱加上 "FMO" 組成，例如：<br />
FMO = Sakura : Mutex = SakuraFMO<br />
FMO = SakuraUnicode : Mutex = SakuraUnicodeFMO<br />
此處判定是否處於訊號狀態非常重要。<br />
讀寫時，務必使用 WaitForSingleObject 或同等的等待函數取得所有權，完成後再使用 ReleaseMutex 釋放所有權。

舊版 baseware 等可能不支援 FMO 用 Mutex，因此即使取得 Mutex 失敗，也不要視為錯誤。<br />
但在這種情況下，請考慮到可能會取得仍在寫入中的不完整 FMO，並留意撰寫可盡可能安全處理的程式碼。

## 讀寫 FMO 的程式碼範例(C++)

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
