# Time Complexity : O(V+E)
# Space Complexity : O(V)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
#Approach 1: BFS
from typing import Optional, List, Node, deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        q = deque()
        hashmap = {}
        q.append(node)
        hashmap[node] = Node(val = node.val)

        while q:
            curr = q.popleft()
            for ne in curr.neighbors:
                if ne not in hashmap:
                    hashmap[ne] = Node(val = ne.val)
                    q.append(ne)
                hashmap[curr].neighbors.append(hashmap[ne])
        
        return hashmap[node]

#Approach 2: DFS
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}

        def dfs(node):
            #base
            if node in hashmap:
                return 

            copy = Node(node.val)
            hashmap[node] = copy

            for ne in node.neighbors:
                dfs(ne)
                hashmap[node].neighbors.append(hashmap[ne])
            return copy
            

        if node is None:
            return None
        dfs(node)

        return hashmap[node]