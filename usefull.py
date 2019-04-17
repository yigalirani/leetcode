import itertools
def vcomb(v):
    return [x for l in range(0, len(v)+1) for x in itertools.combinations(v, l)] # all combinations , variable length

@functools.lru_cache(maxsize=128) #3.4 and above
frozenhash and tuple of hashable elements are also hashable - usefull in many cashed
to sort a tuple t, do this tuple(sorted(t)) - usefult to make them unique see leetcode 39
generator is something list a list
iterator is womwthing that support next