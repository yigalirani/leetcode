from collections import defaultdict
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        h=defaultdict(int)
        for x in barcodes:
            h[x]+=1
        items=[list(x) for x in h.items()]
        items=sorted(items,key=lambda x: x[1],reverse=True)
        print(items)
        n=len(barcodes)
        ans=[None]*n
        head=0
        first_item=items[0]
        items=items[1:]
        for i in range(first_item[1]):
            ans[i*2]=first_item[0]
        
        ans_head=0
        def append(value):
            nonlocal ans_head
            if ans[ans_head] is not None:
                ans_head+=1
            ans[ans_head]=value
            ans_head+=1
        while items:
            head=head%len(items)
            item=items[head]
            append(item[0])
            item[1]-=1
            if item[1]==0:
                del items[head]
            else:
                head+=1                
        return ans
ans=Solution().rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8])
print (ans)