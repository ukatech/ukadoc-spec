# Sakura Script Escaping

- To display "\\” as a character rather than as the start symbol for Sakura Script, write it as "\\\\”
- Similarly, write the environment-variable embedding tag "%" as "\\%"
- Within tags that take arguments inside square brackets (such as `\q[ラベル名,ID]`), "\]" can be written as "\\\]".
- In the second and subsequent arguments of tags with multiple arguments inside square brackets, if you want "," to be part of an argument, enclose the entire argument in "" to treat it as a single argument.<br />
  Example: `\![raise,OnTest,"100,2"]`
- Similarly, if you want "”" to be part of an argument, enclose the entire argument in "" and double the ” character.<br />
  Example: `\![call,ghost,"the ""MobileMaster"""]`
