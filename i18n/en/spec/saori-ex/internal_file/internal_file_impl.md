# Notes for Baseware Implementing MediaInfo

MediaInfo is limited to what can be implemented without difficulty in baseware on other operating systems using existing components (ffprobe / libavformat, TagLib, standard OS media APIs, etc.).

- **Required (MUST)**: The names, units, and forms of the keys above; use an empty string for values that could not be retrieved; value formatting (line breaks as `0x01`, removal of NUL); the base for relative paths (ghost/master); response form (`Result` + `Value0..`); leave keys not specified in the specification empty and do not return custom keys; accept `/` as a path separator.
- **Recommended (SHOULD)**: Also accept `\` as a path separator (ghost authors use `\`, but on other operating systems `\` may be an ordinary character in a filename). Join tags with multiple values using ` ;  `.
- **May vary by implementation**: Supported formats (additional formats such as ICO and HEIC are fine if they can be retrieved; not retrieving them is not a defect); estimation of the character encoding of original tags; accuracy of VBR duration; how `Result` is determined; which items can be retrieved from which formats. The mapping of tags by format (for example, ID3v2's `TIT2` becoming `title`) is not specified.
- **How to check conformance**: Any values returned must be correct. Returning no value (empty) passes. An error margin is allowed for `duration` (as a guideline, ±100 milliseconds or 1%).

Guidelines for implementation with ffprobe / libavformat:

- `duration` is `format.duration`. `width` / `height` are the values from the video stream for video.
- Ogg and Opus tags are in `streams[].tags`, not `format.tags`.
- Embedded cover images in MP3 and M4A are reported as video streams with `attached_pic`. If these are counted as video, audio files will end up as `video`.
- `track` (in the form `3/12`) and `date` (in the form `2024-05-06`) need to be normalized to the specification's forms: `track` (track number only) and `year` (first 4 digits).

## Implementing ImageInfo / IsMediaLoadable / IsImageLoadable

- **ImageInfo** follows the same rules as MediaInfo (keys, units, empty strings for values that could not be retrieved, and path handling). Set `Result` to `image` only when the image's pixel dimensions can be retrieved, and leave all `Value` fields empty for audio and video files.
- The four levels of **IsMediaLoadable / IsImageLoadable** (`none` / `read` / `embed` / `write`) describe the capabilities of the baseware itself. `embed` means “can be incorporated into and processed by ghosts or balloons” (that is, the baseware can load it as a resource such as a surface or balloon image, or audio for `\![sound]`). `write` means “can be written in that format.” `read` is for formats that can be read, but are not guaranteed to be incorporated and processed; in SSP, this applies to formats for which it has no built-in loader and instead relies on OS codecs. In implementations that use their own loaders to read resources, most readable formats will be `embed`, so `read` need not be returned if there are no formats that qualify as `read`. Higher levels include the lower levels.
- The basis for the determination (header or extension) is not specified. If the file does not exist or is a folder, return 400 (`file not found`); otherwise, do not return an error, and return `none` if the file cannot be read.
