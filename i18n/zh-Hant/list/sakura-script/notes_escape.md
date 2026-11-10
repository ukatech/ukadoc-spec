# Sakura Script escaping

- To display "\\" as a character rather than as the Sakura Script start marker, write it as "\\\\"
- Similarly, write the environment-variable insertion tag "%" as "\\%"
- Within tags that take arguments inside square brackets (such as `\q[ラベル名,ID]`), "\]" can be written as "\\\]".
- If you want a comma "," to be part of the second or a later argument in a tag with multiple arguments inside square brackets, enclose the entire argument in "" to treat it as a single argument.<br />
  Example: `\![raise,OnTest,"100,2"]`
- Similarly, if you want a double quote """ to be part of an argument, enclose the entire argument in "" and double each ".<br />
  Example: `\![call,ghost,"the ""MobileMaster"""]`
