
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def marge(x):
            start=min(x.start,newInterval.start)
            end=max(x.end,newInterval.end)
            if end-start<=x.end-x.start+newInterval.end-newInterval.start:
                return True,Interval(start,end)
            return False,newInterval
        merged=[]
        for x in intervals:
            overlaped,newInterval=marge(x)
            if not overlaped:
                merged.append(x)
        ans=[]
        placed=False
        for x in merged:
            if not placed and newInterval.end<x.start:
                ans.append(newInterval)
                placed=True
            ans.append(x)
        
        if not placed and len(ans)==0 or len(ans) and newInterval.start>ans[-1].end:
            ans.append(newInterval)
        return ans