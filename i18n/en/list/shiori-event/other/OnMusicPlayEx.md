# OnMusicPlayEx

**カテゴリ:** Other events

Notifies the ghost of information about the song playing in a supported music player, such as the standard Windows media player app.<br />
If this event is not handled, it falls back to OnMusicPlay.<br />
Note that all video and music playback in browsers is treated as OnVideoPlayEx.

- **Reference0**: Song title
- **Reference1**: Artist name
- **Reference2 and later**: Extension information name\[byte value 1\]extension information contents [OnMusicPlayEx extension information list](caption_musicplayex_codes.md)

**対応:** SSP 2.7.55
