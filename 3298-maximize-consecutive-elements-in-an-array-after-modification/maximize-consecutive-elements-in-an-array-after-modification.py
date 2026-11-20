from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        max_val = nums[-1] + 2
        dp = [0] * max_val
        
        for num in nums:
            dp[num + 1] = dp[num] + 1
            dp[num] = dp[num - 1] + 1
            
        return max(dp)