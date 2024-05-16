# Time Complexity : O(n*2^n)
# Space Complexity : O(n*2^n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#Approach 1: BFS
from typing import List, deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        sets = set()
        q = deque()
        q.append(s)
        sets.add(s)
        flag = False

        def isValid(s):
            count = 0
            for i in range(0, len(s)):
                c = s[i]
                if c.isalpha(): 
                    continue
                if c == '(':
                    count += 1
                elif c == ')':
                    if count == 0:
                        return False
                    else:
                        count -= 1
            return count == 0

        while q and not flag:
            size = len(q)
            for i in range(0, size):
                curr = q.popleft()
                if(isValid(curr)):
                    flag = True
                    result.append(curr)
                if not flag:
                    for j in range(0, len(curr)):
                        c = curr[j]
                        if(not c.isalpha()):
                            child = curr[0:j] + curr[j+1:]
                            if child not in sets:
                                q.append(child)
                                sets.add(child)
        return result

#Approach 2: DFS
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        sets = set()
        maxVal = 0

        def dfs(s):
            nonlocal maxVal
            # base case
            if len(s) < maxVal or s in sets:
                return
            # logic
            if isValid(s):
                if len(s) > maxVal:
                    maxVal = len(s)
                    result.clear()  # clear previous results as we found a longer valid string
                if len(s) == maxVal:
                    result.append(s)
            sets.add(s)
            for i in range(len(s)):
                c = s[i]
                if c.isalpha():
                    continue
                child = s[:i] + s[i+1:]
                dfs(child)

        def isValid(s):
            count = 0
            for i in range(len(s)):
                c = s[i]
                if c.isalpha():
                    continue
                if c == '(':
                    count += 1
                elif c == ')':
                    if count == 0:
                        return False
                    else:
                        count -= 1
            return count == 0

        dfs(s)
        return result               
        