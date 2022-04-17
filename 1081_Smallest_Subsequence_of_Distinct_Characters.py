#shttps://leetcode.com/problems/smallest-subsequence-of-distinct-characters/discuss/308210/JavaPython-Stack-Solution-O(N)
class Solution:
    def smallestSubsequence(self, S):
        last = {c: i for i, c in enumerate(S)}
        stack = []
        for i, c in enumerate(S):
            if c in stack: continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)

print(Solution().smallestSubsequence("cdadabcc"))