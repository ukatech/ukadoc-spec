# Common DLL Specification

## Common DLL Specification

This specification defines the common interface for DLL modules used by SHIORI, SAORI, and other Ukagaka systems.

## Memory Management

All arguments and return values are passed using Windows Global Memory. Specifically, the procedure is as follows:

- The baseware allocates memory using GlobalAlloc() with the GMEM_FIXED flag and writes data to it
- The module casts the received HGLOBAL to (char\*) and accesses the data directly
- The module uses the len parameter to obtain the data length and reads the required data
- The module frees the memory using GlobalFree()
- To return a result, the module allocates new memory using GlobalAlloc() with GMEM_FIXED
- The module writes the result to the allocated memory and sets len to the new data length
- The baseware frees the returned memory handle using GlobalFree() after use

Notes:

- GlobalLock()/GlobalUnlock() are unnecessary when using the GMEM_FIXED flag
- Casting HGLOBAL to (char\*) allows direct memory access
- The passed memory is not guaranteed to be NULL-terminated, so always use the len parameter to limit the access range
- It is recommended to allocate one byte more than len for return-value memory and zero-terminate it to ensure robust operation regardless of the baseware implementation

## request Function

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

All requests are made through a single function named request. The request function is the primary interface of a Ukagaka module and handles all requests from the baseware.

The request data format is designed after HTTP and SSTP headers and follows these rules:

- All lines are separated by CR+LF (0x0D, 0x0A)
- The first line contains the command name and protocol version
- The second and subsequent lines contain any number of headers in the form "header name: value"
- The end of the header section is indicated by two consecutive CR+LF sequences (an additional blank line)
- The character encoding follows the scheme specified in the header (typically UTF-8 or the default OEM codepage)

## Lifecycle Functions

The following functions are called when the DLL is loaded and unloaded.

### loadu Function

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

This function initializes the module.<br />
The global memory in the first argument contains the module's directory path in *UTF-8 encoding*.

Implemented in SSP 2.6.92 (2025/1/16). Earlier versions implement only load.

Example operations:

- Read the required data files using the passed path as the current directory
- Initialize the resources required for module operation
- Initialize log files and databases as needed

Notes:

- Always free the passed global memory, even if the string data is not needed
- Return TRUE if initialization succeeds, or FALSE if it fails
- The baseware uses this function in preference to load

#### load Function

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

The legacy version of the loadu function.<br />
Its specification is the same as loadu, except that the module directory path in the first argument is encoded in the default OEM codepage (CP932 in a Japanese environment).

Notes:

- Used as a fallback when the loadu function is not implemented
- For compatibility, it is recommended to implement both load and loadu and ignore a call to load if initialization has already been performed by loadu
- For Unicode support, the received path must be converted to a wide-character string as appropriate

#### unload Function

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

This function performs module shutdown. It is called by the baseware when the module is unloaded.

Operations to implement:

- Release file handles opened with CreateFile or similar functions
- Release synchronization objects created with CreateMutex or similar functions
- Wait for threads created with CreateThread or similar functions to terminate, and perform cleanup
- Release all other system resources allocated by the module

The return value is not currently used, but returning TRUE is recommended for future extensibility.

## Multi-Instance Functions (Optional)

`load` / `request` / `unload` support only one instance per DLL. For baseware that needs to create multiple instances from the same DLL in one process, the following functions can **optionally** be implemented to distinguish instances by id. The module remains valid without them and works as before with baseware that does not call them.

```
extern "C" __declspec(dllexport) long __cdecl multi_loadu(HGLOBAL h, long len);
extern "C" __declspec(dllexport) long __cdecl multi_load(HGLOBAL h, long len);
extern "C" __declspec(dllexport) BOOL __cdecl multi_unload(long id);
extern "C" __declspec(dllexport) HGLOBAL __cdecl multi_request(long id, HGLOBAL h, long *len);
```

- **multi_loadu / multi_load**: Create a new instance using the same arguments as `loadu` / `load`. The module directory path uses the same character encoding as `loadu` (UTF-8) or `load` (the default OEM codepage), respectively. The return value is an id identifying the instance (an integer of 1 or greater). As with `loadu` / `load`, the module frees the memory
- **multi_unload**: Shuts down the instance identified by id. Returns TRUE on success, or FALSE if the id does not exist
- **multi_request**: Passes a request in the same format as `request` to the instance identified by id. Returns NULL if the id does not exist

Notes:

- The id 0 is assigned to the instance handled by the legacy `load` / `request` / `unload` functions. `multi_load*` must not return 0
- Both the legacy functions and the multi-instance functions can be implemented in the same DLL. Their instances are treated as separate
- The return value of `multi_load*` on failure is unspecified (YAYA always returns an id)
- SSP does not use these functions (they are intended for baseware other than SSP)

## YAYA-Specific Functions

The following functions are implemented independently by YAYA (`yaya.dll`). They are used to communicate with debugging tools and are not part of the SHIORI specification. Other modules do not need to implement them, and baseware does not need to call them.

!!! note "Note"
    The specification may change at YAYA's discretion. Like the multi-instance functions in the previous section, functions prefixed with `multi_` operate on the instance identified by id.

### CI_check_failed Function

```
extern "C" __declspec(dllexport) BOOL __cdecl CI_check_failed(void);
extern "C" __declspec(dllexport) BOOL __cdecl multi_CI_check_failed(long id);
```

Returns TRUE when dictionary loading has failed and operation is suppressed, or when in emergency mode. Returns FALSE for a nonexistent id (in the `multi_` version) or before `load`.

### Set_loghandler Function

```
extern "C" __declspec(dllexport) void __cdecl Set_loghandler(void (*loghandler)(const wchar_t *str, int mode, int id));
extern "C" __declspec(dllexport) void __cdecl multi_Set_loghandler(long id, void (*loghandler)(const wchar_t *str, int mode, int id));
```

Registers a callback function to receive YAYA logs. Registering it enables log output. The `multi_` version can only register a callback for an instance created by `multi_load*` and does nothing if the id does not exist.

The callback arguments are as follows.

- **str**: The log string (UTF-16). An empty string when `mode` is a control value
- **mode**: The log type or control value
- **id**: The log message number (not the instance id)

The values of `mode` are as follows.

- **0**: Information
- **1**: Fatal error
- **2**: Error
- **3**: Warning
- **4**: Note
- **6**: End of log
- **16 / 17 / 32**: Notification of the character encoding of multibyte characters in subsequent log entries. 16 is Shift_JIS, 17 is UTF-8, and 32 is the OS default. Called once at the start of the log

The callback is called on the thread that called `load` / `request` / `unload`.

### logsend Function

```
extern "C" __declspec(dllexport) BOOL __cdecl logsend(long hwnd);
```

Available only in the Windows DLL version. Pass the handle (HWND) of the window that receives logs via `WM_COPYDATA`. Always returns TRUE. If a callback is registered with `Set_loghandler`, it takes precedence.

The `dwData` field of `WM_COPYDATA` contains the same value as `mode` in `Set_loghandler`, and `lpData` contains the log string (UTF-16, NUL-terminated).
