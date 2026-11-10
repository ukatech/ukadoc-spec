# Bands and levels reported by sound --spectrum= \[2.9.18\]

- **How the bands are divided**: The bands use the standard ISO preferred center frequencies, as commonly used by graphic equalizers and spectrum analyzers in audio equipment. The human ear perceives pitch in terms of “how many times higher” a frequency is, rather than “how many Hz higher,” so the bands are arranged in equal ratios (logarithmically).<br />
  The 10-band setting uses one octave (2×) per band (32,64,125,…,16kHz; the same as the equalizer display on a typical music player), the 15-band setting uses 2/3 octave per band, the 31-band setting uses 1/3 octave per band (20Hz–20kHz), and the 5-band setting uses two octaves (4×) per band.<br />
  The boundary between bands is the geometric mean (multiply and take the square root) of the neighboring center frequencies. The lowest and highest bands are extended outward by the same ratio. Therefore, each band covers the range shown in the table below, with no gaps or overlaps between bands.

- **Frequencies are fixed regardless of output format**: This table is the same regardless of the sound file format (sample rate, bit depth, number of channels, or type such as mp3, wav, or flac). Internal analysis uses a window of about 85 milliseconds, adjusted to the sample rate (4096 points at 44.1kHz and 48kHz), giving a frequency resolution of about 11Hz.<br />
  However, no sound exists above half the sample rate (the Nyquist frequency), so any band with more than half its range above that frequency will always be 0 (for example, in a file with a sample rate of 22.05kHz, bands above about 11kHz will be 0).

- **Level values (0–100)**: The sound energy within a band is summed, converted to the amplitude of a sine wave with amplitude 1.0 as the maximum, and expressed in dB, with -60dB mapped to 0 and 0dB (a full-scale sine wave) mapped to 100. Regardless of band width, sine waves with the same amplitude have the same value in every band (for example, a sine wave with amplitude 0.5 = -6dB is about 90). Multiple channels such as stereo are analyzed as a single sound averaged across the channels.<br />
  Values update immediately when they rise, and fall from 100 to 0 over 500 milliseconds when they decrease. The overall level (Reference2) uses the same scale and represents the level of the entire sound before it is divided into bands (the value is the same when --spectrum-bands=0).<br />
  Because the low-frequency bands (roughly 100Hz and below) have widths close to the frequency resolution (about 11Hz), they can be affected by sounds in the immediately neighboring bands. A sine wave may produce a value slightly below its actual value, or spill over into a neighboring band.

- **5 bands (center frequencies and ranges: Hz)**:

  | Number | 0 | 1 | 2 | 3 | 4 |
  | --- | --- | --- | --- | --- | --- |
  | Center | 63 | 250 | 1000 | 4000 | 16000 |
  | Range | 32～125 | 125～500 | 500～2000 | 2000～8000 | 8000～32000 |

- **10 bands (default)**:

  | Number | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Center | 32 | 64 | 125 | 250 | 500 | 1000 | 2000 | 4000 | 8000 | 16000 |
  | Range | 23～45 | 45～89 | 89～177 | 177～354 | 354～707 | 707～1414 | 1414～2828 | 2828～5657 | 5657～11314 | 11314～22627 |

- **15 bands**:

  | Number | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Center | 25 | 40 | 63 | 100 | 160 | 250 | 400 | 630 | 1000 | 1600 | 2500 | 4000 | 6300 | 10000 | 16000 |
  | Range | 20～32 | 32～50 | 50～79 | 79～126 | 126～200 | 200～316 | 316～502 | 502～794 | 794～1265 | 1265～2000 | 2000～3162 | 3162～5020 | 5020～7937 | 7937～12649 | 12649～20239 |

- **31 bands**:

  | Number | Center | Range | Number | Center | Range | Number | Center | Range |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 0 | 20 | 18～22 | 11 | 250 | 224～281 | 22 | 3150 | 2806～3550 |
  | 1 | 25 | 22～28 | 12 | 315 | 281～355 | 23 | 4000 | 3550～4472 |
  | 2 | 31.5 | 28～36 | 13 | 400 | 355～447 | 24 | 5000 | 4472～5612 |
  | 3 | 40 | 36～45 | 14 | 500 | 447～561 | 25 | 6300 | 5612～7099 |
  | 4 | 50 | 45～56 | 15 | 630 | 561～710 | 26 | 8000 | 7099～8944 |
  | 5 | 63 | 56～71 | 16 | 800 | 710～894 | 27 | 10000 | 8944～11180 |
  | 6 | 80 | 71～89 | 17 | 1000 | 894～1118 | 28 | 12500 | 11180～14142 |
  | 7 | 100 | 89～112 | 18 | 1250 | 1118～1414 | 29 | 16000 | 14142～17889 |
  | 8 | 125 | 112～141 | 19 | 1600 | 1414～1789 | 30 | 20000 | 17889～22361 |
  | 9 | 160 | 141～179 | 20 | 2000 | 1789～2236 |  |  |  |
  | 10 | 200 | 179～224 | 21 | 2500 | 2236～2806 |  |  |  |
