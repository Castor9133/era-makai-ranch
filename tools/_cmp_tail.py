# -*- coding: utf-8 -*-
import pathlib, re
root = pathlib.Path(r'C:/Cursor local/era-makai-ranch/ERB')
hpath = next(root.rglob('*イッシュ口上1.ERB'))
h = hpath.read_text(encoding='utf-8')
i = pathlib.Path(r'C:/Cursor local/era-makai-ranch/tools/_boyish_clean_init.erb').read_text(encoding='utf-8')
needle = 'ELSEIF SOURCE:尻穴射精经验'
mh, mi = h.index(needle), i.index(needle)
th, ti = h[mh:], i[mi:]
print('tails equal', th == ti)
if th != ti:
    for n in range(min(len(th), len(ti))):
        if th[n] != ti[n]:
            print('diff at', n, repr(th[n:n+40]), repr(ti[n:n+40]))
            break
