# rateofusegraph

**カテゴリ:** Notify event

Notifies usage graph information. *\[NOTIFY\]*

- **Reference\***: The following information, separated by byte value 1.
  - **1st**: Ghost name.
  - **2nd**: sakura name.
  - **3rd**: kero name.
  - **4th**: Number of launches.
  - **5th**: Running time. (minutes)
  - **6th**: Running time percentage. (%)
  - **7th**: Status.<br />
    boot (running)<br />
    install (installed)<br />
    vanish (uninstalled information remains)<br />
    One of the above.
  - **8th**: Number of launches. (weekly report, total from today back to 7 days ago) \[SSP 2.8.54 and later\]
  - **9th**: Running time. (weekly report, minutes)
  - **10th**: Running time percentage. (weekly report, %)
  - **11th**: Number of launches. (monthly report, total from today back to 30 days ago)
  - **12th**: Running time. (monthly report, minutes)
  - **13th**: Running time percentage. (monthly report, %)

**対応:** SSP
