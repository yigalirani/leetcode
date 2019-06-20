
import itertools
def vcomb(v):
    return [x for l in range(0, len(v)+1) for x in itertools.combinations(v, l)] # all combinations , variable length

@functools.lru_cache(maxsize=128) #3.4 and above
frozenhash and tuple of hashable elements are also hashable - usefull in many cashed
to sort a tuple t, do this tuple(sorted(t)) - usefult to make them unique see leetcode 39
generator is something list a list
iterator is womwthing that support next
tokenizer:
class Tokenzier:
    def __init__(self,s):
        self.s=s
        self.head=0
    def read(self):
        ans=self.look()
        if ans is not None:
            self.head+=1
        return ans
    def look(self):
        if self.head==len(self.s):
            return None
        return self.s[self.head]

deque
chr/ord
collections.deque:
append, popleft
while(d): #check if dqusue empty

from heapq import *
def sort(v):
    h=[]
    for x in v:
        heappush(h,x)
    ans=[]
    while h:
        x=heappop(h)
        ans.append(x)
    return ans
also usefull
heapq.heapify(v) #heapify in place in linear time
heap.heapreplace

to convert str to list:
list(str)
flaten list:
grid[i][j] for row in rows(I,J) for (i,j) in row 
treat first of generator diffrenk:
r=iter(range(10))
first=next(r)
print('flrst',first)
#print('first',first)
for row in r: