# OnDarkTheme

**カテゴリ:** OS state event

Occurs when the OS switches to the dark theme (a darker display).<br />
Notified with NOTIFY (cannot speak) immediately after startup, and with GET (can speak) when the theme changes.

- **Reference0**: 0/1: Application setting; 1 means dark theme, 0 means normal (light) theme
- **Reference1**: 0/1: System setting; 1 means dark theme, 0 means normal (light) theme (2.6.29)

**対応:** SSP 2.5.02
