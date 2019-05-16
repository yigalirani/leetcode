class Solution(object):
    def romanToInt(self, s):
        def calc(I,V,X):
            #print's=',s
            t=[I,
            I+I,
            I+I+I,
            I+V,
            V,
            V+I,
            V+I+I,
            V+I+I+I,
            I+X]
            maxsuffix=''
            maxvaue=0
            for i,suffix in enumerate(t):
                if s.endswith(suffix):
                    if len(suffix)>len(maxsuffix):
                        maxsuffix=suffix
                        maxvaue=i+1
            #print maxsuffix,maxvaue
            return len(maxsuffix),maxvaue

        l='IVXLCDMV '
        ans=0
        mult=1
        while(s):
            eaten,value=calc(l[0],l[1],l[2])
            ans+=value*mult
            mult*=10
            if eaten:
                s=s[:-eaten]
            #print ans,s,mult,eaten
            l=l[2:]
        #print' none'
        return ans
print(Solution().romanToInt('MCMXCIV'))