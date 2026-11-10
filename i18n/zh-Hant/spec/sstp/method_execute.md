# Method: EXECUTE

The EXECUTE method can be used to retrieve various kinds of ghost information and execute various commands that do not use Sakura Script.<br />
Executing this method does not make the ghost speak, but may change its internal state.

## EXECUTE example

```
EXECUTE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Command: GetName
```

## Request-specific headers

- **Command or Command\[param1,param2...\]**: The command to execute. The operation performed and the returned information are described below.<br />
  Parameters to pass to the command are specified after the square brackets.
- **Reference\* \[SSP\]**: Parameters can also be specified using the Reference0 and subsequent headers instead of using square brackets.

See below for the strings that can be specified in the Command header and the results returned as "additional data" in the response.

## Commands that can be specified in the Command header and the additional data returned

- **GetName**: The names of the running ghost (`\0` name), (`\1` name), comma-separated
- **GetNames \[SSP\]**: A list of the currently installed `\0` names, separated by line breaks and terminated by a blank line.
- **GetFMO \[SSP 2.5.57\] \[リモート制限あり\]**: Retrieves information equivalent to the contents of [FMO](../fmo-mutex/index.md).<br />
  However, it is limited to data managed internally by applications communicating over SSTP, and differs from the original FMO, which is shared by the concurrently running applications.<br />
  This is mainly used by console applications that have no window and cannot send Direct SSTP, to implement functionality equivalent to Direct SSTP using only Socket SSTP and the ReceiverGhostHWnd header.<br />
  Results are separated by line breaks and terminated by a blank line.<br />
  For remote requests, path information is omitted, and the headers and hwnd are replaced with dummy values.
- **GetGhostName \[SSP\]**: The name of the running ghost itself (the name in descript.txt)
- **GetShellName \[SSP\]**: The name of the shell currently used by the running ghost
- **GetBalloonName \[SSP\]**: The name of the balloon currently used by the running ghost
- **GetVersion**: The version of the baseware (the running software)
- **GetGhostNameList \[SSP 2.6.53\]**: A line-break-separated list of the names (the names in descript.txt) of all ghosts recognized by SSP
- **GetShellNameList \[SSP 2.6.53\]**: A line-break-separated list of the names (the names in descript.txt) of all shells recognized by the running ghost
- **GetBalloonNameList \[SSP 2.6.53\]**: A line-break-separated list of the names (the names in descript.txt) of all balloons recognized by SSP
- **GetHeadlineNameList \[SSP 2.6.53\]**: A line-break-separated list of the names (the names in descript.txt) of all headline sensors recognized by SSP
- **GetPluginNameList \[SSP 2.6.53\]**: A line-break-separated list of the names (the names in descript.txt) of all plugins recognized by SSP
- **GetShortVersion \[SSP 2.6.53\]**: The version of the baseware (the running software), containing only the period-separated version number<br />
  A simple comparison with values such as ssp.full.version in [version.json](https://ssp.shillest.net/archive/version.json) can be used to check whether this is the latest version.
- **GetStatus \[SSP 2.8.94\]**: The current execution state of the running ghost. This is the same as the Status header in a SHIORI/3.0 request or [currentghost.status](../../list/propertysystem/property-system/currentghost.status.md) in the property system.<br />
  If multiple states apply, they are comma-separated. See [※SHIORI Status header](../../list/propertysystem/property-system/currentghost.status.md) for the meaning of each value.<br />
  If no state applies, there is no additional data (status code 200).
- **Quiet \[リモート不可\]**: Remains silent until Restore is executed or 16 seconds have elapsed. No additional data (success with a status code in the 200 range)
- **Restore**: Cancels Quiet. No additional data (success with a status code in the 200 range)
- **CompressArchive \[SSP 2.7.23\] \[リモート不可\]**: Compresses the files in the specified folder into a ZIP file. If the destination file has a `.7z` extension, it is saved in 7z format; otherwise, it is saved in ZIP format (even if `.lzh` or `.cab` is specified, the contents are ZIP). Hidden files and folders are not included.<br />
  Parameter 0: Compressed file name (specify the full path; relative paths cannot be specified)<br />
  Parameter 1: Full path of the folder to compress<br />
  Parameter 2 and subsequent parameters: Options (optional)<br />
  The available options are as follows.<br />
  --event=event identifier……Specifying an event identifier continues compression after the response, and the event occurs when it finishes. If the identifier begins with On, the event with that identifier occurs; otherwise, OnCompressArchiveComplete or OnCompressArchiveFailure occurs. If omitted, the response is not returned until processing is complete.<br />
  --password=password……Enables AES-encrypted ZIP using the specified password.<br />
  See [OnCompressArchiveComplete](../../list/shiori-event/other/OnCompressArchiveComplete.md) and [OnCompressArchiveFailure](../../list/shiori-event/other/OnCompressArchiveFailure.md) for the specifications of events after the operation.<br />
  \[SSP 2.9.25\] This can also be called from SAORI over DirectSSTP using [internal_file's CompressArchive](../saori-ex/internal_file/internal_file.CompressArchive.md) (relative paths and `/` separators can also be used).<br />
  \[SSP 2.9.33\] If Parameter 1 is not a folder (for example, if it is a file path), compression fails with 400 without attempting to compress (if `--event=` is specified, the failure event—OnCompressArchiveFailure, or the identifier with `Failure` appended—occurs with `invalid parameter`). Before this version, passing a file path caused compression to fail with `file not found`.<br />
  For security reasons, the destination is restricted to locations under folders managed by SSP (locations specified in the "Folder" settings, such as the ghost and balloon folders).<br />
  This restriction may be tightened as appropriate, so it is safest to limit the destination to a location under the folder containing the ghost's own data.<br />
  No additional data (success with a status code in the 200 range)
- **ExtractArchive \[SSP 2.7.23\] \[リモート不可\]**: Extracts the specified archive. In addition to ZIP, formats such as 7z and tar can also be extracted (see [formats supported by internal_file's ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md#対応する形式)).<br />
  Parameter 0: Compressed file name (specify the full path; relative paths cannot be specified)<br />
  Parameter 1: Full path of the destination folder<br />
  Parameter 2 and subsequent parameters: Options (optional)<br />
  The available options are as follows.<br />
  --event=event identifier……Specifying an event identifier continues extraction after the response, and the event occurs when it finishes. If the identifier begins with On, the event with that identifier occurs; otherwise, OnExtractArchiveComplete or OnExtractArchiveFailure occurs. If omitted, the response is not returned until processing is complete.<br />
  --password=password……Extracts using the specified password. \[SSP 2.9.26\] The password prompt is not displayed. If a password is required but not specified, or if it is incorrect, extraction fails without displaying a dialog (the response is 500; if an event is specified, the identifier plus Failure, or [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md), occurs). Before \[SSP 2.9.25\], this option was ignored and a dialog was displayed.<br />
  \[SSP 2.9.26\] Even if the destination is specified as an absolute path containing `..`, it is rejected if the resolved path is outside a folder managed by SSP (previously, extraction outside managed folders was allowed).<br />
  See [OnExtractArchiveComplete](../../list/shiori-event/other/OnExtractArchiveComplete.md) and [OnExtractArchiveFailure](../../list/shiori-event/other/OnExtractArchiveFailure.md) for the specifications of events after the operation.<br />
  \[SSP 2.9.25\] This can also be called from SAORI over DirectSSTP using [internal_file's ExtractArchive](../saori-ex/internal_file/internal_file.ExtractArchive.md) (relative paths and `/` separators can also be used).<br />
  For security reasons, extraction is restricted to locations under folders managed by SSP (locations specified in the "Folder" settings, such as the ghost and balloon folders).<br />
  This restriction may be tightened as appropriate, so it is safest to limit the destination to a location under the folder containing the ghost's own data.<br />
  No additional data (success with a status code in the 200 range)
- **DumpSurface \[SSP 2.5.98\] \[リモート不可\]**: Outputs the composited surface image to the specified directory. The parameters are the same as for [`\![execute,dumpsurface]`](../../list/sakura-script/misc/bang-execute-dumpsurface-ID-prefix-ID-ID.md).<br />
  However, an event ID cannot be specified; specify the directory, scope ID, surface list, prefix, zero-position cropping, and animation ID \[SSP 2.9.05\] in that order.<br />
  \[SSP 2.9.08\] As with the SakuraScript version, parameters can also be specified in any order using the --dir= / --scope= / --surface= / --prefix= / --fromzero= / --animation= formats, and may be mixed with the positional format described above (parameters that do not begin with -- are assigned in the order they appear, following the order above). All parameters except the directory can be omitted; if the scope ID is omitted, it defaults to 0. --event= is ignored.<br />
  Since commas cannot be written in the parameters of the DumpSurface\[...\] format, specify surface lists containing commas using Reference0 or a subsequent Reference header.<br />
  Note that the response is not returned until processing is complete.<br />
  No additional data (success with a status code in the 200 range)
- **MoveAsync \[SSP\] \[リモート不可\]**: Executes the same operation as [`\![moveasync]`](../../list/sakura-script/surface/bang-moveasync.note.md) without going through Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  A move without async cannot be executed because the response cannot be returned before the SSTP timeout and this can cause a deadlock.<br />
  No additional data (success with a status code in the 200 range)
- **SetTrayIcon \[SSP\] \[リモート不可\]**: Executes the same operation as [`\![set,tasktrayicon]`](../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md) without going through Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  No additional data (success with a status code in the 200 range)
- **SetTrayBalloon \[SSP\] \[リモート不可\]**: Executes the same operation as [`\![set,trayballoon]`](../../list/sakura-script/event/bang-set-trayballoon.md) without going through Sakura Script. Parameters are specified in the same way as in the Sakura Script version.<br />
  No additional data (success with a status code in the 200 range)
- **SetProperty \[SSP\] \[リモート不可\]**: Writes a value to the [property system](../../list/propertysystem/index.md).<br />
  Parameter 0: Property name<br />
  Parameter 1: Value to set<br />
  No additional data (success with a status code in the 200 range)
- **GetProperty \[SSP\]**: Reads a value from the [property system](../../list/propertysystem/index.md).<br />
  Parameter 0: Property name<br />
  The additional data is the retrieved property value.
- **SetCookie**: Writes to a general-purpose data storage area saved separately for each client name specified by Sender.<br />
  This is intended to be used in the same way as browser "cookies".<br />
  Parameter 0: Cookie name<br />
  Parameter 1: Value to set<br />
  No additional data (success with a status code in the 200 range)
- **GetCookie**: Reads from the general-purpose data storage area saved separately for each client name specified by Sender.<br />
  Parameter 0: Cookie name<br />
  The additional data is the retrieved cookie value.
