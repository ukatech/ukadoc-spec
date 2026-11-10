# OnDarkTheme

**カテゴリ:** OS state event

Occurs when the OS switches to a dark theme (darker display).<br />
Notified as NOTIFY (cannot speak) immediately after startup, and as GET (can speak) when the theme changes.

- **Reference0**: 0/1: Application setting; 1 is dark theme, 0 is normal (light) theme
- **Reference1**: 0/1: System setting; 1 is dark theme, 0 is normal (light) theme (2.6.29)

**対応:** SSP 2.5.02
