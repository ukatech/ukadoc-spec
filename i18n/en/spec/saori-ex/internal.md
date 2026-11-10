# Common rules for built-in modules

These are the rules shared by modules built into SSP whose names start with `internal_`. (Their names start with `internal_` to avoid conflicts with SAORI DLLs with the same name.)<br />
These modules can only be called from Direct SSTP. They cannot be loaded as DLLs.

## Functions and arguments

`Argument0` is the function name (case-insensitive), and `Argument1` onward are its arguments. An unknown function name returns 400 (`unknown function`).<br />
Each function takes a fixed number of **positional arguments**, followed by **options** (`--name=value`).

- A value in a positional argument's position is treated as data, not as an option, even if it starts with `--`.
- Options can only be written after positional arguments. When writing an option while skipping an optional positional argument, include an empty argument.
- Option names are case-insensitive. If the same name is written twice, the later one takes effect.
- `--name` without an `=` is equivalent to `--name=` with an empty value. Options with empty values can also be written. For example, `--aad=` represents "empty additional authentication data." However, if an option that requires a value to be meaningful (such as `--async=` or `--iv=`) is empty, the function fails (usually with 400 `invalid parameter`).
- Arguments and options that take numbers require decimal integers, which may have a sign (`+` or `-`). Spaces, hexadecimal numbers, and decimals are not allowed. If a value cannot be read as a number, the result is 400 (`invalid parameter`); if it does not fit in a signed 64-bit integer, the result is 400 (`out of range`). The valid range is determined by each function.
- A value after the positional arguments that does not start with `--`, or an option not accepted by the function, results in 400 (`invalid parameter`). This can happen when passing an option added in a newer SSP to an older SSP, so you can check whether an option is supported with [internal_system's Describe](internal_system/internal_system.Describe.md).
- \[SSP 2.9.25\] Functions with no fixed number of positional arguments ([MediaInfo in internal_file](internal_file/internal_file.MediaInfo.md) and, \[SSP 2.9.27\] [ImageInfo](internal_file/internal_file.ImageInfo.md)) read everything from the first value starting with `--` in the second or later position as options.
- All functions accept [`--async=identifier`](async.md).

```
Argument0: Digest
Argument1: sha256
Argument2: SGVsbG8=
Argument3: --data-in=base64
Argument4: --out=base64
```

## Byte input formats

Hashes and similar operations work with byte sequences, but SAORI can pass only strings. Each argument that takes a byte sequence has a name (such as `data`, `key`, `password`, `salt`, `ciphertext`, `signature`, `a`, and `b`; see each function's description), and you can change how the argument is read with `--name-in=format`. For example: `--key-in=hex`, `--data-in=base64`.<br />
Byte sequences passed as options (`--aad=`, `--iv=`, `--info=`) work the same way; you can change how they are read with options such as `--aad-in=hex`.

- **text**: Converts the string to bytes using the character encoding specified by `--charset=` (default: **UTF-8**). This is not the request's `Charset` (so the result is the same regardless of the sender's character encoding, as with Web API signatures). If a character cannot be represented in that encoding, the result is 400 (`invalid encoding`).
- **hex**: Hexadecimal. Uppercase and lowercase are both accepted. An odd number of digits or a non-hexadecimal character results in 400 (`invalid encoding`).
- **base64 / base64url**: Padding (`=`) is optional. Both formats accept characters from base64 and base64url (`+ / - _`). Any other character or invalid padding results in 400 (`invalid encoding`).
- **base32**: RFC 4648. Uppercase and lowercase are both accepted, and padding is optional. Invalid characters result in 400 (`invalid encoding`).
- **url**: Percent-decodes the value. `+` is not converted to a space. If the two characters after `%` are not hexadecimal digits, the result is 400 (`invalid encoding`).
- **bech32**: \[SSP 2.9.14\] BIP-173 bech32 (such as nostr's `npub1...` / `nsec1...`; bech32m cannot be read). Converts the data part to a byte sequence. The part before `1` (the HRP, such as `npub`) is ignored, so check the beginning of the string in your script if you need to verify its type. All-uppercase and all-lowercase strings are accepted. Mixed case, an invalid checksum, or an invalid character results in 400 (`invalid encoding`). There is no length limit (BIP-173's limit of 90 characters does not apply).
- **file**: Treats the value as a file path and reads the file contents. This can only be used for `data` in `Digest` / `HMAC` in `internal_crypto` (using it with another function or an argument other than `data` results in 400 `invalid parameter`).<br />
  Paths follow the rules in [File paths](#ファイルのパス). If the file does not exist, the result is 400 (`file not found`); if reading fails partway through, the result is 500 (`file read failed`).

The default format is defined for each argument (see each function's description). Decoded data is limited to 8 MB per argument (`too large`), but since a Direct SSTP request itself is limited to 1 MB, the actual limit is lower. `file` is read in chunks, so it has no size limit.

## Byte output formats

Functions that return byte sequences can change how the result is written with `--out=format`. The default format is defined for each function. The default output format matches the default input format for the same name, so you can pass the output directly to another function.

- **hex**: Hexadecimal (lowercase).
- **HEX**: Hexadecimal (uppercase). Format names are case-insensitive, but `HEX` in `--out=` is an exception: the output is uppercase only when written as `HEX` (`Hex` produces lowercase hexadecimal). For input `--name-in=`, `HEX` is read as the same format as `hex`.
- **base64**: With padding.
- **base64url**: Without padding.
- **base32**: RFC 4648. With padding.
- **url**: Converts all characters other than RFC 3986 unreserved characters (`A-Z a-z 0-9 - . _ ~`) to `%XX` (uppercase).
- **bech32**: \[SSP 2.9.14\] BIP-173 bech32 (lowercase). Specify the HRP (such as `npub`, 1–83 characters) with `--hrp=`. Only [Convert in internal_data](internal_data/internal_data.Convert.md) accepts `--hrp=`; using `--out=bech32` with another function results in 400 (`invalid parameter`).
- **text**: Returns the result as a string using the encoding specified by `--charset=` (default: UTF-8). If the bytes cannot be converted back correctly using that encoding, or contain NUL or a newline (which cannot be written in a SAORI header), the result is 500 (`not text`).<br />
  Responses are returned using the request's `Charset` encoding, so characters that cannot be represented in that encoding become `?`. To ensure any character can be received, send the request with `Charset: UTF-8`.

For `--charset=`, specify a character encoding name (such as `UTF-8`, `Shift_JIS`, or `EUC-JP`). An unknown name, UTF-16, or UTF-32 results in 400 (`invalid parameter`).

## File paths

These rules apply to arguments that specify files (`--data-in=file` and the functions in [internal_file](internal_file/index.md)).

- Relative paths are resolved from the ghost folder (ghost/master). A relative path passed in a call with no ghost results in 400 (`ghost required`).
- Both `/` and `\` can be used as separators.
- If a directory is passed to an argument that expects a file, it is treated as if the file does not exist and results in 400 (`file not found`).
- \[SSP 2.9.33\] If a file is passed to an argument that expects a directory (the source directory for `CompressArchive`), the result is 400 (`invalid parameter`).
- **There are no restrictions on files that can be read.** Operations that only read files (hashing with `--data-in=file`, `MediaInfo` / `ImageInfo` / `IsMediaLoadable` / `IsImageLoadable`, the archive for `ExtractArchive`, and the source for `CompressArchive`) can read files outside SSP-managed folders when given an absolute path. Only write destinations (the destination for `CompressArchive` and the extraction destination for `ExtractArchive`) are restricted to SSP-managed folders. Since file existence can be determined by whether the result is `file not found`, do not pass user input or similar directly as a path.

## Responses and failure reasons

On success, the result is returned in `Result` with status 200. If the result is an empty string, the status is 204. Functions that return a boolean return `1` (true) or `0` (false) with status 200. A result such as "no match" is not a failure.<br />
In addition to the common cases, [ErrorDescription](directsstp.md) can contain the following:

- **unsupported algorithm**: 400. Unknown algorithm name.
- **invalid encoding**: 400. The value cannot be read in the format specified by `--name-in=`, or compressed data is corrupted.
- **invalid key**: 400. The key length does not match the algorithm, the key cannot be read as a public-key cryptography key, or the key type does not match the method.
- **out of range**: 400. A number or date/time is outside the supported range.
- **too large**: 400. The data is too large.
- **file not found**: 400. The file specified by `--data-in=file` does not exist.
- **not text**: 500. The value cannot be converted back to a string with `--out=text`.
- **file read failed**: 500. Reading the file failed partway through.
- **authentication failed**: 500. Decryption failed (for example, because the ciphertext was tampered with or the key is incorrect), or a JWT could not be verified.
- **expired / not yet valid**: 500. The JWT has expired (`exp`) / the current time is before its valid-from time (`nbf`).
- **internal error**: 500. An unexpected failure occurred inside the baseware.
