import sys
from typing import List

# Increase recursion depth for skewed trees up to N = 10^5
sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        ans = [1] * n
        # Tracks the closest ancestor for each character 'a'-'z'
        last_seen = [-1] * 26
        
        def dfs(u: int) -> None:
            char_idx = ord(s[u]) - 97  # ord('a') == 97
            prev_ancestor = last_seen[char_idx]
            
            # Determine u's new parent before updating last_seen with u itself
            new_p = prev_ancestor if prev_ancestor != -1 else parent[u]
            
            last_seen[char_idx] = u
            for v in adj[u]:
                dfs(v)
            last_seen[char_idx] = prev_ancestor  # Backtrack
            
            # Propagate u's final subtree size directly to its new parent
            if new_p != -1:
                ans[new_p] += ans[u]
                
        dfs(0)
        return ans