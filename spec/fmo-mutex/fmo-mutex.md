# FMO用Mutex

FMO自体に排他制御の仕組みはないため、書き込み・読み取りの衝突を避けるために、別途Mutexを保持しています。<br />
FMO名+"FMO"という名前になり、例えば以下のようになります。<br />
FMO = Sakura : Mutex = SakuraFMO<br />
FMO = SakuraUnicode : Mutex = SakuraUnicodeFMO<br />
こちらはシグナル状態・非シグナル状態の判定が重要になります。<br />
読み書きを行う際は、必ずWaitForSingleObjectや同等の待機関数を使い所有権を取得し、終わったらReleaseMutexで所有権を開放してください。

旧いベースウェア等でFMO用Mutexに対応していない場合があるので、Mutexの取得に失敗してもエラーにはしないでください。<br />
ただしこの場合は、不完全な書き込み中のFMOを取得する可能性を考慮して、できるだけ安全に処理できるコードを書くよう留意してください。

## FMOを読み書きするコード例(C++)

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
