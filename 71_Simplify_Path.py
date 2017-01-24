class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        cur=[]
        for x in path.split('/'):
            if x=='..':
                if len(cur):
                    del cur[-1]
                continue
            if x=='.' or x=='':
                continue
            cur.append(x)
        return '/'+'/'.join(cur)
        