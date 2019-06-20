import collections
same code, easier to read:

    def normalize_row(r):
        return tuple(x ^ r[0] for x in r) 

    def maxEqualRowsAfterFlips(A):
        the_counter=collections.Counter(normalize_row(r) for r in A)
        return max(the_counter.values())
print(f([[0,1],[1,0]]))
print(f([[0,0,0],[0,0,1],[1,1,0]]))