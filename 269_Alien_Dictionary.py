from collections import defaultdict
def tsort(dag):
  ans=[]
  has_cycles=False
  temp_mark=set()
  perm_mark=set()
  #for k,v in dag.items():
  #  print(k,list(v))
  def visit(c):
    nonlocal has_cycles
    if c in perm_mark:
      return
    if c in temp_mark:
      has_cycles=True
      return
    temp_mark.add(c)
    children=dag.get(c)
    for node in (dag.get(c) or set()):
      visit(node)
    perm_mark.add(c)
    ans.append(c)
  for c in dag.keys():
    visit(c)
  if (has_cycles):
    return ''
  return ''.join(ans)
  

class Solution:
  def alienOrder(self,words):
    trie={}
    dag=defaultdict(set)
    
    for word in words:
      head=trie
      max_i=len(word)-1
      for i,c in enumerate(word):
        dag[c]=dag[c] or set()
        for lower in head.keys():
            if (lower!=c): #avoid cycles
              dag[c].add(lower)        
        head[c]=head.get(c) or {}
        head=head[c]
        if i==max_i and len(head):
          return ''
    return tsort(dag)
cases=[
  ["z","z"],
  ["abc","ab"],
  ["wrt","wrf","er","ett","rftt"],
  ["z","x","z"]

]
for case in cases:
  print(Solution().alienOrder(case))  
      
        

