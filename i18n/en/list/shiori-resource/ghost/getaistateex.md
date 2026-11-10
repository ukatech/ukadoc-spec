# getaistateex

**カテゴリ:** Ghost information

A version of getaisate that allows multiple specifications. Reference0 is passed the index of the graph data being requested (the number is zero-based).<br />
To display only two graphs, respond when Reference0 is 0 or 1, and return no value (204) for 2 or higher.<br />
The format is the same as getaistate.

- **Reference0**: Which graph's data this is (zero-based). 0, 1, 2…

**対応:** SSP 2.4.26
