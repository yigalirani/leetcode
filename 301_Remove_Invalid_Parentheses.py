class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isvalid(s):
            counter = 0
            for c in s:
                if c == '(':
                    counter += 1
                elif c == ')':
                    counter -= 1
                if counter < 0:
                    return False
            return counter == 0
        
        level = {s}
        while True:
            valid = list(filter(isvalid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
            print(level)


# Test the function
if __name__ == "__main__":
    s = "(a)())()"
    solution = Solution()
    result = solution.removeInvalidParentheses(s)
    print(result)  # Output: ["(a())()", "(a)()()"]