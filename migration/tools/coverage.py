"""page-level coverage: every character of the page BODY (not just the content container) must land in some
unit, except for the elements that are dropped on purpose (navigation, page title, UI parts)."""
import sys, collections
import conv, layout, verify
from conv import *
from layout import *


def body_text(stem):
    soup = BeautifulSoup(layout.load_html(stem), 'lxml')
    body = soup.body
    # dropped on purpose: site navigation / generated TOC / page title / banners (see migration/README.md)
    for e in body.select('nav.menu-header, nav.sidebar, section.navigation-bar, header, footer, h1#page-title, p.banner, p.author'):
        e.decompose()
    class U: pass
    u = U(); u.title = ''; u.nodes = list(body.children)
    return verify.src_text(u)


def run(stems):
    per = collections.defaultdict(list)
    for u in layout.ALL_UNITS:
        per[u.stem].append(u)
    bad = 0
    for s in stems:
        a = collections.Counter(verify.norm(body_text(s)))
        b = collections.Counter()
        for u in per[s]:
            b.update(verify.norm(verify.src_text(u)))
        # ':' is added by the verifier for entry <dl>s; titles are counted on the unit side
        diff = {k: (a[k], b[k]) for k in set(a) | set(b) if a[k] > b[k] and k != ':'}
        print(s, 'LOST' if diff else 'ok', dict(list(diff.items())[:12]) if diff else sum(a.values()))
        bad += bool(diff)
    print('coverage problems:', bad)


if __name__ == '__main__':
    stems = sys.argv[1:] or sorted(p.stem for p in SRC.glob('*.html') if p.stem not in SKIP_PAGES)
    for s in stems:
        layout.layout_page(s)
    run(stems)
