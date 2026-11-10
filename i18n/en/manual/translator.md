# Translator

In a ghost, a translator is called MAKOTO.

It can be placed on both the ghost side and the shell side (CROW supports the ghost side only).

To use it on the ghost side, `makoto.dll` must be placed directly under master.

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-makoto.dll
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　:
　　　　　　:
```

To use it on the shell side, makoto.dll must be placed directly under each shell folder.

```filetree
+-(myghost)
　　+-shell
　　　　+-master(またはadditional_shell)
　　　　　　+-makoto.dll
　　　　　　+-descript.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-surfaces.txt
　　　　　　:
　　　　　　:
```

It works as a filter on scripts created by SHIORI, replacing strings.

If it is present on both the ghost and shell sides, the ghost-side translation runs first, followed by the shell-side translation.

Translation occurs just before the text is displayed in the balloon.

As with SHIORI, there are many files that can be used as MAKOTO, and you need to refer to the documentation for each one for details on how to use it.

In the past, before SHIORI existed, it was used to change dialogue, but SHIORI now mainly handles that role.

Today, it is sometimes used for mechanisms such as changing a character's speech style based on the shell.

Translation is also possible with SHIORI Event OnTranslate (that is, SHIORI also serves as the ghost-side MAKOTO).

If both MAKOTO and SHIORI perform translation, the processing order is SHIORI → MAKOTO.
