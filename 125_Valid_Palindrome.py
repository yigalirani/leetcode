def is_alphanumeric(c):
    return  c>='a' and c<='z' or c>='0' and c<='9'

class Solution(object):
    def isPalindrome(self, s):
        #s=s.lower()
        print(s)
        left=0
        right=len(s)-1
        while True:
            if right<=left:
                return True
            if not is_alphanumeric(s[left]):
                left+=1
                continue
            if not is_alphanumeric(s[right]):
                right-=1
                continue      
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
print(Solution().isPalindrome(",M 9y\"yj\"j9 M,"))