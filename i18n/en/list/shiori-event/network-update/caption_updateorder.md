# Order of network update events

The order of events during a normal SSP network update (ghost update) is as follows.

1. OnUpdateProcessExec　※Only when run from a menu or similar. If a script is returned, the standard update process that follows is not performed.

2. OnUpdateBegin

3. OnUpdateReady　※Only if there are update files. If there are no update files, the following events are skipped and OnUpdateComplete (Reference0 is none) occurs.

4. Repeat the following for each update file.

   1. OnUpdate.OnDownloadBegin
   2. OnUpdate.OnMD5CompareBegin
   3. OnUpdate.OnMD5CompareComplete or OnUpdate.OnMD5CompareFailure<br />
      If the MD5 does not match, retry from OnUpdate.OnDownloadBegin for the same file. If the MD5 still does not match after the retry limit is exceeded, OnUpdateFailure (md5 miss) occurs and no subsequent files are processed.

5. After all files have been downloaded, the update files are replaced and SHIORI, the shell, and other components are reloaded. OnUpdateComplete then occurs. Therefore, OnUpdateComplete is received by the ghost after it has been reloaded.

- If the update fails partway through (including if it is interrupted), OnUpdateFailure occurs at that point and the process ends. OnUpdateFailure and OnUpdateComplete never both occur for the same update.
- After OnUpdateReady, after processing each file, and before replacing the files, the next step waits until playback of the scripts for all events that have occurred so far is complete. Therefore, if a script is returned for one of these events, the update does not proceed to the next stage until that script has finished playing.
- If the fast-forward key (the key specified by the SSP setting 「Enable fast-forward key」; Ctrl by default) is pressed when the script returned for OnUpdateReady finishes playing and file downloads begin, OnUpdate.OnDownloadBegin and OnUpdate.OnMD5Compare\* do not occur for any files in that update (the files are still downloaded and their MD5 values are still checked). OnUpdateBegin, OnUpdateReady, OnUpdateComplete, and OnUpdateFailure occur as usual.
- For automatic updates (where the update reason is auto), OnUpdateBegin occurs when the presence of update files is confirmed, immediately before OnUpdateReady. If there are no update files, or the update fails before the files are checked, none of OnUpdateBegin, OnUpdateComplete, or OnUpdateFailure occur.
- For update checks only (such as checks from the ghost explorer), OnUpdateBegin, OnUpdateReady, OnUpdate.OnDownloadBegin, OnUpdate.OnMD5Compare\*, OnUpdateComplete, and OnUpdateFailure do not occur. Instead, OnUpdateCheckComplete or OnUpdateCheckFailure occurs.
- For updates to items other than ghosts (such as shells and balloons), the event names above are replaced with OnUpdateOther~ (OnUpdateOtherBegin, OnUpdateOther.OnDownloadBegin, and so on). The order is the same.

When updating the ghost itself, its shell, and its balloon together, the sequence of events described above occurs separately for each, in the order ghost → shell → balloon (→ recommended balloon). After all updates are complete, OnUpdateResultEx occurs once, at the end. OnUpdateResult occurs immediately afterward only if OnUpdateResultEx did not return a script. For update checks only, these are OnUpdateCheckResultEx and OnUpdateCheckResult, respectively.
