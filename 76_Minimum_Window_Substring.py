from collections import defaultdict
def build_hash(t):
  ans=defaultdict(int)
  for c in t:
    ans[c]+=1
  return ans

class Solution(object):
  def minWindow(self,s,t):
    needed_hash=build_hash(t)
    cur_hash=defaultdict(int)
    missing=len(t)
    front=-1
    back=0
    output=''
    def grow():
      nonlocal missing,front,back
      while front+1<len(s):
        front+=1
        c=s[front]
        if not needed_hash.get(c):
          continue
        cur_hash[c]+=1
        if (cur_hash[c]>needed_hash[c]):
          continue
        missing-=1
        if missing==0:
          return True
      return False
    def shrink():
      nonlocal back,front,output,missing
      while back<=front:
        c=s[back]
        back+=1
        if needed_hash.get(c)==None:
          continue
        cur_hash[c]-=1
        if cur_hash[c]<needed_hash[c]:
          missing+=1
          if output=='' or front-back+1<len(output):
            output=s[back-1:front+1]
          return
    while(grow()):
      shrink()
    return output
a=Solution()
print(a.minWindow("ADOBECODEBANC", "ABC"))