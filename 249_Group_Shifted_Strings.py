from collections import defaultdict
def calc_group(s):
    def shift(c):
        shft=ord('z')-ord(s[0])
        return chr(
            (
              ord(c)+
              shft
            ) 
            % 
            (ord('z')-ord('a')+1)
            +ord('a')
        )
        
    return ''.join(shift(c) for c in s)
class Solution:
    def groupStrings(self, strings):
        h=defaultdict(list)
        for s in strings:
            h[calc_group(s)].append(s)
        print(h)
        return h.values()
calc_group('za')        
ans=Solution().groupStrings(['az','ba'])
print(ans)