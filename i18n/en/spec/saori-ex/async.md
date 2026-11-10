# Asynchronous calls

Functions in built-in modules (those whose names begin with `internal_`) run asynchronously when given the `--async=identifier` option. Once the request is accepted, the response is returned immediately with status 204, and the result is later delivered to the calling ghost as an event.<br />
This cannot be used when calling without a ghost (400 `ghost required`). If the identifier is empty, the response is 400 (`invalid parameter`).<br />
Use `--async` for time-consuming operations (such as hashing large files or passwords, deriving keys, or generating RSA key pairs).<br />
In SSP, up to roughly the number of CPUs (2–4) asynchronous calls can run at the same time. Any additional calls wait in order until an earlier one finishes.

## Event that delivers the result

- **Event name**: If the identifier starts with `On` (case-sensitive), that name is used on success, and “identifier + `Failure`” on failure. Avoid using the name of an existing event (such as `OnBoot`) as the identifier, as the result will be delivered as that event.<br />
  Otherwise, [OnInternalSaoriComplete](../../list/shiori-event/other/OnInternalSaoriComplete.md) is used on success, and [OnInternalSaoriFailure](../../list/shiori-event/other/OnInternalSaoriFailure.md) on failure.
- **Reference on success**: Reference0 = identifier, Reference1 = result (the `Result` of a synchronous call), Reference2 = module name, Reference3 = function name, Reference4 onward = `Value0` onward.
- **Reference on failure**: Reference0 = identifier, Reference1 = reason for failure (the same string as `ErrorDescription` in a synchronous call), Reference2 = module name, Reference3 = function name.

Incorrect numbers of arguments or option names result in a 400 response upon acceptance. Errors in argument contents (such as unreadable hexadecimal) are delivered in the failure event.

## Conditions and order of result delivery

- If the calling ghost has not exited, the result is always delivered. It is delivered even while the ghost is time-critical or in passive mode or guidance mode (it is delivered as long as SHIORI remains loaded, even if it is stored in the cache). \[SSP 2.9.27\] Before this version, results might not be delivered if processing finished while in these states.
- If SHIORI is processing another request, delivery waits until it finishes.
- If the calling ghost exits before the result is delivered (including when SHIORI is reloaded), the result is not delivered.
- Results from multiple asynchronous calls may not arrive in the order the calls were made (they arrive in order of completion, and calls that wait because the number of concurrent calls has been exceeded start in the order that slots become available). If order matters, match results by identifier, or make the next call after the previous result arrives.
