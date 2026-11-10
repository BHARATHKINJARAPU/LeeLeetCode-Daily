class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        if n == 0:
            return 0
        
        dp3, dp2, dp1 = 0, 0, 0
        current = 0
        
        for j in range(1, n + 1):
            cost_j = costs[j - 1]
            option1 = dp1 + cost_j + 1
            option2 = dp2 + cost_j + 4 if j >= 2 else float('inf')
            option3 = dp3 + cost_j + 9 if j >= 3 else float('inf')
            
            current = min(option1, option2, option3)
            
            dp3 = dp2
            dp2 = dp1
            dp1 = current
            
        return current