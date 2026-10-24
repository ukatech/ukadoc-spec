# Windows上のSSPにおけるXInput固有の仕様

Windows上のSSPではXInput APIを使用してゲームパッド入力を取得している。そのため以下の制約がある。

- **対応コントローラ**: XInput対応ゲームパッド（Xbox系コントローラ等）のみ。DirectInput専用のコントローラは認識されない。
- **同時接続数**: 最大4台。パッドインデックスは0～3の範囲。
- **OnGamepadAxisMoveのReference2（生値）の範囲**: スティックは-32768～32767、トリガーは0～255。
