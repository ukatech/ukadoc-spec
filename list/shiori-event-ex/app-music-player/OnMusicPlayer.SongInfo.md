# OnMusicPlayer.SongInfo

**カテゴリ:** Music player通知イベント

Notifies information about the music player's internal state to all open ghosts. *\[NOTIFY\]*<br />
Because the implementation is added and updated on the ghost side, some ghosts may use an older version with fewer references.

- **Reference0**: The sakura name of the ghost that sent the event.

- **Reference1**: The file path of the currently loaded song. Empty if no song is loaded.

- **Reference2**: The playlist index number of the currently loaded song. -1 if no song is loaded, and in certain circumstances when a song has been removed from the playlist but is still playing.

- **Reference3**: The playback state. 0 if stopped, 1 if playing music, and 2 if playback is paused.

- **Reference4**: The current volume, from 0-100.

- **Reference5**: The current playback speed, usually from 0-400. Some implementations may allow speeds higher than 400.

- **Reference6**: The current left/right balance. -100 is all the way to the left, 0 is centered, and 100 is all the way to the right.

- **Reference7**: The play mode. Numbers correspond to the following modes.

  - 0 - Loop Playlist
  - 1 - Shuffle and Loop
  - 2 - Loop One Song
  - 3 - Play One Song
  - 4 - Random

- **Reference8**: A special flag for stopping playback. "stop after playback" means playback will stop when the current song ends. "stop after playlist" means playback will stop when the current playlist ends (applicable in both "Loop Playlist" and "Shuffle and Loop" modes). Empty if neither flag is set.

- **Reference9**: The number of songs in the current playlist.
