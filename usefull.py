import itertools
def vcomb(v):
    return [x for l in range(0, len(v)+1) for x in itertools.combinations(v, l)] # all combinations , variable length