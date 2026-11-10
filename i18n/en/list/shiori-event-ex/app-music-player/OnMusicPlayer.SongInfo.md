# OnMusicPlayer.SongInfo

**カテゴリ:** Music player notification event

Notifies all running ghosts of information about the music player's internal state. *\[NOTIFY\]*<br />
Because implementations are added and updated on the ghost side, some ghosts using older versions have fewer References.

- **Reference0**: The sakura name of the ghost that sent the event.
- **Reference1**: The file path of the currently loaded song. Empty if no song is loaded.
- **Reference2**: The song's number in the current playlist. -1 if no song is loaded. It is also -1 in some situations, such as when playback continues after the song has been removed from the playlist.
- **Reference3**: Playback state. 0 when stopped, 1 when playing, and 2 when paused.
- **Reference4**: Current volume. 0–100.
- **Reference5**: Current playback speed. Usually 0–400. Some implementations may support speeds above 400.
- **Reference6**: Current left-right balance. -100 is fully left, 0 is center, and 100 is fully right.
- **Reference7**: Playback mode. The numbers correspond to the following modes.
  - 0 - Loop playlist
  - 1 - Shuffle and loop
  - 2 - Loop one song
  - 3 - Play one song only
  - 4 - Random
- **Reference8**: Special flags for stopping playback. "stop after playback" means playback stops when the current song ends, while "stop after playlist" means playback stops when the current playlist ends (this applies in both "Loop playlist" and "Shuffle and loop" modes). Empty if neither flag is set.
- **Reference9**: Number of songs in the current playlist.
