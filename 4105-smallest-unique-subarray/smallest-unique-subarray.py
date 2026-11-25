from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # Suffix Automaton states (at most 2*n - 1 states)
        max_states = 2 * n
        length = [0] * max_states
        link = [-1] * max_states
        cnt = [0] * max_states
        transitions = [{} for _ in range(max_states)]
        
        size = 1
        last = 0
        
        # Build Suffix Automaton
        for x in nums:
            cur = size
            size += 1
            length[cur] = length[last] + 1
            cnt[cur] = 1
            
            p = last
            while p != -1 and x not in transitions[p]:
                transitions[p][x] = cur
                p = link[p]
                
            if p == -1:
                link[cur] = 0
            else:
                q = transitions[p][x]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = size
                    size += 1
                    length[clone] = length[p] + 1
                    transitions[clone] = transitions[q].copy()
                    link[clone] = link[q]
                    # Cloned state starts with cnt = 0 (not a new prefix ending)
                    
                    while p != -1 and transitions[p].get(x) == q:
                        transitions[p][x] = clone
                        p = link[p]
                        
                    link[q] = clone
                    link[cur] = clone
                    
            last = cur
            
        # Counting sort states by length descending to propagate endpos counts
        order = sorted(range(1, size), key=lambda i: length[i], reverse=True)
        for v in order:
            if link[v] != -1:
                cnt[link[v]] += cnt[v]
                
        # Find minimum length among all states that occur exactly once
        ans = n
        for v in range(1, size):
            if cnt[v] == 1:
                min_len_in_state = length[link[v]] + 1
                if min_len_in_state < ans:
                    ans = min_len_in_state
                    
        return ans