# Method: EXECUTE

The EXECUTE method can retrieve various ghost information and execute commands without using Sakura Script.<br />
The ghost does not speak when this method is executed, but its internal state may change.

## EXECUTE sample

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## Request-specific headers

- **Command or Command\[param1,param2...\]**: The command to execute. The operations and returned information are described below.<br />
  The square brackets and their contents specify parameters to pass to the command.
- **Reference\* \[SSP\]**: Parameters can also be specified in Reference0 and subsequent headers instead of using square brackets.

See below for the strings that can be specified in the Command header and the results returned in the response's "additional data".

## Commands for the Command header and returned additional data

- **GetName**: The running ghost's (`\0` name),(`\1` name), separated by a comma.
- **GetNames \[SSP\]**: A list of currently installed `\0` names, separated by newlines and terminated by a blank line.
- **GetFMO \[SSP 2.5.57\] \[remote restrictions apply\]**: Retrieves information equivalent to the contents of [FMO](../fmo-mutex/index.md).<br />
  However, it is limited to the data managed within the application communicating via SSTP, unlike the actual FMO shared by concurrently running applications.<br />
  It is mainly used by console applications and similar programs that have no window and cannot send Direct SSTP, to use the ReceiverGhostHWnd header over Socket SSTP alone and achieve functionality equivalent to Direct SSTP.<br />
  Entries are separated by newlines and terminated by a blank line.<br />
  For remote requests, path information is omitted, and the headers and hwnd are replaced with dummy values.
- **GetGhostName \[SSP\]**: The name of the running ghost itself (name in descript.txt).
- **GetShellName \[SSP\]**: The name of the shell currently used by the running ghost.
- **GetBalloonName \[SSP\]**: The name of the balloon currently used by the running ghost.
- **GetVersion**: The version of the baseware (the running software).
- **GetGhostNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all ghosts recognized by SSP.
- **GetShellNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all shells recognized by the running ghost.
- **GetBalloonNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all balloons recognized by SSP.
- **GetHeadlineNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all headlines recognized by SSP.
- **GetPluginNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all plugins recognized by SSP.
- **GetGhostUUIDList \[SSP 2.9.35\]**: A newline-separated list of the [UUID](../../list/propertysystem/property-system/general-property/uuid.md) values of all ghosts recognized by SSP, in the same order as GetGhostNameList.<br />
  **GetBalloonUUIDList \[SSP 2.9.35\]**: The UUID values of all balloons, in the same order as GetBalloonNameList.<br />
  **GetShellUUIDList \[SSP 2.9.35\]**: The UUID values of all shells recognized by the running ghost, in the same order as GetShellNameList.<br />
  UUID values are calculated from values in descript.txt using the [metainfo-standard](https://github.com/ukatech/metainfo-standard) procedure (the same as `uuid` in the property system).
- **GetGhostMetaInfoList \[SSP 2.9.35\]**: A newline-separated list of metainfo folder URLs for all ghosts recognized by SSP, in the same order as GetGhostNameList.<br />
  **GetBalloonMetaInfoList \[SSP 2.9.35\]**: The metainfo folder URLs for all balloons, in the same order as GetBalloonNameList.<br />
  **GetShellMetaInfoList \[SSP 2.9.35\]**: The metainfo folder URLs for all shells recognized by the running ghost, in the same order as GetShellNameList.<br />
  These are the [metainfo](../../descript/ghost/descript-txt/metainfo.md) values in descript.txt, or URLs derived from [githubrepo](../../descript/ghost/descript-txt/githubrepo.md) if absent (assuming `master` as the default branch). Entries with neither are blank lines.
- **GetShortVersion \[SSP 2.6.53\]**: The version of the baseware (the running software), consisting only of the period-separated version number.<br />
  A simple comparison with ssp.full.version in [version.json](https://ssp.shillest.net/archive/version.json), for example, can determine whether it is the latest version.
- **GetStatus \[SSP 2.8.94\]**: The current execution state of the running ghost. The contents are the same as the Status header of a SHIORI/3.0 request and [currentghost.status](../../list/propertysystem/property-system/currentghost.status.md) in the property system.<br />
  If multiple states apply, they are separated by commas. See [SHIORI Status header](../../list/propertysystem/property-system/currentghost.status.md) for the meaning of each value.<br />
  If no state applies, there is no additional data (status code 200).<br />
  \[SSP 2.9.39\] GetStatus in EXECUTE also includes `scriptbusy` (a script is waiting to play or is playing). `talking` disappears between queued scripts and between accepting a script and starting playback, but `scriptbusy` remains. The SEND response is returned after the script is queued, so it is always visible if read immediately afterward. It is not added to the Status header of a SHIORI/3.0 request or to `currentghost.status`, so as not to change ghost-side checks.
- **SetTimeShift \[SSP 2.9.39\] \[not available remotely\]**: Sets the offset for "virtual modification of the current time" (time machine) synchronously, without going through the ghost's script. This is for testing ghosts that depend on the date or time.<br />
  Parameter 0: The offset. The format is the same as the value of [`\![timemachine,set,値]`](../../list/sakura-script/misc/bang-timemachine-set-value.md) (`+秒` / `-秒` / `0` / an ISO8601 date and time). This sets the offset to the specified value rather than adding it to the current offset.<br />
  Accepted only when SSP is started with `--allow-timemachine-control`. Otherwise, it does nothing, fails with 420, and records a warning in the error log. It cannot be executed remotely (420). If the value is omitted or cannot be parsed, it fails with 400 and leaves the offset unchanged.<br />
  On success, the resulting offset in seconds as a signed integer is returned as additional data (status code 200). The offset is already applied when the response is received, and the property `system.os.timeshift` also returns that value. The offset lasts only for the current session and is not saved in settings.
- **Quiet \[not available remotely\]**: Remains silent until Restore is executed or 16 seconds have passed. No additional data (success with a 200-series status code).
- **Restore**: Cancels Quiet. No additional data (success with a 200-series status code).
- **CompressArchive \[SSP 2.7.23\] \[not available remotely\]**: Compresses the files in the specified folder into a ZIP file. If the destination extension is `.7z`, the format is 7z; otherwise, it is ZIP (even if `.lzh` or `.cab` is specified, the contents are ZIP). Hidden files and folders are not included.<br />
  Parameter 0: Archive file name (specify a full path; relative paths are not allowed).<br />
  Parameter 1: Full path of the folder to compress.<br />
  Parameter 2 onward: Options (optional).<br />
  The options are as follows.<br />
  --event=event identifier: If an event identifier is specified, compression continues after the response and an event occurs when it finishes. If the identifier starts with On, an event with that identifier occurs; otherwise, OnCompressArchiveComplete or OnCompressArchiveFailure occurs. If omitted, the response is not returned until processing is complete.<br />
  --password=password: Enables AES-encrypted ZIP using the specified password.<br />
  See [OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md) and [OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md) for the events after execution.<br />
  \[SSP 2.9.25\] From SAORI over DirectSSTP, this can also be called via [CompressArchive in internal_file](../saori-ex/internal_file/internal_file.CompressArchive.md) (relative paths and `/` separators can also be used).<br />
  \[SSP 2.9.33\] If parameter 1 is not a folder (for example, a file path), it fails with 400 without compressing anything. If `--event=` is specified, a failure event (OnCompressArchiveFailure or the identifier with `Failure` appended) occurs with `invalid parameter`. Previously, passing a file path caused compression to fail with `file not found`.<br />
  For security reasons, the compression destination is restricted to locations within folders managed by SSP (locations specified in the "Folder" settings, such as the ghost and balloon folders).<br />
  This restriction may be tightened as needed, so it is advisable to limit the destination to the folder containing the ghost's own data or its subfolders.<br />
  No additional data (success with a 200-series status code).
- **ExtractArchive \[SSP 2.7.23\] \[not available remotely\]**: Extracts the specified archive. In addition to ZIP, it can extract formats such as 7z and tar (see [ExtractArchive in internal_file](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式) for supported formats).<br />
  Parameter 0: Archive file name (specify a full path; relative paths are not allowed).<br />
  Parameter 1: Full path of the destination folder.<br />
  Parameter 2 onward: Options (optional).<br />
  The options are as follows.<br />
  --event=event identifier: If an event identifier is specified, extraction continues after the response and an event occurs when it finishes. If the identifier starts with On, an event with that identifier occurs; otherwise, OnExtractArchiveComplete or OnExtractArchiveFailure occurs. If omitted, the response is not returned until processing is complete.<br />
  --password=password: Extracts using the specified password. \[SSP 2.9.26\] No password input dialog is shown. If a password is required but missing or incorrect, extraction fails without a dialog (the response is 500, and if an event is specified, the event is the identifier plus Failure or [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)). In \[SSP 2.9.25\] and earlier, this option was ignored and a dialog was shown.<br />
  \[SSP 2.9.26\] Even if an absolute destination path containing `..` is specified, it is rejected if the resolved path is outside SSP-managed folders (previously, extraction outside managed folders was possible).<br />
  See [OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md) and [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md) for the events after execution.<br />
  \[SSP 2.9.25\] From SAORI over DirectSSTP, this can also be called via [ExtractArchive in internal_file](../saori-ex/internal_file/internal_file.ExtractArchive.md) (relative paths and `/` separators can also be used).<br />
  For security reasons, the extraction destination is restricted to locations within folders managed by SSP (locations specified in the "Folder" settings, such as the ghost and balloon folders).<br />
  This restriction may be tightened as needed, so it is advisable to limit the destination to the folder containing the ghost's own data or its subfolders.<br />
  No additional data (success with a 200-series status code).
- **DumpSurface \[SSP 2.5.98\] \[not available remotely\]**: Outputs composited surface images to the specified directory. The parameters are the same as for [`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md).<br />
  However, an event ID cannot be specified. Specify the directory, scope ID, surface list, prefix, zero-position cropping, and animation ID \[SSP 2.9.05\], in that order.<br />
  \[SSP 2.9.08\] As with the Sakura Script version, parameters can also be specified in any order using --dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation=, and may be mixed with positional parameters (parameters not starting with -- are assigned in the order above, in the order they appear). All parameters except the directory may be omitted; the scope ID defaults to 0. --event= is ignored.<br />
  Because commas cannot be written in parameters in the DumpSurface\[...\] format, specify surface lists containing commas in Reference0 or subsequent headers.<br />
  Note that the response is not returned until processing is complete.<br />
  No additional data (success with a 200-series status code).
- **MoveAsync \[SSP\] \[not available remotely\]**: Performs the same operation as [`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md) without using Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  A move without async cannot be executed because it cannot return a response before the SSTP timeout and can cause a deadlock.<br />
  No additional data (success with a 200-series status code).
- **SetTrayIcon \[SSP\] \[not available remotely\]**: Performs the same operation as [`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md) without using Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  No additional data (success with a 200-series status code).
- **SetTrayBalloon \[SSP\] \[not available remotely\]**: Performs the same operation as [`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md) without using Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  No additional data (success with a 200-series status code).
- **SetProperty \[SSP\] \[not available remotely\]**: Writes a value to the [property system](../../list/propertysystem/index.md).<br />
  Parameter 0: Property name.<br />
  Parameter 1: Value to set.<br />
  No additional data (success with a 200-series status code).
- **GetProperty \[SSP\]**: Reads a value from the [property system](../../list/propertysystem/index.md).<br />
  Parameter 0: Property name.<br />
  The additional data is the retrieved property value.
- **SetCookie**: Writes to a general-purpose data storage area maintained for each client name specified by Sender.<br />
  It is intended to be used like browser cookies.<br />
  Parameter 0: Cookie name.<br />
  Parameter 1: Value to set.<br />
  No additional data (success with a 200-series status code).
- **GetCookie**: Reads from a general-purpose data storage area maintained for each client name specified by Sender.<br />
  Parameter 0: Cookie name.<br />
  The additional data is the retrieved cookie value.
