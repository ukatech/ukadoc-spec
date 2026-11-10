# OnMusicPlayEx

**カテゴリ:** Other events

Notifies the ghost of information about the currently playing track in supported music player software, such as the Windows default media player.<br />
If this event is not handled, it falls back to OnMusicPlay.<br />
Note that all video and music playback in browsers is treated as OnVideoPlayEx.

- **Reference0**: Track title
- **Reference1**: Artist name
- **Reference2以降**: Extended information name\[byte value 1\]extended information content [OnMusicPlayEx extended information list](caption_musicplayex_codes.md)

**対応:** SSP 2.7.55
