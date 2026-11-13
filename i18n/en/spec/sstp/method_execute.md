# Method: EXECUTE

The EXECUTE method retrieves various information about a ghost and executes various commands without using Sakura Script.<br />
The ghost does not speak when this method is executed, but its internal state may change.

## EXECUTE sample

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## Request-specific headers

- **Command or Command\[param1,param2...\]**: The command to execute. The actions performed and information returned are described below.<br />
  The square brackets and their contents specify parameters to pass to the command.
- **Reference\* \[SSP\]**: Parameters can also be specified in headers starting with Reference0 instead of using square brackets.

See below for the strings that can be specified in the Command header and the results returned as additional data in the response.

## Commands available in the Command header and the additional data returned

- **GetName**: The running ghost's (`\0` name),(`\1` name), separated by a comma.
- **GetNames \[SSP\]**: A list of the `\0` names of currently installed ghosts, separated by newlines and terminated by an empty line.
- **GetFMO \[SSP 2.5.57\] \[remote restrictions apply\]**: Retrieves information equivalent to the contents of [FMO](../fmo-mutex/index.md).<br />
  Unlike the actual FMO, which is shared by concurrently running applications, this is limited to information managed internally by the application communicating via SSTP.<br />
  It is mainly used by console applications that have no window and cannot send Direct SSTP, to use the ReceiverGhostHWnd header with Socket SSTP alone to achieve functionality equivalent to Direct SSTP.<br />
  Entries are separated by newlines and terminated by an empty line.<br />
  For remote requests, path information is omitted, and the header and hwnd are replaced with dummy values.
- **GetGhostName \[SSP\]**: The name of the running ghost itself (name in descript.txt).
- **GetShellName \[SSP\]**: The name of the shell currently used by the running ghost.
- **GetBalloonName \[SSP\]**: The name of the balloon currently used by the running ghost.
- **GetVersion**: The version of the baseware (the running software).
- **GetGhostNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all ghosts recognized by SSP.
- **GetShellNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all shells recognized by the running ghost.
- **GetBalloonNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all balloons recognized by SSP.
- **GetHeadlineNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all headlines recognized by SSP.
- **GetPluginNameList \[SSP 2.6.53\]**: A newline-separated list of the names (name in descript.txt) of all plugins recognized by SSP.
- **GetGhostUUIDList \[SSP 2.9.35\]**: A newline-separated list of the [UUID](../../list/propertysystem/property-system/general-property/uuid.md)s of all ghosts recognized by SSP, in the same order as GetGhostNameList.<br />
  **GetBalloonUUIDList \[SSP 2.9.35\]**: The UUIDs of all balloons, in the same order as GetBalloonNameList.<br />
  **GetShellUUIDList \[SSP 2.9.35\]**: The UUIDs of all shells recognized by the running ghost, in the same order as GetShellNameList.<br />
  UUIDs are calculated from the values in descript.txt using the [metainfo-standard](https://github.com/ukatech/metainfo-standard) procedure (the same as `uuid` in the property system).
- **GetGhostMetaInfoList \[SSP 2.9.35\]**: A newline-separated list of the URLs of the metainfo folders of all ghosts recognized by SSP, in the same order as GetGhostNameList.<br />
  **GetBalloonMetaInfoList \[SSP 2.9.35\]**: The URLs of the metainfo folders of all balloons, in the same order as GetBalloonNameList.<br />
  **GetShellMetaInfoList \[SSP 2.9.35\]**: The URLs of the metainfo folders of all shells recognized by the running ghost, in the same order as GetShellNameList.<br />
  These are the [metainfo](../../descript/ghost/descript-txt/metainfo.md) values in descript.txt. If absent, the URL is derived from [githubrepo](../../descript/ghost/descript-txt/githubrepo.md) (the default branch is assumed to be `master`). If neither is present, the entry is an empty line.
- **GetShortVersion \[SSP 2.6.53\]**: The version of the baseware (the running software), containing only the period-separated version number.<br />
  A simple comparison with ssp.full.version in [version.json](https://ssp.shillest.net/archive/version.json), for example, can determine whether it is the latest version.
- **GetStatus \[SSP 2.8.94\]**: The current execution state of the running ghost. It has the same contents as the Status header of a SHIORI/3.0 request and [currentghost.status](../../list/propertysystem/property-system/currentghost.status.md) in the property system.<br />
  If multiple states apply, they are separated by commas. See [SHIORI Status header](../../list/propertysystem/property-system/currentghost.status.md) for the meaning of each value.<br />
  If no state applies, there is no additional data (status code 200).
- **Quiet \[not available remotely\]**: Remains silent until Restore is executed or 16 seconds have passed. No additional data (a 200-series status code indicates success).
- **Restore**: Cancels Quiet. No additional data (a 200-series status code indicates success).
- **CompressArchive \[SSP 2.7.23\] \[not available remotely\]**: Compresses the files in the specified folder into a ZIP file. If the destination extension is `.7z`, the format is 7z; otherwise, it is ZIP (even if `.lzh` or `.cab` is specified, the contents are ZIP). Hidden files and folders are excluded.<br />
  Parameter 0: Archive file name (specify a full path; relative paths are not allowed).<br />
  Parameter 1: Full path of the folder to compress.<br />
  Parameter 2 onward: Options (optional).<br />
  The options are as follows.<br />
  --event=event identifier: If an event identifier is specified, compression continues after the response, and an event occurs upon completion. If the identifier starts with On, an event with that identifier occurs; otherwise, OnCompressArchiveComplete or OnCompressArchiveFailure occurs. If omitted, no response is returned until processing completes.<br />
  --password=password: Enables AES-encrypted ZIP using the specified password.<br />
  See [OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md) and [OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md) for specifications of events after the operation.<br />
  \[SSP 2.9.25\] From SAORI over DirectSSTP, this can also be called using [CompressArchive in internal_file](../saori-ex/internal_file/internal_file.CompressArchive.md) (relative paths and `/` separators can also be used).<br />
  \[SSP 2.9.33\] If parameter 1 is not a folder (for example, a file path), the operation fails with 400 without compressing (if `--event=` is specified, the failure event (OnCompressArchiveFailure or the identifier with `Failure` appended) occurs with `invalid parameter`). Previously, passing a file path caused compression to fail with `file not found`.<br />
  For security reasons, the compression destination is restricted to locations under folders managed by SSP (locations specified in the "Folders" settings, such as the ghost and balloon folders).<br />
  As this restriction may be strengthened as needed, it is safer to limit the destination to a folder under the folder containing the ghost's own data.<br />
  No additional data (a 200-series status code indicates success).
- **ExtractArchive \[SSP 2.7.23\] \[not available remotely\]**: Extracts the specified archive. In addition to ZIP, formats such as 7z and tar can also be extracted (see [ExtractArchive in internal_file](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式) for supported formats).<br />
  Parameter 0: Archive file name (specify a full path; relative paths are not allowed).<br />
  Parameter 1: Full path of the destination folder.<br />
  Parameter 2 onward: Options (optional).<br />
  The options are as follows.<br />
  --event=event identifier: If an event identifier is specified, extraction continues after the response, and an event occurs upon completion. If the identifier starts with On, an event with that identifier occurs; otherwise, OnExtractArchiveComplete or OnExtractArchiveFailure occurs. If omitted, no response is returned until processing completes.<br />
  --password=password: Extracts using the specified password. \[SSP 2.9.26\] No password prompt is displayed. If a password is required but not specified, or is incorrect, the operation fails without a dialog (the response is 500; if an event was specified, the event is the identifier plus Failure, or [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md)). In \[SSP 2.9.25\] and earlier, this option was ignored and a dialog was displayed.<br />
  \[SSP 2.9.26\] Even if an absolute path containing `..` is specified as the destination, it is rejected if the resolved path is outside folders managed by SSP (previously, extraction outside managed folders was possible).<br />
  See [OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md) and [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md) for specifications of events after the operation.<br />
  \[SSP 2.9.25\] From SAORI over DirectSSTP, this can also be called using [ExtractArchive in internal_file](../saori-ex/internal_file/internal_file.ExtractArchive.md) (relative paths and `/` separators can also be used).<br />
  For security reasons, the extraction destination is restricted to locations under folders managed by SSP (locations specified in the "Folders" settings, such as the ghost and balloon folders).<br />
  As this restriction may be strengthened as needed, it is safer to limit the destination to a folder under the folder containing the ghost's own data.<br />
  No additional data (a 200-series status code indicates success).
- **DumpSurface \[SSP 2.5.98\] \[not available remotely\]**: Outputs composited surface images to the specified directory. The parameters are the same as for [`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md).<br />
  However, an event ID cannot be specified; specify the directory, scope ID, surface list, prefix, zero-position cropping, and animation ID \[SSP 2.9.05\], in that order.<br />
  \[SSP 2.9.08\] As with the Sakura Script version, parameters can also be specified in any order using the forms --dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation=, and mixed with positional parameters (parameters not starting with -- are assigned in the order listed above, in the order they appear). All parameters except the directory can be omitted; the scope ID defaults to 0. --event= is ignored.<br />
  Because commas cannot be used in parameters in the DumpSurface\[...\] form, specify surface lists containing commas in Reference0 and subsequent headers.<br />
  Note that no response is returned until processing completes.<br />
  No additional data (a 200-series status code indicates success).
- **MoveAsync \[SSP\] \[not available remotely\]**: Performs the same operation as [`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md) without using Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  A move without async cannot be executed because it cannot return a response before the SSTP timeout and would cause a deadlock.<br />
  No additional data (a 200-series status code indicates success).
- **SetTrayIcon \[SSP\] \[not available remotely\]**: Performs the same operation as [`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md) without using Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  No additional data (a 200-series status code indicates success).
- **SetTrayBalloon \[SSP\] \[not available remotely\]**: Performs the same operation as [`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md) without using Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  No additional data (a 200-series status code indicates success).
- **SetProperty \[SSP\] \[not available remotely\]**: Writes a value to the [property system](../../list/propertysystem/index.md).<br />
  Parameter 0: Property name.<br />
  Parameter 1: Value to set.<br />
  No additional data (a 200-series status code indicates success).
- **GetProperty \[SSP\]**: Reads a value from the [property system](../../list/propertysystem/index.md).<br />
  Parameter 0: Property name.<br />
  The additional data is the retrieved property value.
- **SetCookie**: Writes to a general-purpose data storage area maintained separately for each client name specified by Sender.<br />
  It is intended for use similar to browser cookies.<br />
  Parameter 0: Cookie name.<br />
  Parameter 1: Value to set.<br />
  No additional data (a 200-series status code indicates success).
- **GetCookie**: Reads from a general-purpose data storage area maintained separately for each client name specified by Sender.<br />
  Parameter 0: Cookie name.<br />
  The additional data is the retrieved cookie value.
