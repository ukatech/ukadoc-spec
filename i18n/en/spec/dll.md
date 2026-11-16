# Common DLL Specification

## Common DLL Specification

This specification defines the common interface for DLL modules used by SHIORI, SAORI, and other Ukagaka systems.

## Memory Management

All arguments and return values are passed using Windows Global Memory. Specifically, processing follows these steps:

- The baseware allocates memory with GlobalAlloc() using the GMEM_FIXED flag and writes data to it
- The module casts the received HGLOBAL to (char\*) and accesses the data directly
- The module reads the data length from the len parameter and reads the required data
- The module frees the memory with GlobalFree()
- To return a result, the module allocates new memory with GlobalAlloc() using GMEM_FIXED
- The module writes the result to the allocated memory and sets len to the new data length
- The baseware frees the returned memory handle with GlobalFree() after use

Notes:

- GlobalLock()/GlobalUnlock() are unnecessary when using the GMEM_FIXED flag
- Casting HGLOBAL to (char\*) enables direct memory access
- The passed memory is not guaranteed to be NULL-terminated, so always use the len parameter to limit the access range
- For robust operation regardless of the baseware implementation, it is recommended to allocate one byte more than len for return data and zero-terminate it

## request Function

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

All requests are made through a single function called request. The request function is the primary interface of a Ukagaka module and handles all requests from the baseware.

The request data format is designed with reference to HTTP and SSTP header formats and follows these rules:

- All lines are separated by CR+LF (0x0D, 0x0A)
- The first line contains the command name and protocol version
- The second and subsequent lines contain any number of headers in the format "header name: value"
- The end of the header section is indicated by two consecutive CR+LF sequences (an additional empty line)
- The character encoding follows the scheme specified in the header (typically UTF-8 or the default OEM codepage)

## Lifecycle Functions

The following functions are called when the DLL is loaded and unloaded.

### loadu Function

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

This function initializes the module.<br />
The global memory in the first argument contains the module's directory path in *UTF-8 encoding*.

It was implemented in SSP 2.6.92 (2025/1/16). Earlier versions implement only load.

Example operations:

- Load required data files using the passed path as the current directory
- Initialize resources required for module operation
- Initialize log files and databases as needed

Notes:

- Always free the passed global memory, even if the string data is not needed
- Return TRUE if initialization succeeds, or FALSE if it fails
- Baseware uses this function preferentially

#### load Function

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

The legacy version of the loadu function.<br />
It has the same specification as loadu, except that the module directory path in the first argument is encoded in the default OEM codepage (CP932 in Japanese environments).

Notes:

- Used as a fallback when loadu is not implemented
- For compatibility, it is recommended to implement both load and loadu and ignore calls to load if loadu has already initialized the module
- For Unicode support, the received path must be converted appropriately to a wide-character string

#### unload Function

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

This function performs module shutdown. It is called by the baseware when the module is unloaded.

Operations to implement:

- Release file handles opened with CreateFile or similar functions
- Release synchronization objects created with CreateMutex or similar functions
- Wait for threads created with CreateThread or similar functions to terminate and perform cleanup
- Release all other system resources allocated by the module

The return value is not currently used, but returning TRUE is recommended for future extensibility.

## Multi-Instance Functions (Optional)

`load` / `request` / `unload` support only one instance per DLL. For baseware that needs to create multiple instances from the same DLL in one process, the following functions, which distinguish instances by id, can **optionally** be implemented. The module remains valid without them and works as before with baseware that does not call them.

```
extern "C" __declspec(dllexport) long __cdecl multi_loadu(HGLOBAL h, long len);
extern "C" __declspec(dllexport) long __cdecl multi_load(HGLOBAL h, long len);
extern "C" __declspec(dllexport) BOOL __cdecl multi_unload(long id);
extern "C" __declspec(dllexport) HGLOBAL __cdecl multi_request(long id, HGLOBAL h, long *len);
```

- **multi_loadu / multi_load**: Create a new instance with the same arguments as `loadu` / `load`. The module directory path encoding also follows `loadu` (UTF-8) and `load` (the default OEM codepage), respectively. The return value is an id identifying the instance (an integer of 1 or greater); returning `-1` on failure is recommended. Baseware treats return values of 0 or less as failure. As with `loadu` / `load`, the module frees the memory
- **multi_unload**: Shut down the instance identified by id. Returns TRUE on success or FALSE if the id does not exist
- **multi_request**: Pass a request in the same format as `request` to the instance identified by id. Returns NULL if the id does not exist

Notes:

- The id 0 is assigned to the instance handled by the legacy `load` / `request` / `unload`. `multi_load*` must not return 0
- Both the legacy functions and the multi-instance functions can be implemented in the same DLL. Their instances are treated as separate
- YAYA's `multi_load*` returns an id even if dictionary loading fails (just as `load` always returns TRUE; use `CI_check_failed` to check for failure)
- SSP does not use these functions (they are intended for baseware other than SSP)

## YAYA-Specific Functions

The following functions are implemented independently by YAYA (`yaya.dll`). They are used to work with debugging check tools and are not part of the SHIORI specification. Other modules do not need to implement them, and baseware does not need to call them.

!!! note "Note"
    The specification may change to suit YAYA's needs. Like the multi-instance functions in the previous section, functions prefixed with `multi_` operate on the instance identified by id.

### CI_check_failed Function

```
extern "C" __declspec(dllexport) BOOL __cdecl CI_check_failed(void);
extern "C" __declspec(dllexport) BOOL __cdecl multi_CI_check_failed(long id);
```

Returns TRUE when dictionary loading has failed and operation is suppressed, or when the module is in emergency mode. Returns FALSE for a nonexistent id (in the `multi_` version) or before `load`.

### Set_loghandler Function

```
extern "C" __declspec(dllexport) void __cdecl Set_loghandler(void (*loghandler)(const wchar_t *str, int mode, int id));
extern "C" __declspec(dllexport) void __cdecl multi_Set_loghandler(long id, void (*loghandler)(const wchar_t *str, int mode, int id));
```

Registers a callback function to receive YAYA logs. Registration enables log output. The `multi_` version can only register a callback for an instance created by `multi_load*` and does nothing for a nonexistent id.

The callback arguments are as follows.

- **str**: Log string (UTF-16). An empty string when `mode` is a control value
- **mode**: Log type or control value
- **id**: Log message number (not the instance id)

The values of `mode` are as follows.

- **0**: Information
- **1**: Fatal error
- **2**: Error
- **3**: Warning
- **4**: Note
- **6**: End of log
- **16 / 17 / 32**: Notification of the multibyte character encoding for subsequent logs. 16 is Shift_JIS, 17 is UTF-8, and 32 is the OS default. Called once at the start of the log

The callback is called on the thread that called `load` / `request` / `unload`.

### logsend Function

```
extern "C" __declspec(dllexport) BOOL __cdecl logsend(long hwnd);
```

Available only in the Windows DLL version. Pass the handle (HWND) of the window that receives logs via `WM_COPYDATA`. Always returns TRUE. If a callback is registered with `Set_loghandler`, it takes precedence.

`WM_COPYDATA` has the same value as the `mode` of `Set_loghandler` in `dwData`, and the log string (UTF-16, NUL-terminated) in `lpData`.
