# reduce

**カテゴリ:** surface brace \> Drawing Methods

Composites the transparency of the *base layer* and *new layer*. Think of it as "cutting out" the base layer using the new layer's transparency information.<br />
The *opacity* of the *base layer* and the *new layer* is multiplied (valid transparent colors are treated as fully transparent areas).<br />
For example, an area with 40% opacity in the *base layer* and 60% opacity in the *new layer* becomes an area with 24% opacity = 76% transparency after compositing.<br />
Information other than transparency (RGB values) is simply ignored.<br />
Areas outside the *new layer* are treated as transparent.<br />
This method was provided for dressup, but can also be used in animations that are not dressup and in elements.

**対応:** Materia / SSP
