# rateofusegraph

**カテゴリ:** Notify event

Notify information for the usage graph. *\[NOTIFY\]*

- **Reference\***: The following information, separated by byte value 1.
  - **1st**: Ghost name.
  - **2nd**: sakura name.
  - **3rd**: kero name.
  - **4th**: Number of launches.
  - **5th**: Launch time (minutes).
  - **6th**: Launch time ratio (%).
  - **7th**: Status.<br />
    boot (running)<br />
    install (installed)<br />
    vanish (uninstalled, but information remains)<br />
    One of the above.
  - **8th**: Number of launches (weekly report; total for the 7 days up to today). \[SSP 2.8.54 and later\]
  - **9th**: Launch time (weekly report, minutes).
  - **10th**: Launch time ratio (weekly report, %).
  - **11th**: Number of launches (monthly report; total for the 30 days up to today).
  - **12th**: Launch time (monthly report, minutes).
  - **13th**: Launch time ratio (monthly report, %).

**対応:** SSP
