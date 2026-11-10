# getaistate

**カテゴリ:** Ghost information

The SHIORI/3.0 version of the AI graph.<br />
Draws a radar chart for internal ghost state (number of talks, affection level, etc.).<br />
Return the data in the following format.

Graph display values \[byte value 1\] graph labels \[byte value 1\] graph additive values \[byte value 1\] graph maximum values

- **Graph display values**: Return the values to display on the graph as comma-separated half-width numbers.<br />
  Decimal places are supported from 2.4.26.
- **Graph labels (optional)**: Return the labels to display on the graph, separated by commas.<br />
  If omitted: Neuron,NeuronM,NeuronK,NeuronD,NeuronE,Synapse
- **Graph additive values (optional)**: Return the graph "additive values" as comma-separated half-width numbers.<br />
  Decimal places are supported from 2.4.26.<br />
  Additive values are a feature that highlights values increased through learning or values that have changed recently, by adding them to the graph display values.<br />
  If omitted: all zero, not displayed
- **Graph maximum values (optional)**: Return the graph maximum values as comma-separated half-width numbers. Maximum value ≧ (display value + additive value).<br />
  Decimal places are supported from 2.4.26.<br />
  If omitted: calculate display value + additive value and set the maximum of those values for all elements

Example: 1250,1500,45,65,19500,4\[b1\]horsepower,rpm,km/h,t,kgf,axis\[b1\]100,50,40,0,0,1\[b1\]1350,1550,130,96,20000,8<br />
\[b1\] indicates byte value 1.<br />
The display will look as follows.<br />
![AI Graph](../../../assets/image/aigraph.png)

**対応:** SSP recognizes decimal places from 2.4.26
