# Writing to Sound Properties \[2.8.72\]

Of the sound properties, [position](sound.position.md), [playing](sound.playing.md), and [pause](sound.pause.md) support writing via [`\![set,property,～]`](../../../sakura-script/property-system-operation/bang-set-property.md). All other sound properties are read-only.

Writes are converted into the same processing as the corresponding Sakura Script tags. Thus, the result is exactly the same as when writing the tags directly; if the specified operation is invalid (for example, writing pause to media that is already stopped), nothing happens, just as with the tags.

Because the converted tags specify the target by element name, if multiple media items have the same element name, even when the target is specified by [index(ID)](../currentghost.sound.index-ID.md), the write is applied to the most recently created media item with a matching element name. Note that the target may differ from the one used for reading.

Also, writes are performed asynchronously, so the result may not yet be reflected if you read the same property immediately after writing to it.
