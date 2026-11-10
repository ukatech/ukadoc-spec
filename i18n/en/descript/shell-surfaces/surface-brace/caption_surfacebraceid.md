# ID Specifications Allowed in surface\* Braces

The following notations can be used together. All are SSP-specific.

- **Enumeration with ","**:

  ```
  surface1,3,4,6,12
  {
  // 略
  }
  ```

  Specifying IDs separated by "," allows the same content to be defined for multiple surfaces.

- **Range specification with "-"**:

  ```
  surface1-12
  {
  // 略
  }
  ```

  Specifying IDs using "-" allows the same content to be defined for multiple surfaces in a consecutive range (surface1 through 12 in this example).

- **Excluding IDs from a range with "!"**:

  ```
  surface1-30,!15,!20-25
  {
  // 略
  }
  ```

  IDs listed after "!"—either individual IDs or ranges—are excluded from the definition (in this example, this is equivalent to specifying surface1-14,16-19,26-30).<br />
  Exclusions using ! take precedence over other specifications regardless of their position (for example, even if 3 is added after ! as in surface1-10,!2-4,3, it is excluded).

The original MATERIA specification only allows enumeration with a surface prefix, as shown below.

```
surface1,surface3,surface4
{
// 略
}
```
