# OnMusicPlayEx

**カテゴリ:** Other events

Notifies the ghost of information about the currently playing song from supported music players, such as the standard Windows media player app.<br />
If this event is not handled, it falls back to OnMusicPlay.<br />
Note that all video and music playback in browsers is handled as OnVideoPlayEx.

- **Reference0**: Song title
- **Reference1**: Artist name
- **Reference2 onward**: Extended information name\[byte value 1\]extended information content [OnMusicPlayEx extended information list](caption_musicplayex_codes.md)

**対応:** SSP 2.7.55
