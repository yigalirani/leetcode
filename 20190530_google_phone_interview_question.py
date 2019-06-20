Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.


“01?1?” -> [“01010”, “01110”, “01011”, “01111”]

def f(p):
	if len(p)==0:
		yield ‘’
		return

	for s in f(p[:-1]):
		if p[-1]==’?’:
			yield s+’1’
			yield s+’0’
		else:
		       yield p



Given a string, find the length of the longest substring that starts and ends with the same letter.

def f(s):
	h={}
	for i,x in enumerate(s):
		if x not in h:
			h[x]=i
	max_len=0
	for i in range(len(s)-1,-1,-1):
		the_len=i-h[s[i]]
		max_len=max(max_len,the_len)
	return max_len
	

   0  1  2  3  4
0  ~  #  T  T  
1  ~  ~  #  #  #
2  ~  ~  #  ~  ~
3  ~  #  #  ~  
4  ~  ~  #  ~  

WATER = 1
LAND = 2
TREASURE = 3

class Map:
  def width(self):
    …

  def height(self):
    …

  # Returns value at position
  def get(self, coord):
    …

  # Returns list of neighbor coordinates
  def neighbors(self, coord):
    …
def f(m):
	h=collections.counter()
	def fill(i,j):
		cell= m.get((i,j))
		if cell==WATER:
			a[i][j]=0
return
		if a[i][j] is not None:
			return
		if cell==’TREASURE’:
			h(cur_island)+=1
		m[i][j]=cur_island
		for i1,j1 in m.neighbors((i,j)):
			fill(i1,j1)
		
		
		
	cur_island=1
	a=[[None]*m.width() for x in range(m.height())]
	for i in range(m.width()):
		for j in range(m.height()):
			fill(i,j)
			cur_island+=1
	return max(h.values())
			
def f(source,dest,m):
	q=collections.deque()
	s=set()
	s.add((source,0)):
	while(q):
		top,cost=q.popleft():
		if top==dest:
			return cost
		for x in m.neighbors(top):
			if x in s:
				continue
			s.add(x)
			if m.get(x)==WATER:
				x_cost=0
			else:
				x_cost=1
			q.add((x,cost+x_cost))
