# Property System

## Overview

The property system lets ghosts access and read or write various parameters that the baseware maintains while running.

- [Reference: CROW test item documentation](http://crow.aqrs.jp/devtest.html)

## 記述例

There are two ways to use the property system: environment variables and regular tags.<br />
See also the sections on the property system in Sakura Script and environment variables.

- **[%property\[property name\]](../../sakura-script/environment-variable/pct-property.md)**: Reference a property as an environment variable and insert its value.<br />
  Use this when you simply want to display the value as-is.<br />
  The following inserts (displays) the baseware name and version at that location.

  ```
  %property[baseware.name] ver,%property[baseware.version]
  ```

- **[`\![get,property,event name,property name]`](../../sakura-script/property-system-operation/bang-get-property.md)**: Use a Sakura Script tag to trigger a SHIORI Event with an arbitrary name, then retrieve a property through its Reference.<br />
  Use this when you want the SHIORI side to perform an action based on a property.<br />
  The following triggers a SHIORI Event with the ID "OnGetSakuraName" and sends the name of the partner (Teddy) of the ghost "Emily/Phase4.5" as reference0.

  ```
  \![get,property,OnGetSakuraName,ghostlist(Emily/Phase4.5).keroname]
  ```

- **[`\![set,property,property name,value]`](../../sakura-script/property-system-operation/bang-set-property.md)**: Use a Sakura Script tag to change a property.<br />
  Not all properties can be written to, but those marked *\[SET enabled\]* on this page can be manipulated in this way.<br />
  The following hides the shell "ULTIMATE FORM" from the shell-switching menu in the owner-draw menu.

  ```
  \![set,property,currentghost.shelllist(ULTIMATE FORM).menu,hidden]
  ```
