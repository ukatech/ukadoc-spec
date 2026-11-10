# Bands and levels reported by sound's --spectrum= \[2.9.18\]

- **How bands are divided**: Uses the standard division by center frequencies from the ISO preferred number series, commonly used in graphic equalizers and spectrum analyzers for audio equipment. The human ear perceives pitch in terms of “how many times higher” a frequency is, rather than “how many Hz higher,” so the bands are also arranged at equal ratios (logarithmically).<br />
  10 bands are spaced one octave (2x) apart (32,64,125,…,16kHz; the same as the equalizer display on a typical music player), 15 bands are spaced 2/3 octave apart, 31 bands are spaced 1/3 octave apart (20Hz–20kHz), and 5 bands are spaced 2 octaves (4x) apart.<br />
  The boundary between bands is the geometric mean of the adjacent center frequencies (multiply them and take the square root), and the lowest and highest bands are extended outward by the same ratio. Therefore, the ranges covered by each band are as shown in the table below, with no gaps or overlaps between bands.

- **Frequencies are fixed regardless of output format**: This table is the same regardless of the sound file format (sample rate, bit depth, number of channels, or type such as mp3, wav, or flac). Internal analysis uses a window of about 85 milliseconds (4096 samples at 44.1kHz and 48kHz), adjusted for the sample rate, giving a frequency resolution of about 11Hz.<br />
  However, there is no sound above half the sample rate (the Nyquist frequency), so any band whose range extends more than halfway above that frequency will always be 0 (for example, in a file with a sample rate of 22.05kHz, bands above about 11kHz will be 0).

- **Level value (0–100)**: The sound energy within a band is summed, converted to the amplitude of a sine wave with an amplitude of 1.0 as the maximum, and expressed in dB, with -60dB mapped to 0 and 0dB (a full-scale sine wave) mapped to 100. The same-amplitude sine wave has the same value in every band, regardless of band width (for example, a sine wave with an amplitude of 0.5 = -6dB is about 90). Multiple channels such as stereo are analyzed as a single averaged sound.<br />
  Values are reflected immediately when they rise, and fall from 100 to 0 over 500 milliseconds when they decrease. The overall level (Reference2) uses the same scale and is the level of the entire sound before it is divided into bands (it has the same value even when --spectrum-bands=0).<br />
  Since the band width at the low-frequency end (roughly below 100Hz) is close to the frequency resolution (about 11Hz), sound in an adjacent band can affect it. Even when a sine wave is played, its value may be slightly lower than expected, or some of it may spill over into an adjacent band.

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
