# Memo

## Baseware Feature Comparison

| Feature List | MATERIA | SSP | CROW | ninix-kagari |
| --- | --- | --- | --- | --- |
| Console | ○ | × | × | △ |
| Clock synchronization | ○ | ○ | ○ | × |
| Headline sensor | ○ | ◎ | ○ | × |
| Mail check | ○ | ○ | ○ | × |
| Plugin | ○ | ◎ | × | × |
| Baseware update | × | △ | ○ | × |
| Shell scaling | × | ○ | ○ | ○ |
| Dressup | △ | ○ | × | △ |
| Calendar | × | ○ | × | × |
| IM | × | ○ | × | × |
| Multiple instances | △ | ◎ | ○ | ○ |
| Free movement of ghosts | × | ○ | × | × |
| Multiple partners | × | ○ | × | ○ |

SSP's headline sensor can also use RSS.

SSP's baseware update feature only provides a check function.

There are many plugins exclusive to SSP.

In MATERIA583, a bug prevents dressup of the partner.

MATERIA can run multiple instances if there are multiple executable files.

SSP can run multiple characters in a single process.

## Recommended Site Banners

Only MATERIA and SSP can display these.

Place banners in the \*/ghost/master/banner/ folder.

In urllist, follow the format for each SHIORI and write the entries

"Site name" "URL" "Banner file name (without the extension)"

in that order.

## Notes and Tips on Compatibility

- In MATERIA, mail checks, network update counts, and similar values start counting from 0.

  SSP and CROW start counting from 1.

  In SSP, setting useorigin1 in SHIORI Resource to 0 makes it zero-origin, as in MATERIA.

- Only MATERIA supports surface numbers up to 8192.

- In MATERIA and CROW, transparency does not work correctly when pna is used for overlay.

- MATERIA recognizes surface animation wait times only up to 10.

  To make them longer, specify the same animation multiple times in a row.

- Only SSP and CROW can load files encrypted using dft/dfp/dgt/dgp.

- Animations run slightly faster (more smoothly) in SSP.

- In SSP, other operations are possible while the inputbox is open.

- SSP and CROW support semi-transparency in balloons as well.

  However, inputbox-related elements cannot be made transparent.

## SSP-Only Features

- The following image formats are supported.

  BMP/PNG/JPEG/GIF/MAG/XBM/PI/ICO/CUR

- Transparency can be displayed using 32bitPNG.

- The following compressed files can be installed.

  CAB/self-extracting archives

- surfacetable.txt (replaces the display of the surface test window)

  surfaces2.txt (surfaces.txt that can be overridden for SSP)

  developer_options.txt (text file for specifying files to exclude when creating updates2.dau or nar with SSP)

- Play talks by dragging and dropping SSF files.
