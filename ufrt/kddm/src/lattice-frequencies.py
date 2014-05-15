from itertools import chain,combinations,product
from collections import defaultdict

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

I = 'abcdef'
T = ['abc', 'acdef', 'abc', 'de']

dep = defaultdict(list)
for X in powerset(I):
    cnt = sum([1 for i in T if set(X).issubset(set(i))])
    if (cnt != 0):
        n = ''.join(X)
        dep[cnt].append(n)

for c in sorted(dep):
    s = sorted(dep[c], key=lambda x: (len(x), x))
    print c, ':', ','.join(s)

