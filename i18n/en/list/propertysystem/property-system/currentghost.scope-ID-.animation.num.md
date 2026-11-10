# currentghost.scope(ID).animation.num

**カテゴリ:** Property System

Animation IDs for the current ghost's scope ID.<br />
When retrieved: A comma-separated list of the IDs of animations currently running. This reflects only the state at the moment of retrieval; it is not guaranteed that the animations will still be running after the result is received and processed.<br />
When set: Runs the specified animation IDs in addition. Animations with IDs that are not specified are not stopped; the specified animations are simply added. Multiple IDs can be set at once as a comma-separated list, behaving the same as specifying multiple `\i[]` tags in succession.

**対応:** SSP 2.8.28
