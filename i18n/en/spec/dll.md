# Common DLL Specification

## Common DLL Specification

This specification defines the common interface for DLL modules used by SHIORI, SAORI, and other Ukagaka systems.

## Memory Management

All argument and return-value transfer uses Windows Global Memory. Specifically, perform the following steps:

- The baseware allocates memory with GlobalAlloc() using the GMEM_FIXED flag, then writes the data
- The module casts the received HGLOBAL to (char\*) and accesses the data directly
- The module refers to the len parameter to get the data length and reads the necessary data
- The module frees the memory with GlobalFree()
- When returning a result, the module allocates new memory with GlobalAlloc() using GMEM_FIXED
- The module writes the result to the allocated memory and sets len to the new data length
- After using the returned memory handle, the baseware frees it with GlobalFree()

Notes:

- When using the GMEM_FIXED flag, GlobalLock()/GlobalUnlock() are not required
- Casting HGLOBAL to (char\*) allows direct memory access
- The passed memory is not guaranteed to be NULL-terminated, so always refer to the len parameter to limit the range of access
- To ensure robust behavior independent of the baseware implementation, it is preferable to allocate one byte more than len for the return-value memory and zero-terminate it

## request Function

```
extern "C" __declspec(dllexport) HGLOBAL __cdecl request(HGLOBAL h, long *len);
```

All requests are handled by the single function named request. The request function is the main interface for Ukagaka modules and handles all requests from the baseware.

The request data format is designed with reference to HTTP and SSTP header formats, and follows these rules:

- All lines are separated by CR+LF (0x0D, 0x0A)
- The first line specifies the command name and protocol version
- The second and subsequent lines contain any number of headers in the format "header name: value"
- The end of the header section is indicated by two consecutive CR+LF sequences (an additional blank line)
- Character encoding follows the method specified in the headers (typically UTF-8 or the default OEM codepage)

## Lifecycle Functions

The following functions are called when the DLL is loaded and unloaded.

### loadu Function

```
extern "C" __declspec(dllexport) BOOL __cdecl loadu(HGLOBAL h, long len);
```

This function initializes the module.<br />
The global memory passed as the first argument contains the module directory path encoded in *UTF-8*.

Implemented starting with SSP 2.6.92 (2025/1/16). Earlier versions only implement load.

Examples of processing:

- Use the passed path as the current directory and load the necessary data files
- Initialize resources required for the module to operate
- Initialize log files or databases as necessary

Notes:

- Always free the passed global memory, even if the string data is not needed
- Return TRUE if initialization succeeds, or FALSE if it fails
- This function is given priority by the baseware

#### load Function

```
extern "C" __declspec(dllexport) BOOL __cdecl load(HGLOBAL h, long len);
```

The legacy version of the loadu function.<br />
Its specification is the same as that of the loadu function, except that the module directory path passed as the first argument is encoded using the default OEM codepage (CP932 in Japanese environments).

Notes:

- Used as a fallback if the loadu function is not implemented
- To ensure compatibility, it is preferable to implement both load and loadu, and to ignore load if it is called after loadu has initialized the module
- To support Unicode, the received path must be converted to a wide string appropriately

#### unload Function

```
extern "C" __declspec(dllexport) BOOL __cdecl unload();
```

This function terminates the module. It is called by the baseware when the module is unloaded.

Processing to implement:

- Release file handles opened with CreateFile, etc.
- Release synchronization objects created with CreateMutex, etc.
- Wait for threads created with CreateThread, etc. to terminate, then perform cleanup
- Release all other system resources allocated by the module

The return value is not currently used, but returning TRUE is preferable for future extensibility.
