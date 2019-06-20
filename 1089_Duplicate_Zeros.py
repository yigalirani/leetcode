class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        def calc_heads():
            oh=0
            ih=0
            while True:
                if oh>=n-1:
                    return ih,oh
                x=arr[ih]
                ih+=1
                oh+=1
                if x==0:
                    oh+=1

        ih,oh=calc_heads()
        print(ih,oh,ih)
        ih-=1
        def write(c,i):
            if i<n:
                print
                arr[i]=c
                print(i,)
        while ih>=0:
            c=arr[ih]
            ih-=1
            write(c,oh)
            oh-=1
            if c==0:
                write(c,oh)
                oh-=1
inout=[1,0,2,3,0,4,5,0]
#inout=[1,2,3]

inout=[8,4,5,0,0,0,0,7]
Solution().duplicateZeros(inout)
print(inout)

84580000