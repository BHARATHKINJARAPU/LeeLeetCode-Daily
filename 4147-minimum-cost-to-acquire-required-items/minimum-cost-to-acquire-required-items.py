class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 <= 0 and need2 <= 0:
            return 0
            
        if need1 > need2:
            need1, need2 = need2, need1
            cost1, cost2 = cost2, cost1
            
        c1 = need1 * cost1 + need2 * cost2
        c2 = need1 * costBoth + (need2 - need1) * cost2
        c3 = need2 * costBoth
        
        return min(c1, c2, c3)