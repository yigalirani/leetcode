class Solution:
    def largestSumOfAverages(self, A, K):
        n=len(A)
        def avg(start,end):
            ans=sum(A[i] for i in range(start,end))/(end-start)
            return ans
        def f(start,k):
            print('---',start,k,'---\\')
            ans=0
            if k==1:
                return avg(start,n)
            for i in range(start+1,n):
                a=avg(start,i)
                b=f(start+1,k-1)
                ans=max(ans,a+b)
            print('---',ans,'---//')
            return ans
        return f(0,K)
Solution().largestSumOfAverages([9,1,2,3,9],3)


