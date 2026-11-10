# FMO (File Mapping Object)

All baseware maintain a named file mapping object (FMO) while running.<br />
By reading this inter-process shared memory, you can obtain information about running ghosts at relatively low cost.<br />
To avoid reading incomplete information while it is being written, mutual exclusion is handled by [FMO Mutex](fmo-mutex.md). Please check it as well.

- **FMO name and character encoding**: Sakura: OS-dependent; Shift JIS on Japanese OSes<br />
  SakuraUnicode: fixed to UTF-8 \[SSP 2.5.26以降～\]
- **FMO size**: The first 4 bytes (bytes 0–3) indicate the size allocated for the FMO.<br />
  This is a fixed value indicating the allocation size of the FMO itself, not the length of the information written to it.<br />
  The value is currently fixed at 0x00010000 in little-endian, or 64 KB.<br />
  To ensure compatibility with other programs, changing the size is not currently considered.
- **Data body**: The data body of the FMO starts at byte 4. It uses the following format.<br />
  (32-byte identifier).(key name)\[`\1`\]value\[`\r\n`\]<br />
  \[`\1`\] is the byte value 1, and \[`\r\n`\] is CR+LF (line break).<br />
  This format is repeated over multiple lines.
- **End of data**: The end of data is marked by the byte value 0, as in a C string.<br />
  Therefore, the maximum usable size of the data body is 65531 bytes (65536 - 4 - 1).<br />
  If you need to write to an FMO, take care to avoid writing incomplete information if the size limit is likely to be exceeded.<br />
  If the size limit is likely to be exceeded, it is preferable not to write an entire data set; if that is not possible, at least avoid ending in the middle of a line.

## Data body example

```
ssp_fmo_header_00004468_000f0dea.path[\1]D:\ssp\
ssp_fmo_header_00004468_000f0dea.hwnd[\1]986602
ssp_fmo_header_00004468_000f0dea.name[\1]ラーシェ
ssp_fmo_header_00004468_000f0dea.keroname[\1]ティセ
ssp_fmo_header_00004468_000f0dea.sakura.surface[\1]0
ssp_fmo_header_00004468_000f0dea.kero.surface[\1]10
ssp_fmo_header_00004468_000f0dea.kerohwnd[\1]1052114
ssp_fmo_header_00004468_000f0dea.hwndlist[\1]986602,1052114
ssp_fmo_header_00004468_000f0dea.ghostpath[\1]D:\ssp\ghost\DE10_3001\
ssp_fmo_header_00004468_00120da6.path[\1]D:\ssp\
ssp_fmo_header_00004468_00120da6.hwnd[\1]1183142
ssp_fmo_header_00004468_00120da6.name[\1]Emily
ssp_fmo_header_00004468_00120da6.keroname[\1]Teddy
ssp_fmo_header_00004468_00120da6.sakura.surface[\1]20
ssp_fmo_header_00004468_00120da6.kero.surface[\1]10
ssp_fmo_header_00004468_00120da6.kerohwnd[\1]1117626
ssp_fmo_header_00004468_00120da6.hwndlist[\1]1183142,1117626,921002,2035340,658950
ssp_fmo_header_00004468_00120da6.ghostpath[\1]D:\ssp\ghost\emily4\
```

- **32-byte identifier**: A unique identifier for one ghost set. You must choose a string that does not duplicate any other identifier, at least within the FMO.<br />
  Common approaches include combining unique information and taking its MD5 hash, or combining it with an HWND (window handle).<br />
  Although the length is not specified by the Materia standard, it should be fixed at 32 bytes for compatibility.

- **Key name and value**: The key indicating the type of information and the information itself. They are as follows.

  - **path**: Full path to the root folder of the running baseware.
  - **hwnd**: Window handle of the main window. Decimal notation.
  - **name**: Same as sakura.name in descript.txt.
  - **keroname**: Same as kero.name in descript.txt.
  - **sakura.surface**: Surface ID currently displayed on the `\0` side. Decimal notation.
  - **kero.surface**: Surface ID currently displayed on the `\1` side. Decimal notation.
  - **kerohwnd**: Window handle of the `\1` side window. Decimal notation.\[SSPのみ\]
  - **hwndlist**: Comma-separated list of all window handles currently in use. Decimal notation.\[SSPのみ\]
  - **ghostpath**: Full path to the running ghost.\[SSPのみ\]
  - **fullname**: The name entry in the running ghost's descript.txt.\[SSP 2.5.58～\]
  - **modulestate**: A comma-separated string indicating the state of the modules loaded in the running ghost.\[SSP 2.5.79～\]<br />
    shiori:running SHIORI is loaded (if it is not loaded, the string itself is absent)<br />
    makoto-ghost:running The ghost-side MAKOTO is loaded<br />
    makoto-shell:running The shell-side MAKOTO is loaded<br />
    compatible:running Compatibility mode is enabled and script.txt, etc. are loaded<br />
    If communication between SSP and the various modules has an error, critical is used instead of running<br />
    Example: ssp_fmo_header_00004468_00120da6.modulestate\[`\1`\]shiori:running,makoto-ghost:running\\r\\n
