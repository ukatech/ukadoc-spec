import sys
import verify
import coverage
from conv import *
stems = sys.argv[1:] or sorted(p.stem for p in SRC.glob('*.html') if p.stem not in SKIP_PAGES)
verify.run(stems)
verify.check_anchors()
verify.check_code_lines()
coverage.run(stems)
