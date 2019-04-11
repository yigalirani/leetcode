def  getkth(v1,v2,k): #translated to python from soluton number 3
    l1=len(v1)
    l2=len(v2)
    if l1>l2:  # let l1 <= l2
        return getkth(v2,v1, k)
    if l1==0:
        return v2[k-1]
    if (k==1):
        return min(v1[0], v2[0])
    i=min(l1,k/2)
    j=min(l2,k/2)
    if v1[i-1] > v2[j-1]:
        return getkth(v1,v2[j:],k-j)
    else:
        return getkth(v1[i:],v2,k-i)

class Solution(object):
    def findMedianSortedArrays(self,v1,v2):
        m=len(v1)
        n=len(v2)
        l=(m+n+1)/2
        r=(m+n+2)/2
        return (getkth(v1,v2,l) + getkth(v1,v2,r)) / 2.0